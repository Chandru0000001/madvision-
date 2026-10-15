# FastAPI Task Management API

## 1. Project Overview

This project is a simple Task Management REST API developed using Python and FastAPI.

It allows users to retrieve tasks, create new tasks, retrieve individual tasks, and validate incoming data.

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
└── README.md
```

## 4. Requirements

Install Python and Visual Studio Code.

The project uses a Python virtual environment to manage its dependencies.

## 5. Installation and Setup

### Step 1: Open the project directory

Open the VS Code terminal and run:

```powershell
cd "C:\Users\chand\OneDrive\Desktop\madvision project\fastapi_project"
```

### Step 2: Create a virtual environment (if needed)

If you have not created a virtual environment for this project, run:

```powershell
python -m venv venv
```

If the virtual environment already exists, skip this command.

### Step 3: Activate the virtual environment

On Windows PowerShell, run:

```powershell
.\venv\Scripts\Activate.ps1
```

If the environment is already active, skip this command.

### Step 4: Install dependencies

Run:

```powershell
python -m pip install "fastapi[standard]"
```

## 6. Run the API

Start the development server using:

```powershell
fastapi dev main.py
```

The API will usually be available at:

http://127.0.0.1:8000

Keep the terminal running while testing the API.

## 7. API Endpoints

| HTTP Method | Endpoint      | Description           |
| ----------- | ------------- | --------------------- |
| GET         | `/tasks`      | Retrieve all tasks    |
| POST        | `/tasks`      | Create a new task     |
| GET         | `/tasks/{id}` | Retrieve a task by ID |

## 8. Test the API

FastAPI automatically generates interactive API documentation.

Open the following address in your browser:

http://127.0.0.1:8000/docs

### Test 1: Retrieve all tasks

Endpoint:

```http
GET /tasks
```

Steps:

1. Open Swagger UI.
2. Expand `GET /tasks`.
3. Click **Try it out**.
4. Click **Execute**.

Expected result: `200 OK`.

### Test 2: Create a task

Endpoint:

```http
POST /tasks
```

Example request body:

```json
{
  "id": 3,
  "title": "Practice FastAPI",
  "completed": false
}
```

Steps:

1. Expand `POST /tasks`.
2. Click **Try it out**.
3. Enter the JSON request body.
4. Click **Execute**.

Expected result: `201 Created`.

### Test 3: Retrieve one task

Endpoint:

```http
GET /tasks/1
```

Steps:

1. Expand `GET /tasks/{id}`.
2. Click **Try it out**.
3. Enter `1` as the ID.
4. Click **Execute**.

Expected result: `200 OK` if task ID 1 exists.

## 9. Error Handling and Validation

The API validates incoming task data using Pydantic.

The task model applies these rules:

* Task ID must be an integer greater than zero.
* Task title must contain between 3 and 100 characters.
* The completion status must be Boolean.
* The completion status defaults to `false` if omitted.

The API also checks for duplicate task IDs.

### Supported error responses

| Status Code | Description            |
| ----------- | ---------------------- |
| 404         | Task not found         |
| 409         | Task ID already exists |
| 422         | Invalid request data   |

### Example: Task not found

Request:

```http
GET /tasks/100
```

Example response:

```json
{
  "detail": "Task with ID 100 was not found"
}
```

### Example: Duplicate task ID

If you try to create a task using an existing ID, the API returns:

```json
{
  "detail": "Task with ID 1 already exists"
}
```

The status code is `409 Conflict`.

### Example: Invalid title

Request:

```json
{
  "id": 3,
  "title": "Hi",
  "completed": false
}
```

The API returns `422 Unprocessable Entity` because the title is shorter than three characters.

## 10. Important Notes

* Tasks are currently stored in an in-memory Python list.
* Task data is not permanently stored in a database.
* Tasks reset to their initial values when the application restarts.
* Task IDs must be unique.
* The development server should remain running during testing.

## 11. Future Improvements

Possible improvements include:

* Add a PUT endpoint to update tasks.
* Add a DELETE endpoint to remove tasks.
* Store tasks in a database such as SQLite or PostgreSQL.
* Add automated tests using pytest.
* Add authentication and authorization.

## 12. Conclusion

This project demonstrates the basics of building a REST API using FastAPI, defining data models with Pydantic, handling errors, and testing endpoints using Swagger UI.
