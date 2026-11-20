def validate_input(question):

    # Check empty input
    if not question:
        return False, "Question cannot be empty."

    # Remove unnecessary spaces
    question = question.strip()

    # Check spaces-only input
    if not question:
        return False, "Please enter a valid question."

    # Check minimum length
    if len(question) < 3:
        return False, "Question is too short."

    # Check maximum length
    if len(question) > 1000:
        return False, "Question is too long."

    return True, question