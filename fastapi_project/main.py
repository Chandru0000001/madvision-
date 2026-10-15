from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()


# Task validation model
class Task(BaseModel):
    id: int = Field(gt=0, description="Task ID must be greater than zero")
    title: str = Field(
        min_length=3,
        max_length=100,
        description="Title must contain 3 to 100 characters"
    )
    completed: bool = False


# Sample task data
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


# Custom validation error handler
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


# GET: List all tasks
@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}


# POST: Create a new task
@app.post("/tasks", status_code=201)
def create_task(task: Task):

    # Check for duplicate IDs
    for existing_task in tasks:
        if existing_task["id"] == task.id:
            raise HTTPException(
                status_code=409,
                detail=f"Task with ID {task.id} already exists"
            )

    tasks.append(task.model_dump())

    return {
        "message": "Task created successfully",
        "task": task.model_dump()
    }


# GET: Retrieve one task
@app.get("/tasks/{id}")
def get_task(id: int):

    if id <= 0:
        raise HTTPException(
            status_code=422,
            detail="Task ID must be greater than zero"
        )

    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task with ID {id} was not found"
    )