import json
from pathlib import Path


# Load JSON data
def load_json():
    file_path = Path(__file__).parent / "employees.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: employees.json file not found.")
        return None

    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return None


# Display employee records
def display_employees(employees):
    if not employees:
        print("No employees found.")
        return

    print("\n========== EMPLOYEE RESULTS ==========")

    for employee in employees:
        print(f"ID: {employee['id']}")
        print(f"Name: {employee['name']}")
        print(f"Department: {employee['department']}")
        print(f"Role: {employee['role']}")
        print(f"Email: {employee['email']}")
        print("-" * 35)


# Search employees by name
def search_employee_by_name(employees, name):
    results = [
        employee for employee in employees
        if name.lower() in employee["name"].lower()
    ]

    display_employees(results)


# Filter employees by department
def filter_employee_by_department(employees, department):
    results = [
        employee for employee in employees
        if employee["department"].lower() == department.lower()
    ]

    display_employees(results)


# Filter employees by role
def filter_employee_by_role(employees, role):
    results = [
        employee for employee in employees
        if role.lower() in employee["role"].lower()
    ]

    display_employees(results)


# Search tasks by title
def search_task_by_title(tasks, title):
    results = [
        task for task in tasks
        if title.lower() in task["title"].lower()
    ]

    display_tasks(results)


# Filter tasks by status
def filter_tasks_by_status(tasks, status):
    results = [
        task for task in tasks
        if task["status"].lower() == status.lower()
    ]

    display_tasks(results)


# Filter tasks by priority
def filter_tasks_by_priority(tasks, priority):
    results = [
        task for task in tasks
        if task["priority"].lower() == priority.lower()
    ]

    display_tasks(results)


# Display task records
def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\n========== TASK RESULTS ==========")

    for task in tasks:
        print(f"Task ID: {task['taskId']}")
        print(f"Title: {task['title']}")
        print(f"Assignee: {task['assignee']}")
        print(f"Status: {task['status']}")
        print(f"Priority: {task['priority']}")
        print("-" * 35)


# Main program
def main():
    data = load_json()

    if data is None:
        return

    employees = data.get("employees", [])
    tasks = data.get("tasks", [])

    while True:
        print("\n========== SEARCH AND FILTER MENU ==========")
        print("1. Search employee by name")
        print("2. Filter employees by department")
        print("3. Filter employees by role")
        print("4. Search tasks by title")
        print("5. Filter tasks by status")
        print("6. Filter tasks by priority")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            name = input("Enter employee name: ").strip()
            search_employee_by_name(employees, name)

        elif choice == "2":
            department = input("Enter department: ").strip()
            filter_employee_by_department(employees, department)

        elif choice == "3":
            role = input("Enter employee role: ").strip()
            filter_employee_by_role(employees, role)

        elif choice == "4":
            title = input("Enter task title: ").strip()
            search_task_by_title(tasks, title)

        elif choice == "5":
            status = input(
                "Enter status (Pending, In Progress, Completed): "
            ).strip()
            filter_tasks_by_status(tasks, status)

        elif choice == "6":
            priority = input("Enter priority (Low, Medium, High): ").strip()
            filter_tasks_by_priority(tasks, priority)

        elif choice == "7":
            print("Thank you! Program closed.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()