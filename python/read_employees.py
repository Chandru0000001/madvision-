import json
from pathlib import Path

# Get the current Python file's folder
folder_path = Path(__file__).parent

# Locate the JSON file
json_file = folder_path / "employees.json"

# Read the JSON file
with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)


# Display Employee Records
print("\n========== EMPLOYEE RECORDS ==========\n")

for employee in data["employees"]:
    print("Employee ID:", employee["id"])
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Role:", employee["role"])
    print("Email:", employee["email"])
    print("-------------------------------------")


# Display Task Records
print("\n========== TASK RECORDS ==========\n")

for task in data["tasks"]:
    print("Task ID:", task["taskId"])
    print("Title:", task["title"])
    print("Assignee:", task["assignee"])
    print("Status:", task["status"])
    print("Priority:", task["priority"])
    print("-------------------------------------")