from flask import Flask, request,jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

from services.pdf_service import process_pdf
from services.rag_service import (create_vectors, retrieve_chunks)
from services.llm_service import generate_answer

load_dotenv()
api_key=os.getenv("GOOGLE_API_KEY")
app=Flask(__name__)

CORS (app)

BASE_DIR=os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER=os.path.join(BASE_DIR,"uploads")
os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route("/")
def home():
    return "PDF Chatbopt backend running"

@app.route("/upload", methods=["POST"])
def upload_pdf():
    file=request.files["file"]
    if not file:
        return jsonify({
            "error":"No file uploaded"
        }),400

    filepath=os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )
    print("FILEPATH:", filepath)
    print("EXISTS:", os.path.exists(filepath))
    print("IS FILE:", os.path.isfile(filepath))
    file.save(filepath)
 
    chunks=process_pdf(filepath)
    print(f"length{len(chunks)}")
    create_vectors(chunks)

    return jsonify({
        "message": "PDF uploaded and processed successfully"
    })

@app.route("/ask", methods=["POST"])
def ask_question():
    data=request.get_json()
    question=data.get("question")
    if not question:
        return jsonify({
            "error":"Question is required"
        }),400

    relevant_docs=retrieve_chunks(question)

    answer=generate_answer(
        question, relevant_docs
    )

    return jsonify({
        "answer":answer
    })

if __name__=="__main__":
    app.run(debug=True)