import os

import chromadb
from dotenv import load_dotenv
from google import genai
from google.genai import types


# STEP 1: Load Gemini API key

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")


# STEP 2: Connect to Gemini

client = genai.Client(api_key=api_key)


# STEP 3: Connect to ChromaDB

chroma_client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = chroma_client.get_collection(
    name="rag_documents"
)


# STEP 4: Ask the user a question

question = input("\nEnter your question: ")


# STEP 5: Convert question into an embedding

response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question,
    config=types.EmbedContentConfig(
        task_type="RETRIEVAL_QUERY",
        output_dimensionality=768
    )
)

question_embedding = response.embeddings[0].values


# STEP 6: Search ChromaDB

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)


# STEP 7: Display retrieved results

print("\n========== RETRIEVED RESULTS ==========")

for i in range(len(results["documents"][0])):

    print(f"\nResult {i + 1}")

    print("Source:", results["metadatas"][0][i]["source"])

    print("Chunk ID:", results["metadatas"][0][i]["chunk_id"])

    print("Text:", results["documents"][0][i])

    print("Distance:", results["distances"][0][i])


print("\n======================================")