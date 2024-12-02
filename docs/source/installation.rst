Installation
============

To set up and run the RagOllamm Document Query App, follow these steps:

Prerequisites Ensure you have the following installed on your system before proceeding: - Python 3.8 or above - Pip (Python's package manager) - Git - [Ollama LLM Backend](https://www.ollama.ai/) (for serving the language model)

Steps to Install 1. **Clone the Repository** First, clone the repository from GitHub to your local machine: ``` git clone <repository> cd <repository> ```

2. **Set Up a Virtual Environment** Create and activate a virtual environment to isolate dependencies: - On **Windows**: ``` python -m venv Ragenv Ragenv\Scripts\activate ``` - On **macOS/Linux**: ``` python3 -m venv Ragenv source Ragenv/bin/activate ```

3. **Install Required Dependencies** Install the necessary Python packages: ``` pip install -r requirements.txt ``` This will install all the dependencies, including: - Streamlit - LangChain - Chroma - Ollama LLM libraries

4. **Start the Ollama LLM Backend** Ensure the Ollama LLM backend is running on your local machine. Follow these steps: - Download and install the [Ollama](https://www.ollama.ai/) LLM software. - Start the Ollama server locally by running: ``` ollama serve --port 11434 ``` By default, the backend should be accessible at `http://127.0.0.1:11434`.

5. **Run the Streamlit App** Launch the app using Streamlit: ``` streamlit run streamlit_app.py ```

6. **Access the App** Open the app in your web browser. It will usually be available at: ``` http://localhost:8501 ```

7. **Upload Your Document** In the app, upload a plain text file (`.txt` format) using the file uploader. Start querying your document by entering questions in the provided input box.

Troubleshooting If you encounter any issues during installation or while running the app, here are some common solutions: - **Ollama Backend Not Running**: Ensure the server is active and accessible at `http://127.0.0.1:11434`. Use the following command to start it: ``` ollama serve --port 11434 ``` - **Dependencies Missing**: If any packages are missing, ensure you installed them with: ``` pip install -r requirements.txt ``` - **App Not Starting**: Verify you are in the correct directory and have activated the virtual environment: ``` source Ragenv/bin/activate # macOS/Linux Ragenv\Scripts\activate # Windows ```

Dependencies The `requirements.txt` file should include the following: ``` streamlit langchain_community langchain_ollama ``` These dependencies will ensure the app runs smoothly with all required functionalities.

Notes For additional help, refer to the official documentation of [Streamlit](https://docs.streamlit.io) and [Ollama](https://www.ollama.ai/).
