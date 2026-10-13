import json
from pathlib import Path

folder_path = Path(__file__).parent

json_file = folder_path / "employees.json"

with open(json_file, "r", encoding="utf-8") as file:
    data = json.load(file)


print("\n********* EMPLOYEE RECORDS *********\n")

for employee in data["employees"]:
    print("Employee ID:", employee["id"])
    print("Name:", employee["name"])
    print("Department:", employee["department"])
    print("Role:", employee["role"])
    print("Email:", employee["email"])


print("\n========== TASK RECORDS ==========\n")

for task in data["tasks"]:
    print("Task ID:", task["taskId"])
    print("Title:", task["title"])
    print("Assignee:", task["assignee"])
    print("Status:", task["status"])
    print("Priority:", task["priority"])