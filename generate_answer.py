import os
import time

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


# STEP 4: Get user question

question = input("\nEnter your question: ").strip()

if not question:
    raise ValueError("Please enter a question!")


# STEP 5: Convert question into embedding

embedding_response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=question,
    config=types.EmbedContentConfig(
        task_type="RETRIEVAL_QUERY",
        output_dimensionality=768
    )
)

question_embedding = embedding_response.embeddings[0].values


# STEP 6: Retrieve relevant documents

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

retrieved_documents = results["documents"][0]

retrieved_sources = results["metadatas"][0]


if not retrieved_documents:
    print("\nNo relevant documents found.")
    raise SystemExit


# STEP 7: Combine retrieved text into context

context = "\n\n".join(retrieved_documents)


print("\n========== RETRIEVED CONTEXT ==========")

print(context)


# STEP 8: Create prompt for Gemini

prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not available in the context,
say: "I don't have enough information in the provided documents."

Do not make up information.

CONTEXT:
{context}

USER QUESTION:
{question}

Provide a clear and simple answer.
"""


# STEP 9: Send context and question to Gemini

response = None

for attempt in range(3):

    try:

        print("\nConnecting to Gemini...")

        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )

        print("Gemini response received!")

        break

    except Exception as error:

        print("\nGemini request failed:", error)

        if attempt < 2:

            wait_time = 10 * (attempt + 1)

            print(f"Retrying in {wait_time} seconds...")

            time.sleep(wait_time)

        else:

            print("\nGemini is currently unavailable.")
            print("Please try again later.")


# STEP 10: Display AI answer

print("\n========== AI GENERATED ANSWER ==========")

if response is not None and response.text:

    print(response.text)

else:

    print("AI answer could not be generated.")

print("\n=========================================")


# STEP 11: Display source documents

print("\n========== SOURCE DOCUMENTS ==========")

for source in retrieved_sources:

    print("\nSource:", source["source"])

    print("Chunk ID:", source["chunk_id"])


print("\n======================================")

print("\nRAG application completed!")