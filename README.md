# GenAI App With LangSmith

This project is a demonstration of a Generative AI application using LangChain, AWS Bedrock (with the Llama 3 model), and Streamlit for the user interface. It also integrates LangSmith for tracing and monitoring Large Language Model (LLM) calls.

## Screenshots

### Webpage

![Webpage Screenshot](./picture/Screenshot%20from%202025-11-03%2021-32-03.png)

### LangSmith

![LangSmith Screenshot](./picture/Screenshot%20from%202025-11-03%2021-35-29.png)

## Project Structure

- `src/app.py`: The main Streamlit application file.
- `notebooks/`: Contains Jupyter notebooks for experimentation and getting started.
  - `FirstTutorial_langSmith.ipynb`: A great starting point to get introduced to LangChain and LangSmith.
- `requirements.txt`: A list of Python dependencies for this project.
- `.env`: Configuration file for environment variables (e.g., API keys).
- `README.md`: This file.

## LangSmith Integration

This project uses LangSmith for observability, providing full visibility into the LLM application's behavior. The integration is planned in several phases:

1.  **Initial Setup**: Basic tracing to capture all LLM calls, chain execution, latency, and token usage.
2.  **Basic Insights**: Adding metadata like session IDs and environment tags to better organize and filter traces.
3.  **Advanced Features**: Implementing user feedback collection, custom tags, cost tracking, and an analytics dashboard within the Streamlit app.

### Benefits of LangSmith Integration

- **Full Visibility**: Understand your LLM application's behavior.
- **Debugging**: Easily debug issues by reviewing exact traces.
- **User Feedback**: Improve prompts and responses based on user feedback.
- **Cost Monitoring**: Track and optimize spending on LLM calls.
- **Data-Driven Insights**: Gain actionable insights for optimization.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add the following:
    ```
    LANGCHAIN_API_KEY="your-langchain-api-key"
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_PROJECT="your-langchain-project-name"
    ```

## Usage

To run the Streamlit application, execute the following command in your terminal:

```bash
streamlit run src/app.py
```

## First Tutorial

For those new to LangChain and LangSmith, the `notebooks/FirstTutorial_langSmith.ipynb` notebook provides a step-by-step guide to get you started.