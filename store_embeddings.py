import chromadb
import json
import os


# STEP 1: Load embeddings JSON file

json_file = "chunk_embeddings.json"

if not os.path.exists(json_file):
    raise FileNotFoundError(
        "chunk_embeddings.json not found. Run embeddings.py first."
    )

with open(json_file, "r", encoding="utf-8") as file:

    all_chunks = json.load(file)


print("Total chunks loaded:", len(all_chunks))


# STEP 2: Connect to ChromaDB

client = chromadb.PersistentClient(
    path="./chroma_db"
)


# STEP 3: Create a collection

collection = client.get_or_create_collection(
    name="rag_documents",
    metadata={"hnsw:space": "cosine"}
)


# STEP 4: Prepare data

ids = []

documents = []

embeddings = []

metadatas = []


for chunk in all_chunks:

    # Create unique ID
    chunk_id = f"{chunk['source']}_{chunk['chunk_id']}"

    ids.append(chunk_id)

    # Original text
    documents.append(chunk["text"])

    # Numerical embedding
    embeddings.append(chunk["embedding"])

    # Document information
    metadatas.append({
        "source": chunk["source"],
        "chunk_id": chunk["chunk_id"]
    })


# STEP 5: Store data in ChromaDB

collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings,
    metadatas=metadatas
)


# STEP 6: Verify stored data

print("\n========== CHROMADB RESULTS ==========")

print("Collection name:", collection.name)

print("Total records stored:", collection.count())


# STEP 7: Display stored documents

results = collection.peek(limit=5)

for i in range(len(results["ids"])):

    print("\nID:", results["ids"][i])

    print("Text:", results["documents"][i])

    print("Metadata:", results["metadatas"][i])


print("\n=====================================")

print("Embeddings successfully stored in ChromaDB!")

print("Database location: ./chroma_db")