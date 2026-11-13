import os
import json
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from langchain_text_splitters import RecursiveCharacterTextSplitter


# STEP 1: Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found in .env file")


# STEP 2: Connect to Gemini
client = genai.Client(api_key=api_key)


# STEP 3: Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
)


# STEP 4: Read documents and create chunks
documents_folder = "documents"

all_chunks = []

if not os.path.exists(documents_folder):
    raise FileNotFoundError("Documents folder not found!")


for filename in os.listdir(documents_folder):

    if filename.endswith(".txt"):

        file_path = os.path.join(documents_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read()

        chunks = text_splitter.split_text(text)

        for index, chunk in enumerate(chunks):

            all_chunks.append({
                "source": filename,
                "chunk_id": index + 1,
                "text": chunk
            })


print("\nTotal chunks created:", len(all_chunks))


# STEP 5: Extract chunk text
texts = [chunk["text"] for chunk in all_chunks]


# STEP 6: Generate embeddings in batches
all_embeddings = []

batch_size = 5

for i in range(0, len(texts), batch_size):

    batch_texts = texts[i:i + batch_size]

    print(f"\nProcessing batch {i // batch_size + 1}")

    try:

        response = client.models.embed_content(
            model="gemini-embedding-001",
            contents=batch_texts,
            config=types.EmbedContentConfig(
                task_type="RETRIEVAL_DOCUMENT",
                output_dimensionality=768
            )
        )

        all_embeddings.extend(response.embeddings)

        print("Batch completed successfully!")

        # Wait between batches
        if i + batch_size < len(texts):
            time.sleep(4)

    except Exception as error:

        print("\nEmbedding generation failed!")
        print("Error:", error)

        raise


# STEP 7: Attach embeddings to chunks

if len(all_embeddings) != len(all_chunks):
    raise ValueError("Number of embeddings does not match number of chunks!")

for chunk, embedding in zip(all_chunks, all_embeddings):

    chunk["embedding"] = embedding.values


# STEP 8: Display embedding results
print("\n========== EMBEDDING RESULTS ==========")

for chunk in all_chunks:

    print("\nSource:", chunk["source"])

    print("Chunk ID:", chunk["chunk_id"])

    print("Text:", chunk["text"])

    print("Embedding dimensions:", len(chunk["embedding"]))

    print("First 5 embedding values:",
          chunk["embedding"][:5])


# STEP 9: Save embeddings into JSON
with open("chunk_embeddings.json", "w", encoding="utf-8") as file:

    json.dump(all_chunks, file, indent=4)


print("\n======================================")
print("Embeddings generated successfully!")
print("Total chunks:", len(all_chunks))
print("Total embeddings:", len(all_embeddings))
print("Saved to chunk_embeddings.json")
print("======================================")