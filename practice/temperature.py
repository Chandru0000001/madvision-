from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": "Write a short story about AI."
        }
    ],
    temperature=0.7,
    max_tokens=150
)

print(response.choices[0].message.content)