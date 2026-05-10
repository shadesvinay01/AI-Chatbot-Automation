import os
from pypdf import PdfReader
from rag.vector_store import add_knowledge

def process_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def ingest_directory(client_id, directory_path):
    """Read all txt and pdf files from a directory and add to knowledge base."""
    if not os.path.exists(directory_path):
        print(f"Directory {directory_path} not found.")
        return

    all_texts = []
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if filename.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as f:
                all_texts.append(f.read())
            print(f"Processed text: {filename}")
            
        elif filename.endswith(".pdf"):
            pdf_text = process_pdf(file_path)
            all_texts.append(pdf_text)
            print(f"Processed PDF: {filename}")

    if all_texts:
        add_knowledge(client_id, all_texts)
        print(f"Successfully added {len(all_texts)} documents to {client_id}'s knowledge base.")
    else:
        print("No valid files found for ingestion.")

if __name__ == "__main__":
    # Example usage:
    # ingest_directory("demo_restaurant", "./knowledge_source")
    print("Run this script by calling ingest_directory(client_id, path)")
