import json
from pathlib import Path


# Function 1: Load JSON data
def load_json(filename):
    try:
        file_path = Path(__file__).parent / filename

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("JSON file loaded successfully!")
        return data

    except FileNotFoundError:
        print("Error: JSON file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


# Function 2: Validate employee records
def validate_employees(data):
    if not isinstance(data, dict):
        print("Invalid data: Expected a JSON object.")
        return False

    if "employees" not in data:
        print("Invalid data: 'employees' section is missing.")
        return False

    if not isinstance(data["employees"], list):
        print("Invalid data: Employees must be a list.")
        return False

    required_fields = ["id", "name", "department", "role", "email"]

    for employee in data["employees"]:

        if not isinstance(employee, dict):
            print("Invalid employee: Each record must be an object.")
            return False

        for field in required_fields:
            if field not in employee:
                print(f"Invalid employee: Missing field '{field}'.")
                return False

        if not isinstance(employee["id"], int) or isinstance(employee["id"], bool):
            print("Invalid employee ID: Must be an integer.")
            return False

        for field in ["name", "department", "role", "email"]:
            if not isinstance(employee[field], str) or not employee[field].strip():
                print(f"Invalid employee: '{field}' must be a non-empty string.")
                return False

        if "@" not in employee["email"]:
            print("Invalid employee: Email address is not valid.")
            return False

    print("Employee records validated successfully!")
    return True


# Function 3: Validate task records
def validate_tasks(data):
    if not isinstance(data, dict):
        return False

    if "tasks" not in data:
        print("Invalid data: 'tasks' section is missing.")
        return False

    if not isinstance(data["tasks"], list):
        print("Invalid data: Tasks must be a list.")
        return False

    required_fields = ["taskId", "title", "assignee", "status", "priority"]

    valid_statuses = ["Pending", "In Progress", "Completed"]
    valid_priorities = ["Low", "Medium", "High"]

    for task in data["tasks"]:

        if not isinstance(task, dict):
            print("Invalid task: Each record must be an object.")
            return False

        for field in required_fields:
            if field not in task:
                print(f"Invalid task: Missing field '{field}'.")
                return False

        if not isinstance(task["taskId"], int) or isinstance(task["taskId"], bool):
            print("Invalid task ID: Must be an integer.")
            return False

        for field in ["title", "assignee"]:
            if not isinstance(task[field], str) or not task[field].strip():
                print(f"Invalid task: '{field}' must be a non-empty string.")
                return False

        if task["status"] not in valid_statuses:
            print("Invalid task status:", task["status"])
            return False

        if task["priority"] not in valid_priorities:
            print("Invalid task priority:", task["priority"])
            return False

    print("Task records validated successfully!")
    return True


# Main program
if __name__ == "__main__":

    data = load_json("employees.json")

    if data is not None:
        employees_valid = validate_employees(data)
        tasks_valid = validate_tasks(data)

        if employees_valid and tasks_valid:
            print("\nAll JSON data is valid!")
        else:
            print("\nJSON validation failed.")