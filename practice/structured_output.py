import json

# Python dictionary
response = {
    "name": "Chandra",
    "skill": "Python",
    "experience": "Fresher",
    "status": "Available"
}

# Convert Python dictionary into JSON string
json_output = json.dumps(response, indent=4)

print(json_output)

# Access individual values
print("Name:", response["name"])
print("Skill:", response["skill"])
print("Experience:", response["experience"])

# Convert JSON string into Python dictionary
prompt = json_output

data = json.loads(prompt)

print("\nConverted Python Data:")
print(data)

# Access values from converted data
print("Student Name:", data["name"])
print("Student Skill:", data["skill"])