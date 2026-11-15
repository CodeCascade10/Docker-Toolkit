
from fastapi import FastAPI

app = FastAPI(
    title="Python Docker Application",
    description="A simple FastAPI application running inside Docker",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Hello from Python Docker!",
        "status": "Running successfully",
        "technology": "FastAPI + Docker"
    }


@app.get("/about")
def about():
    return {
        "application": "Python Docker Demo",
        "version": "1.0.0",
        "environment": "Docker Container"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/users")
def get_users():
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"},
        {"id": 3, "name": "Charlie"}
    ]

    return {
        "users": users
    }
