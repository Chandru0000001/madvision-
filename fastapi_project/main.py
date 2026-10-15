from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Task Management API",
    description="A simple REST API built using FastAPI",
    version="1.0.0"
)


# Task Model and Data Validation

class Task(BaseModel):
    id: int = Field(gt=0, description="ID must be greater than zero")

    title: str = Field(
        min_length=3,
        max_length=100,
        description="Title must contain 3 to 100 characters"
    )

    completed: bool = False


# Sample Task Data

tasks = [
    {
        "id": 1,
        "title": "Learn Python",
        "completed": False
    },
    {
        "id": 2,
        "title": "Learn FastAPI",
        "completed": False
    }
]



# Custom Validation Error Handler

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    errors = []

    for error in exc.errors():
        field = ".".join(str(part) for part in error["loc"])

        errors.append({
            "field": field,
            "message": error["msg"]
        })

    return JSONResponse(
        status_code=422,
        content={
            "error": "Validation failed",
            "details": errors
        }
    )



# GET: Retrieve All Tasks

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": tasks
    }



# POST: Create a New Task

@app.post("/tasks", status_code=201)
def create_task(task: Task):

    # Check for duplicate task IDs
    for existing_task in tasks:
        if existing_task["id"] == task.id:
            raise HTTPException(
                status_code=409,
                detail=f"Task with ID {task.id} already exists"
            )

    # Add the new task
    new_task = task.model_dump()
    tasks.append(new_task)

    return {
        "message": "Task created successfully",
        "task": new_task
    }



# GET: Retrieve One Task by ID

@app.get("/tasks/{id}")
def get_task(id: int):

    # Validate the task ID
    if id <= 0:
        raise HTTPException(
            status_code=422,
            detail="Task ID must be greater than zero"
        )

    # Search for the requested task
    for task in tasks:
        if task["id"] == id:
            return task

    # Return an error if the task doesn't exist
    raise HTTPException(
        status_code=404,
        detail=f"Task with ID {id} was not found"
    )