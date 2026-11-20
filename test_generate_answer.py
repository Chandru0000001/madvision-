from generate_answer import generate_answer


question = "What is Python?"

retrieved_documents = [

    "Python is a high-level programming language.",

    "Python is used for web development, automation and AI.",

    "Python has a simple and readable syntax."

]


answer = generate_answer(
    question,
    retrieved_documents
)


print("\n========== GENERATED ANSWER ==========")

print(answer)

print("\n======================================")