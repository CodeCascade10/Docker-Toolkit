
# Basic Python Application for Docker

print("================================")
print("       Hello from Docker!       ")
print("================================")

print("My first Docker application")
print("Running inside a Docker container")

# Application environment
import os

app_env = os.getenv("APP_ENV", "development")

print(f"Application Environment: {app_env}")
print("Docker container is running successfully!")
