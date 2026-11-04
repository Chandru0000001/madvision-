import os
import json

from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Connect to OpenAI
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def summarize_text(text):

    prompt = f"""
    You are an expert text summarization assistant.

    Summarize the following text.

    Rules:
    1. Use simple English.
    2. Keep the summary between 2 and 4 sentences.
    3. Include only important information.
    4. Do not add false information.

    Return valid JSON with these fields:
    {{
        "summary": "Short summary",
        "main_topic": "Main topic"
    }}

    Text:
    {text}
    """

    response = client.responses.create(
        model="gpt-5.5",
        input=prompt
    )

    result = response.output_text

    # Validate JSON response
    data = json.loads(result)

    if not isinstance(data, dict):
        raise ValueError("Invalid response format")

    if not isinstance(data.get("summary"), str):
        raise ValueError("Summary field is missing")

    if not isinstance(data.get("main_topic"), str):
        raise ValueError("Main topic field is missing")

    return data


# Main program
user_text = input("Enter your text: ")

try:
    if not user_text.strip():
        raise ValueError("Input text cannot be empty.")

    result = summarize_text(user_text)

    print("\nAI SUMMARY")
    print("-----------")

    print("Summary:", result["summary"])
    print("Main Topic:", result["main_topic"])

except Exception as e:
    print("Error:", e)