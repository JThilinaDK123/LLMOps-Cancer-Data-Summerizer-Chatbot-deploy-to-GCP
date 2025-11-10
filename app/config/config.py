import os
HF_TOKEN = os.environ.get("HF_TOKEN")

# HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3"
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"
DB_FAISS_PATH="vectorstore/db_faiss"
DATA_PATH="data/"
CHUNK_SIZE=500
CHUNK_OVERLAP=50