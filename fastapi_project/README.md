# FastAPI Task Management API

## 1. Project Overview

This project is a simple Task Management REST API developed using Python and FastAPI.

The API supports retrieving tasks, creating new tasks, retrieving an individual task, validating incoming data, and returning useful error messages.

## 2. Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* REST API
* Swagger UI

## 3. Project Structure

```text
fastapi_project/
├── venv/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 4. Installation

Open the project folder in VS Code and open the terminal.

Navigate to the project directory:

```powershell
cd "C:\Users\chand\OneDrive\Desktop\madvision project\fastapi_project"
```

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

If the virtual environment is already active, skip this command.

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## 5. Run the Application

Run:

```powershell
fastapi dev main.py
```

The API will usually run at:

http://127.0.0.1:8000

## 6. Interactive API Documentation

Open the following address in your browser:

http://127.0.0.1:8000/docs

Use Swagger UI to execute requests and inspect responses.

## 7. API Endpoints

| Method | Endpoint    | Description           |
| ------ | ----------- | --------------------- |
| GET    | /tasks      | Retrieve all tasks    |
| POST   | /tasks      | Create a new task     |
| GET    | /tasks/{id} | Retrieve a task by ID |

## 8. Create a Task

Endpoint:

POST /tasks

Example request:

```json
{
  "id": 3,
  "title": "Practice FastAPI",
  "completed": false
}
```

Expected status code: 201 Created.

## 9. Retrieve All Tasks

Endpoint:

GET /tasks

Expected status code: 200 OK.

## 10. Retrieve One Task

Endpoint:

GET /tasks/1

Expected status code: 200 OK if the task exists.

If the task does not exist, the API returns 404 Not Found.

## 11. Validation Rules

* Task ID must be an integer greater than zero.
* Task title must contain between 3 and 100 characters.
* Completion status must be Boolean.
* Completion status defaults to false.
* Duplicate task IDs are not allowed.

## 12. Error Handling

| Status Code | Meaning              |
| ----------- | -------------------- |
| 200         | Request successful   |
| 201         | Task created         |
| 404         | Task not found       |
| 409         | Duplicate task ID    |
| 422         | Invalid request data |

## 13. Limitations

Tasks are currently stored in a Python list.

The data is not saved permanently and resets when the application restarts.

A database can be added in a future version.

## 14. Future Improvements

* Update tasks using PUT.
* Delete tasks using DELETE.
* Store tasks in a database.
* Add automated tests using pytest.
* Add user authentication.

## 15. Conclusion

This project demonstrates REST API development, request validation, error handling, and interactive API testing using FastAPI.
