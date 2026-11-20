def validate_output(answer):

    # Check whether response exists
    if answer is None:
        return False, "No response received from Gemini."

    # Check empty response
    if not answer.strip():
        return False, "Gemini returned an empty response."

    # Remove unnecessary spaces
    answer = answer.strip()

    # Check minimum response length
    if len(answer) < 5:
        return False, "Generated answer is too short."

    # Check maximum response length
    if len(answer) > 5000:
        return False, "Generated answer is too long."

    # Valid response
    return True, answer