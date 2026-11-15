
# Python Dockerfile

## 1. Introduction

Docker allows us to containerize Python applications by packaging the Python runtime, application code, libraries, and dependencies into a Docker image.

This makes Python applications portable and consistent across development, testing, and production environments.

In this section, we will learn how to:

- Create a Python Dockerfile.
- Install Python dependencies.
- Build Docker images.
- Run Python applications inside containers.
- Expose application ports.
- Use environment variables.
- Optimize Python Docker images.

---

## 2. Project Structure

```text
python-dockerfile/
│
├── Dockerfile
├── app.py
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## 3. Create a Python Application

Create `app.py`.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello from Python Docker!",
        "status": "Running successfully"
    }

@app.get("/about")
def about():
    return {
        "application": "Python Docker Demo",
        "version": "1.0"
    }
```

---

## 4. Create requirements.txt

```text
fastapi
uvicorn[standard]
```

This file contains the Python dependencies required by the application.

---

## 5. Create Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile Explanation

| Instruction | Purpose |
|---|---|
| FROM | Uses Python base image |
| WORKDIR | Sets application directory |
| COPY | Copies application files |
| RUN | Installs Python dependencies |
| EXPOSE | Documents application port |
| CMD | Starts FastAPI application |

---

## 6. Create .dockerignore

```text
.git
.gitignore
.venv/
venv/
__pycache__/
*.pyc
.env
.vscode/
.idea/
.pytest_cache/
```

This prevents unnecessary files from entering the Docker build context.

---

## 7. Build Docker Image

```bash
docker build -t python-fastapi-app .
```

Verify the image:

```bash
docker images
```

---

## 8. Run Docker Container

```bash
docker run -d \
  --name python-container \
  -p 8000:8000 \
  python-fastapi-app
```

Check running containers:

```bash
docker ps
```

---

## 9. Test the Application

Open your browser:

```text
http://localhost:8000
```

FastAPI documentation:

```text
http://localhost:8000/docs
```

Test using curl:

```bash
curl http://localhost:8000
```

Expected response:

```json
{
    "message": "Hello from Python Docker!",
    "status": "Running successfully"
}
```

---

## 10. Useful Docker Commands

### View Container Logs

```bash
docker logs python-container
```

### Enter Container

```bash
docker exec -it python-container sh
```

### Stop Container

```bash
docker stop python-container
```

### Remove Container

```bash
docker rm python-container
```

### Remove Image

```bash
docker rmi python-fastapi-app
```

---

## 11. Docker Image Optimization

Best practices:

1. Use lightweight Python base images.
2. Use `python:3.12-slim` where appropriate.
3. Install dependencies before copying frequently changing application files.
4. Use `--no-cache-dir` with pip.
5. Create a `.dockerignore` file.
6. Avoid installing unnecessary packages.
7. Use multi-stage builds when beneficial.
8. Run applications as a non-root user.
9. Avoid storing secrets inside Docker images.
10. Pin dependency versions for reproducible builds.

---

## 12. Practical Tasks

- [ ] Create a Python application.
- [ ] Create requirements.txt.
- [ ] Write a Dockerfile.
- [ ] Create .dockerignore.
- [ ] Build a Docker image.
- [ ] Run the Python container.
- [ ] Access the application through localhost.
- [ ] Test FastAPI documentation.
- [ ] Check container logs.
- [ ] Stop and remove the container.

---

## 13. Interview Questions

1. How do you containerize a Python application?
2. Why do we use requirements.txt?
3. What is the purpose of python:3.12-slim?
4. Why should dependencies be copied before application code?
5. What is the purpose of EXPOSE?
6. Why does FastAPI need 0.0.0.0 inside Docker?
7. What is the purpose of .dockerignore?
8. How do you reduce Python Docker image size?
9. How do you debug a Python container?
10. How do you run FastAPI inside Docker?

---

## 14. Conclusion

Docker simplifies Python application deployment by packaging the application and its dependencies into portable containers.

Understanding Python Dockerfiles is useful for backend development, microservices, cloud deployment, and DevOps workflows.
```

**Next file:** `04-Dockerfile/python-dockerfile/Dockerfile`

Say **Next** when ready. 🚀