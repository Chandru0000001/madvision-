# RAG-Based AI Document Question Answering System

## Project Overview

This project is an AI-powered document question-answering application built using Retrieval-Augmented Generation (RAG).

Users can ask questions about stored documents and receive AI-generated answers based on the retrieved document information.

## Technologies Used

- Python
- Google Gemini API
- LangChain
- ChromaDB
- JSON

## Project Features

- Document processing
- Text chunking
- Embedding generation
- Vector database storage
- Semantic similarity search
- AI-powered question answering
- Source document tracking
- Context-grounded responses

## Project Structure

```text
RAG_Project/
│
├── documents/
│   ├── python.txt
│   ├── machine_learning.txt
│   └── fastapi.txt
│
├── chunking.py
├── embeddings.py
├── store_embeddings.py
├── retrieve.py
├── generate_answer.py
├── chunk_embeddings.json
├── .env.example
├── .gitignore
└── README.md
```

## Installation

Install the required packages:

```bash
pip install google-genai python-dotenv langchain-text-splitters chromadb
```

## API Configuration

Create a `.env` file in the project directory.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Never upload your actual `.env` file to GitHub.

## How to Run

### Step 1: Generate document chunks

```bash
python chunking.py
```

### Step 2: Generate embeddings

```bash
python embeddings.py
```

### Step 3: Store embeddings in ChromaDB

```bash
python store_embeddings.py
```

### Step 4: Retrieve relevant documents

```bash
python retrieve.py
```

### Step 5: Generate AI answers

```bash
python generate_answer.py
```

## Project Objective

To build an intelligent document question-answering system that retrieves relevant information from documents and uses an LLM to generate context-grounded answers.