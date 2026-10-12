import json
import re
from pathlib import Path


# Load JSON file safely
def load_json(filename):
    file_path = Path(__file__).parent / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("Success: JSON file loaded.")
        return data

    except FileNotFoundError:
        print(f"Error: File '{filename}' was not found.")
    except json.JSONDecodeError as error:
        print(
            f"Error: Invalid JSON syntax at line {error.lineno}, "
            f"column {error.colno}: {error.msg}"
        )
    except OSError as error:
        print(f"Error: Could not read file: {error}")

    return None


# Validate employee records
def validate_employees(data):
    if not isinstance(data, dict):
        print("Error: The main JSON data must be an object.")
        return False

    if "employees" not in data:
        print("Error: Missing required section 'employees'.")
        return False

    if not isinstance(data["employees"], list):
        print("Error: 'employees' must contain a list.")
        return False

    required_fields = [
        "id",
        "name",
        "department",
        "role",
        "email"
    ]

    valid = True

    for index, employee in enumerate(data["employees"], start=1):
        print(f"\nChecking employee record {index}:")

        if not isinstance(employee, dict):
            print("Error: Employee record must be a JSON object.")
            valid = False
            continue

        # Check for missing fields
        for field in required_fields:
            if field not in employee:
                print(f"Error: Missing field '{field}'.")
                valid = False

        # Skip further checks if required fields are missing
        if any(field not in employee for field in required_fields):
            continue

        # Validate employee ID
        if (
            not isinstance(employee["id"], int)
            or isinstance(employee["id"], bool)
            or employee["id"] <= 0
        ):
            print("Error: 'id' must be a positive integer.")
            valid = False

        # Validate text fields
        for field in ["name", "department", "role", "email"]:
            value = employee[field]

            if not isinstance(value, str):
                print(f"Error: '{field}' must be text.")
                valid = False
            elif not value.strip():
                print(f"Error: '{field}' cannot be empty.")
                valid = False

        # Validate email format
        email = employee["email"]

        if isinstance(email, str) and email.strip():
            pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

            if not re.match(pattern, email):
                print(f"Error: Invalid email address '{email}'.")
                valid = False

    return valid


# Validate task records
def validate_tasks(data):
    if not isinstance(data, dict):
        print("Error: The main JSON data must be an object.")
        return False

    if "tasks" not in data:
        print("Error: Missing required section 'tasks'.")
        return False

    if not isinstance(data["tasks"], list):
        print("Error: 'tasks' must contain a list.")
        return False

    required_fields = [
        "taskId",
        "title",
        "assignee",
        "status",
        "priority"
    ]

    valid_statuses = ["Pending", "In Progress", "Completed"]
    valid_priorities = ["Low", "Medium", "High"]

    valid = True

    for index, task in enumerate(data["tasks"], start=1):
        print(f"\nChecking task record {index}:")

        if not isinstance(task, dict):
            print("Error: Task record must be a JSON object.")
            valid = False
            continue

        # Check for missing fields
        for field in required_fields:
            if field not in task:
                print(f"Error: Missing field '{field}'.")
                valid = False

        if any(field not in task for field in required_fields):
            continue

        # Validate task ID
        if (
            not isinstance(task["taskId"], int)
            or isinstance(task["taskId"], bool)
            or task["taskId"] <= 0
        ):
            print("Error: 'taskId' must be a positive integer.")
            valid = False

        # Validate text fields
        for field in ["title", "assignee", "status", "priority"]:
            value = task[field]

            if not isinstance(value, str):
                print(f"Error: '{field}' must be text.")
                valid = False
            elif not value.strip():
                print(f"Error: '{field}' cannot be empty.")
                valid = False

        # Validate status
        if (
            isinstance(task["status"], str)
            and task["status"] not in valid_statuses
        ):
            print(
                f"Error: Invalid status '{task['status']}'. "
                f"Allowed values: {valid_statuses}"
            )
            valid = False

        # Validate priority
        if (
            isinstance(task["priority"], str)
            and task["priority"] not in valid_priorities
        ):
            print(
                f"Error: Invalid priority '{task['priority']}'. "
                f"Allowed values: {valid_priorities}"
            )
            valid = False

    return valid


# Main program
def main():
    data = load_json("employees.json")

    if data is None:
        return

    print("\n========== EMPLOYEE VALIDATION ==========")
    employees_valid = validate_employees(data)

    print("\n========== TASK VALIDATION ==========")
    tasks_valid = validate_tasks(data)

    print("\n========== VALIDATION SUMMARY ==========")

    if employees_valid and tasks_valid:
        print("Success: All employee and task records are valid.")
    else:
        print("Failed: Please fix the errors listed above.")


if __name__ == "__main__":
    main()