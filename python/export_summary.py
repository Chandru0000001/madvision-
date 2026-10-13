import json
from pathlib import Path
from collections import Counter


# Function to load JSON data
def load_json(filename):
    file_path = Path(__file__).parent / filename

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
    except json.JSONDecodeError as error:
        print(f"Error: Invalid JSON format: {error}")

    return None


# Function to generate employee and task summary
def generate_summary(data):
    employees = data.get("employees", [])
    tasks = data.get("tasks", [])

    # Count employees by department
    department_counts = Counter(
        employee["department"] for employee in employees
    )

    # Count tasks by status
    status_counts = Counter(
        task["status"] for task in tasks
    )

    # Count tasks by priority
    priority_counts = Counter(
        task["priority"] for task in tasks
    )

    # Count tasks assigned to each employee
    assignee_counts = Counter(
        task["assignee"] for task in tasks
    )

    # Create summary dictionary
    summary = {
        "employees": {
            "total_employees": len(employees),
            "employees_by_department": dict(department_counts)
        },
        "tasks": {
            "total_tasks": len(tasks),
            "tasks_by_status": dict(status_counts),
            "tasks_by_priority": dict(priority_counts),
            "tasks_by_assignee": dict(assignee_counts)
        }
    }

    return summary


# Function to export summary to a JSON file
def export_summary(summary, filename):
    file_path = Path(__file__).parent / filename

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(summary, file, indent=4)

        print(f"Summary exported successfully to {filename}")

    except OSError as error:
        print(f"Error saving summary: {error}")


# Main program
def main():
    data = load_json("employees.json")

    if data is None:
        return

    summary = generate_summary(data)

    export_summary(summary, "summary.json")

    print("\n========== SUMMARY REPORT ==========")
    print(json.dumps(summary, indent=4))


if __name__ == "__main__":
    main()