import os

from dotenv import load_dotenv
from fastapi import FastAPI

# Load values from the .env file
load_dotenv()

# Read environment variables
APP_NAME = os.getenv("APP_NAME", "My FastAPI App")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# Create the FastAPI application
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    debug=DEBUG
)


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "app_name": APP_NAME,
        "version": APP_VERSION,
        "debug": DEBUG
    }


@app.get("/students")
def get_students():
    return [
        {"id": 1, "name": "Chandra", "course": "Python"},
        {"id": 2, "name": "Ravi", "course": "FastAPI"}
    ]
