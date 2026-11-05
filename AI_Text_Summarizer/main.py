import os
import json

from google import genai
from dotenv import load_dotenv


# Load environment variables

load_dotenv()


# Get Gemini API key

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")


# Connect to Gemini API

client = genai.Client(api_key=api_key)


# Create summarization function

def summarize_text(text):

    prompt = f"""
    You are an expert text summarization assistant.

    Your task is to summarize the following text.

    Rules:
    1. Use simple English.
    2. Keep the summary between 2 and 4 sentences.
    3. Include only important information.
    4. Identify the main topic.
    5. Do not add false information.

    Text to summarize:

    {text}
    """

    # Send request to Gemini

    response = client.models.generate_content(

        model="gemini-3.5-flash-lite",

        contents=prompt,

        config={
            "response_mime_type": "application/json",

            "response_json_schema": {
                "type": "OBJECT",

                "properties": {

                    "summary": {
                        "type": "STRING"
                    },

                    "main_topic": {
                        "type": "STRING"
                    }
                },

                "required": [
                    "summary",
                    "main_topic"
                ],

                "additionalProperties": False
            }
        }
    )


    # Get AI response

    result = response.text

    if not result:
        raise ValueError("Gemini returned an empty response")


    # Validate JSON response

    data = json.loads(result)

    if not isinstance(data, dict):
        raise ValueError("Invalid response format")

    if not isinstance(data.get("summary"), str):
        raise ValueError("Summary field is missing or invalid")

    if not isinstance(data.get("main_topic"), str):
        raise ValueError("Main topic field is missing or invalid")

    if not data["summary"].strip():
        raise ValueError("Summary is empty")

    if not data["main_topic"].strip():
        raise ValueError("Main topic is empty")


    return data


# Main program

print("================================")
print("       AI TEXT SUMMARIZER")
print("================================")

user_text = input("\nEnter your text: ")


try:

    # Check user input

    if not user_text.strip():

        raise ValueError("Input text cannot be empty.")


    # Call summarization function

    result = summarize_text(user_text)


    # Display result

    print("\n========== AI SUMMARY ==========")

    print("\nSummary:")

    print(result["summary"])

    print("\nMain Topic:")

    print(result["main_topic"])

    print("\n================================")


except json.JSONDecodeError:

    print("Error: Gemini returned invalid JSON.")

except Exception as e:

    print("Error:", e)