import os
import chromadb

from dotenv import load_dotenv
from google import genai
from google.genai import types

from logger_config import logger


# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")


# Connect to Gemini
client = genai.Client(api_key=api_key)


# Connect to ChromaDB
chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_collection(
    name="rag_documents"
)


# Retrieval function
def retrieve_documents(question):

    try:

        logger.info("Starting document retrieval")

        # Generate question embedding
        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=question,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=768
            )
        )

        question_embedding = response.embeddings[0].values

        logger.info("Question embedding generated")

        # Search ChromaDB
        results = collection.query(
            query_embeddings=[question_embedding],
            n_results=3
        )

        documents = results["documents"][0]

        sources = results["metadatas"][0]

        if not documents:

            logger.warning("No relevant documents found")

            return [], []

        logger.info(
            f"Retrieved {len(documents)} documents successfully"
        )

        return documents, sources

    except Exception:

        logger.exception("Document retrieval failed")

        raise