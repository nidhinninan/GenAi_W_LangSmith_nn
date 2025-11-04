import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_aws import ChatBedrock
import uuid # add unique ID for each user
from textblob import TextBlob
from langsmith import Client
from langchain_core.callbacks.base import BaseCallbackHandler

load_dotenv()

# Langsmith tracing
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "Bedrock-Streamlit-Demo")

# Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked"),
    ("user", "Question:{question}")
])

# Streamlit UI
st.title("LangChain Demo With Llama 3 Model (8B)")
input_text = st.text_input("What question do you have in mind?")

# Add a unique session ID to track conversations
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

session_id = st.session_state.session_id

# Initialize LangSmith client
client = Client()

# Callback handler to get run_id
class RunIdCallback(BaseCallbackHandler):
    def __init__(self):
        self.run_id = None

    def on_chain_start(self, serialized, inputs, *, run_id, **kwargs):
        self.run_id = run_id
        st.session_state.run_id = run_id

# Ollama model (you can change to gemma3:4b if that's what you downloaded)
# llm = Ollama(model="gemma:2b")
# optionally be explicit about the server:
# llm = Ollama(base_url="http://localhost:11434", model="gemma3:4b")

llm = ChatBedrock(
    model_id="meta.llama3-8b-instruct-v1:0", # Or any other model you have access to
    region_name="us-east-1"      # Or your preferred region
)

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

# Run the chain
if input_text:
    final_query = input_text
    # Spelling correction
    corrected_text = str(TextBlob(input_text).correct())
    if corrected_text.lower() != input_text.lower():
        st.write(f"Did you mean: *{corrected_text}*?")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes, use corrected text"):
                final_query = corrected_text
        with col2:
            if st.button("No, use original text"):
                final_query = input_text

    run_id_callback = RunIdCallback()
    response = chain.invoke(
        {"question": final_query},
        config={
            "metadata": {"session_id": session_id, "original_question": input_text},
            "callbacks": [run_id_callback]
        }
    )
    st.write(response)

if "run_id" in st.session_state:
    run_id = st.session_state.run_id
    feedback = st.radio("Feedback:", ("👍", "👎"), horizontal=True, index=None)
    if feedback:
        score = 1 if feedback == "👍" else 0
        client.create_feedback(run_id=run_id, key="user_rating", score=score)
        st.success("Feedback submitted!")
        del st.session_state.run_id # Clear run_id after feedback
