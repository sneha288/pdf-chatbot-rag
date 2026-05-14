from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_pdf(filepath):
    loader=PyPDFLoader(filepath)
    documents=loader.load()

    splitter=RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks=splitter.split_documents(documents)

    return chunks