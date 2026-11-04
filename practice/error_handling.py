try:
    number = int(input("Enter a number: "))
    print("Your number is:", number)

except ValueError:
    print("Error: Please enter a valid number.")

    import jsonhi

ai_response = """
{
    "name": "Chandra",
    "skill": "Python",
    "experience": "Fresher"
}
"""

try:

    data = json.loads(ai_response)

    if all(key in data for key in ["name", "skill", "experience"]):
        print("Valid AI output")
        print("Name:", data["name"])
        print("Skill:", data["skill"])
        print("Experience:", data["experience"])

    else:
        print("Error: Required fields are missing.")

except json.JSONDecodeError:
    print("Error: AI returned invalid JSON.")