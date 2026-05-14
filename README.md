# PDF Chatbot using RAG, LangChain & Gemini API

## Overview

This project is a full-stack AI-powered PDF chatbot application built using Retrieval-Augmented Generation (RAG). Users can upload PDF documents and ask natural language questions based on the uploaded content.

The application processes PDFs, generates vector embeddings, stores them using FAISS, retrieves relevant chunks, and generates AI responses using Google Gemini.

---

## Features

- Upload PDF documents
- Ask questions about uploaded PDFs
- Retrieval-Augmented Generation (RAG)
- Semantic search using vector embeddings
- AI-generated responses using Gemini API
- React-based chat interface
- Flask REST API backend
- FAISS vector database integration

---

## Tech Stack

### Frontend
- React.js
- Axios
- CSS

### Backend
- Flask
- LangChain
- FAISS
- Google Gemini API
- PyPDFLoader

### Database / Storage
- FAISS Vector Store

---

## Project Architecture

```text
PDF
↓
Text Extraction
↓
Chunking
↓
Embeddings
↓
FAISS Vector Store
↓
Retriever
↓
Gemini LLM
↓
AI Response
```

---

## Folder Structure

```text
PDFChatbot/
│
├── Backend/
│   ├── services/
│   │   ├── pdf_service.py
│   │   ├── rag_service.py
│   │   └── llm_service.py
│   │
│   ├── uploads/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   |  ├── chatbox.jsx
│   │   |  ├── upload.jsx
│   │   |  └── message.jsx
│   │   ├── App.css
│   │   ├── App.jsx
│   |   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## Backend Setup

Navigate to backend:

```bash
cd Backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create:

```text
.env
```

Add:

```env
GOOGLE_API_KEY=your_api_key_here
```

---

## Run Backend

```bash
python app.py
```

Backend runs on:

```text
http://localhost:5000
```

---

## Frontend Setup

Navigate to frontend:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Run frontend:

```bash
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## API Endpoints

### Upload PDF

```http
POST /upload
```

### Ask Question

```http
POST /ask
```

Request body:

```json
{
  "question": "What is this document about?"
}
```

---


## Learning Outcomes

This project helped in understanding:

- Retrieval-Augmented Generation (RAG)
- LangChain workflows
- Vector embeddings
- FAISS vector databases
- Prompt engineering
- Flask API development
- React frontend integration
- LLM application architecture

---

## Author

Sneha Sannakki K V