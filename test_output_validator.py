from output_validator import validate_output


test_answers = [

    "Python is a programming language.",

    "",

    None,

    "Hi",

    "     ",

    "Artificial Intelligence helps computers perform tasks."
]


for answer in test_answers:

    print("\nOriginal Answer:", repr(answer))

    is_valid, result = validate_output(answer)

    if is_valid:

        print("Status: Valid")
        print("Answer:", result)

    else:

        print("Status: Invalid")
        print("Reason:", result)