# RAG-Based AI Document Question Answering System

## 1. Project Overview

This project is an AI-powered document question-answering application built using Retrieval-Augmented Generation (RAG).

Users can ask questions about stored documents and receive AI-generated answers based on relevant retrieved information.

The application uses Google Gemini for answer generation and ChromaDB for vector storage and document retrieval.

## 2. Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- LangChain Text Splitters
- ChromaDB
- Python Dotenv
- JSON

## 3. Features

- Document processing and text chunking
- Embedding generation
- Vector database storage
- Semantic similarity search
- AI-powered question answering
- Input validation
- Generated-answer validation
- Error handling and fallback messages
- Logging of application events and failures
- Source document tracking

## 4. Project Structure

```text
RAG_project/
│
├── documents/
├── chroma_db/
├── logs/
│
├── chunking.py
├── embeddings.py
├── store_embeddings.py
├── retrieve.py
├── generate_answer.py
├── input_validator.py
├── output_validator.py
├── logger_config.py
├── main.py
│
├── test_generate_answer.py
├── test_logger.py
├── test_output_validator.py
├── test_retrieval.py
├── test_validator.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## 5. Requirements

- Python 3.10 or compatible version
- Google Gemini API key
- Internet connection for Gemini API requests

## 6. Installation

Clone or download the project.

Open the project directory in VS Code or PowerShell.

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## 7. Environment Configuration

Create a `.env` file in the project directory.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The `.env` file contains sensitive information and must not be uploaded to GitHub.

Use `.env.example` as a template when setting up the project on another computer.

## 8. Preparing Documents and Embeddings

Run the following scripts in order when preparing or rebuilding the document index:

```bash
python chunking.py
python embeddings.py
python store_embeddings.py
```

These scripts prepare document chunks, generate embeddings, and store them in ChromaDB.

## 9. Running the Application

Start the RAG application:

```bash
python main.py
```

Enter your question when prompted.

The application will:

1. Validate the user's question.
2. Retrieve relevant documents.
3. Generate an answer using Google Gemini.
4. Validate the generated answer.
5. Display the answer and source documents.

## 10. Logging

Application events and errors are recorded in:

```text
logs/rag_app.log
```

Check this file when troubleshooting application problems.

## 11. Testing

The project includes individual test scripts.

Run them using Python:

```bash
python test_validator.py
python test_output_validator.py
python test_logger.py
python test_retrieval.py
python test_generate_answer.py
```

## 12. Security

- API keys are stored in environment variables.
- Actual `.env` files must not be committed to Git.
- `.env.example` contains only a placeholder.
- User input is validated before document retrieval.
- Generated answers are validated before display.
- Application errors are logged for troubleshooting.

## 13. Deployment

This project currently runs as a local Python command-line application.

Public deployment would require an appropriate hosting environment and potentially a web interface or API layer.

Do not deploy without an approved hosting environment and secure API-key configuration.

## 14. Project Objective

To build a reliable AI-powered document question-answering system that retrieves relevant information from stored documents and generates context-grounded responses using a Large Language Model.