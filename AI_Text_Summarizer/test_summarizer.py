from main import summarize_text

test_cases = [

    # Test 1: Normal paragraph
    "Python is a programming language used for web development and AI.",

    # Test 2: Long paragraph
    "Artificial Intelligence is transforming the world. "
    "It is used in healthcare, education, banking and transportation. "
    "AI helps organizations automate tasks and analyze large amounts of data.",

    # Test 3: One sentence
    "The Earth revolves around the Sun.",

    # Test 4: Empty input
    "",

    # Test 5: Numbers only
    "123456789 987654321",

    # Test 6: Technical content
    "Machine learning is a branch of AI that allows computers to learn from data.",

    # Test 7: Repeated sentences
    "Python is easy to learn. Python is easy to learn. Python is easy to learn.",

    # Test 8: Different language
    "La inteligencia artificial ayuda a las computadoras a realizar tareas.",

    # Test 9: Random characters
    "@@@###$$$%%%^^^",

    # Test 10: Very long text
    "Artificial Intelligence is useful. " * 100
]


for i, text in enumerate(test_cases, start=1):

    print("\n==============================")
    print(f"TEST CASE {i}")
    print("==============================")

    try:

        if not text.strip():
            raise ValueError("Input text cannot be empty.")

        result = summarize_text(text)

        print("Summary:", result["summary"])
        print("Main Topic:", result["main_topic"])

        print("STATUS: PASS")

    except Exception as error:

        print("Error:", error)
        print("STATUS: FAIL")