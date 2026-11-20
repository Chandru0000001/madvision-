from input_validator import validate_input

questions = [
    "What is Python?",
    "",
    "   ",
    "Hi",
    "Explain Machine Learning"
]

for question in questions:

    valid, result = validate_input(question)

    print("\nQuestion:", repr(question))

    if valid:
        print("Status: Valid")
    else:
        print("Status: Invalid")
        print("Reason:", result)