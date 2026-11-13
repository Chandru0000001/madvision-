from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

# Documents folder path
DOCUMENT_FOLDER = "documents"

# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=150,
    chunk_overlap=30
)

# Read all documents
for filename in os.listdir(DOCUMENT_FOLDER):

    if filename.endswith(".txt"):

        file_path = os.path.join(DOCUMENT_FOLDER, filename)

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read()

        # Split document into chunks
        chunks = text_splitter.split_text(text)

        print("\nDocument:", filename)

        # Display chunks
        for i, chunk in enumerate(chunks):

            print(f"\nChunk {i + 1}:")
            print(chunk)

            print("-" * 40)