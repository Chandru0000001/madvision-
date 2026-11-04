from openai import OpenAI
from openai import APIError, AuthenticationError, RateLimitError

client = OpenAI()

try:

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "user",
                "content": "Explain artificial intelligence in 3 lines."
            }
        ]
    )

    result = response.choices[0].message.content

    if result:
        print("AI Response:")
        print(result)
    else:
        print("Error: AI returned an empty response.")

except AuthenticationError:
    print("Error: Please check your API key.")

except RateLimitError:
    print("Error: API rate limit or quota exceeded.")

except APIError as e:
    print("API Error:", e)

except Exception as e:
    print("Unexpected Error:", e)