import streamlit as st
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Function to initialize LLM and Embedding Model based on user selection

def initialize_model(model_name):
    try:
        llm = OllamaLLM(model=model_name, base_url="http://127.0.0.1:11434")
        embed_model = OllamaEmbeddings(model=model_name, base_url="http://127.0.0.1:11434")
        return llm, embed_model
    except Exception as e:
        st.error(f"Error initializing model {model_name}: {e}")
        return None, None

# Function to process a file and initialize Chroma
def process_file(file_content, embed_model):
    try:
        # Decode and read the uploaded file content
        text = file_content.decode("utf-8")
        st.success("File loaded successfully.")

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=128)
        chunks = text_splitter.split_text(text)

        # Create Chroma vector store
        vector_store = Chroma.from_texts(chunks, embed_model)
        st.success("Chroma vector store initialized successfully.")
        return vector_store
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None

# Streamlit App
def main():
    # Set the page configuration for better aesthetics
    st.set_page_config(
        page_title="Document Query App",
        page_icon="📄",
        layout="wide",
    )

    # Header and Introduction
    st.title("📄 Document Query App")
    st.markdown("""
    **Upload a text file and explore its content by asking questions.**
    This app leverages advanced language models to retrieve relevant information from your documents.
    """)

    # Sidebar for Model Selection
    st.sidebar.title("Settings")
    st.sidebar.markdown("### Choose a Language Model")
    model_choice = st.sidebar.selectbox(
        "Model",
        options=["llama3", "mistral"],
        help="Select the model to use for processing and querying your document."
    )
    llm, embed_model = initialize_model(model_choice)
    if not llm or not embed_model:
        return

    # File Uploader Section
    st.subheader("Step 1: Upload Your Document")
    uploaded_file = st.file_uploader(
        "Upload a plain text (.txt) file:",
        type=["txt"],
        help="Upload a document in plain text format to start querying."
    )
    if uploaded_file:
        st.info("Processing your document. This may take a few moments.")
        vector_store = process_file(uploaded_file.read(), embed_model)
        if not vector_store:
            return

        # Query Section
        st.subheader("Step 2: Ask a Question")
        query = st.text_input(
            "Enter your question about the document:",
            placeholder="Type your question here...",
        )
        if st.button("Submit Query"):
            if not query.strip():
                st.warning("⚠️ Please enter a valid question.")
            else:
                try:
                    retriever = vector_store.as_retriever()
                    docs = retriever.get_relevant_documents(query)
                    if docs:
                        st.success("📄 Relevant Documents Retrieved:")
                        for i, doc in enumerate(docs):
                            st.markdown(f"**Document {i + 1}:**")
                            st.write(doc.page_content)
                    else:
                        st.warning("No relevant documents found.")
                except Exception as e:
                    st.error(f"Error during retrieval: {e}")

# Entry point for the app
if __name__ == "__main__":
    main()
