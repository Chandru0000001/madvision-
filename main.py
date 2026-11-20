# STEP 1: Import required modules

from input_validator import validate_input
from retrieve import retrieve_documents
from generate_answer import generate_answer
from output_validator import validate_output

from logger_config import logger


# STEP 2: Main application function

def main():

    logger.info("RAG application started")

    print("\n================================")
    print("       RAG AI ASSISTANT")
    print("================================")


    # STEP 3: Get user question

    question = input("\nEnter your question: ")


    # STEP 4: Validate input

    is_valid, result = validate_input(question)

    if not is_valid:

        logger.warning("Input validation failed")

        print("\nInvalid question:", result)

        return

    question = result

    logger.info("Input validation successful")


    # STEP 5: Retrieve relevant documents

    print("\nSearching relevant documents...")

    try:

        documents, sources = retrieve_documents(question)

    except Exception:

        logger.exception("Document retrieval failed")

        print("\nUnable to retrieve documents.")

        return


    # STEP 6: Check retrieved documents

    if not documents:

        logger.warning("No relevant documents found")

        print("\nNo relevant information found.")

        print("Please try another question.")

        return


    print(f"\nSuccessfully retrieved {len(documents)} documents.")

    logger.info("Document retrieval completed")


    # STEP 7: Generate answer

    print("\nGenerating AI answer...")

    answer = generate_answer(
        question,
        documents
    )


    # STEP 8: Validate generated answer

    is_valid, result = validate_output(answer)


    if not is_valid:

        logger.warning("Final output validation failed")

        print("\nUnable to generate a valid answer.")

        return


    answer = result

    logger.info("Final output validation successful")


    # STEP 9: Display final answer

    print("\n================================")
    print("          AI ANSWER")
    print("================================")

    print(answer)


    # STEP 10: Display source documents

    print("\n================================")
    print("        SOURCE DOCUMENTS")
    print("================================")

    for source in sources:

        print("\nSource:", source.get("source", "Unknown"))

        print("Chunk ID:", source.get("chunk_id", "Unknown"))


    # STEP 11: Application completed

    print("\n================================")
    print("     RAG APPLICATION COMPLETED")
    print("================================")

    logger.info("RAG application completed successfully")


# STEP 12: Execute application

if __name__ == "__main__":

    try:

        main()

    except KeyboardInterrupt:

        logger.warning("Application interrupted by user")

        print("\nApplication stopped.")

    except Exception:

        logger.exception("Unexpected application error")

        print("\nSomething went wrong. Check logs/rag_app.log")