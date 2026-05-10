from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# Initialize embeddings once
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def get_vector_store(client_id: str):
    """
    Returns a Chroma vector store for a specific client.
    """
    persist_dir = f"./vector_stores/{client_id}"
    os.makedirs(persist_dir, exist_ok=True)
    
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=embeddings
    )

def add_knowledge(client_id: str, texts: list):
    """
    Adds text data to the client's knowledge base.
    """
    vector_store = get_vector_store(client_id)
    vector_store.add_texts(texts)
    return "Knowledge added successfully"
