Here’s the **Installation** section organized in the same style as the **Introduction** section you provided:

```rst
Installation
============

To set up and run the RagOllamm Document Query App, follow the steps below. This guide ensures proper configuration and smooth operation of the app.

Prerequisites
-------------
Before installing, ensure the following tools are installed on your system:
- **Python 3.8 or above**: Required for running the app and its dependencies.
- **Pip**: Python's package manager for installing dependencies.
- **Git**: For cloning the project repository.
- **[Ollama LLM Backend](https://www.ollama.ai/)**: For serving the language model locally.

Steps to Install
----------------

1. **Clone the Repository**  
   Begin by cloning the project repository to your local machine using Git:  
   ```bash
   git clone <repository>
   cd <repository>
   ```

2. **Set Up a Virtual Environment**  
   Create and activate a virtual environment to isolate dependencies for the app.  

   - On **Windows**:  
     ```bash
     python -m venv Ragenv
     Ragenv\Scripts\activate
     ```
   - On **macOS/Linux**:  
     ```bash
     python3 -m venv Ragenv
     source Ragenv/bin/activate
     ```

3. **Install Required Dependencies**  
   Install all necessary Python libraries listed in `requirements.txt`:  
   ```bash
   pip install -r requirements.txt
   ```
   The required dependencies include:  
   - **Streamlit**: For building the app's interactive interface.  
   - **LangChain**: For working with language models and vector stores.  
   - **Chroma**: For vector storage and retrieval.  
   - **Ollama LLM Libraries**: For integrating and running the language models.

4. **Start the Ollama LLM Backend**  
   Ensure the Ollama LLM backend is running. Follow these steps:  
   - Download and install the [Ollama](https://www.ollama.ai/) software.  
   - Start the server locally:  
     ```bash
     ollama serve --port 11434
     ```
   By default, the backend will be accessible at `http://127.0.0.1:11434`.

5. **Run the Streamlit App**  
   Launch the app using the Streamlit command:  
   ```bash
   streamlit run streamlit_app.py
   ```

6. **Access the App**  
   Open your web browser and navigate to:  
   ```
   http://localhost:8501
   ```
   The app will be live, and you can start uploading documents.

7. **Upload Your Document**  
   - Use the file uploader to upload a plain text document (`.txt` format).  
   - Once uploaded, you can query the document by entering questions in the provided input box.

Troubleshooting
---------------
If you encounter issues during installation or while running the app, refer to the solutions below:

- **Ollama Backend Not Running**  
  Ensure the Ollama backend is active. Use the following command to restart it:  
  ```bash
  ollama serve --port 11434
  ```

- **Missing Dependencies**  
  Reinstall the required packages with:  
  ```bash
  pip install -r requirements.txt
  ```

- **App Not Starting**  
  Verify you are in the correct directory and have activated the virtual environment:  
  ```bash
  source Ragenv/bin/activate  # macOS/Linux  
  Ragenv\Scripts\activate     # Windows
  ```

Dependencies
------------
The `requirements.txt` file contains the following dependencies:  
```text
streamlit
langchain_community
langchain_ollama
```
These dependencies ensure the app operates with all required functionalities.

Notes
-----
For further assistance, consult the official documentation of the tools used:  
- **[Streamlit Documentation](https://docs.streamlit.io)**  
- **[Ollama Documentation](https://www.ollama.ai/)**
```

