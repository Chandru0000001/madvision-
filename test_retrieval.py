from retrieve import retrieve_documents

question = "What is Python?"

documents, sources = retrieve_documents(question)

print("\nRETRIEVED DOCUMENTS:")

for document in documents:
    print(document)

print("\nSOURCES:")

for source in sources:
    print(source)