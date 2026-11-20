import os
import time

from dotenv import load_dotenv
from google import genai

from logger_config import logger
from output_validator import validate_output


# STEP 1: Load Gemini API key

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Gemini API key not found!")


# STEP 2: Connect to Gemini

client = genai.Client(api_key=api_key)


# STEP 3: Create answer generation function

def generate_answer(question, retrieved_documents):

    # Check retrieved documents

    if not retrieved_documents:

        logger.warning("No documents available for generation")

        return "I don't have enough information in the provided documents."


    # STEP 4: Prepare context

    context = "\n\n".join(retrieved_documents)


    # STEP 5: Create prompt

    prompt = f"""
    You are a helpful AI assistant.

    Answer the user's question using ONLY
    the information provided in the context.

    Rules:

    1. Do not invent information.
    2. Use simple English.
    3. If information is missing, say:
       I don't have enough information in the provided documents.

    CONTEXT:

    {context}

    USER QUESTION:

    {question}

    ANSWER:
    """


    # STEP 6: Generate answer with retry

    response = None

    for attempt in range(3):

        try:

            logger.info("Sending request to Gemini")

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            logger.info("Gemini response received")

            break

        except Exception:

            logger.exception(
                f"Gemini API attempt {attempt + 1} failed"
            )

            if attempt < 2:

                wait_time = 5 * (attempt + 1)

                logger.warning(
                    f"Retrying in {wait_time} seconds"
                )

                time.sleep(wait_time)

            else:

                logger.error("All Gemini API attempts failed")

                return "Sorry, the AI service is currently unavailable."


    # STEP 7: Validate generated answer

    if response is None:

        return "Answer generation failed."


    is_valid, result = validate_output(response.text)


    if not is_valid:

        logger.warning("Generated answer failed validation")

        return "Sorry, a valid answer could not be generated."


    logger.info("Answer generated and validated successfully")

    return result