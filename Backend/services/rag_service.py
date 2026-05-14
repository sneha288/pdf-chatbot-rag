from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
print("APIKEY",api_key)
vector_store=None

embeddings=GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001"
)

def create_vectors (chunks):
    global vector_store
    vector_store=FAISS.from_documents(
        chunks,
        embeddings
    )

def retrieve_chunks(question):
    global vector_store
    if vector_store is None:
        raise ValueError("No pdf has been processed yet!")
    retriever=vector_store.as_retriever(search_kwargs={"k":2})
    docs=retriever.invoke(question)

    return docs