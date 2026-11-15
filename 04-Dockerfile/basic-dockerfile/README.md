
# Basic Dockerfile

## 1. Introduction

A Dockerfile is a text file containing a set of instructions used to build a Docker image.

It automates the process of packaging an application and its dependencies into a Docker image.

Dockerfiles help developers create consistent and reproducible application environments.

---

## 2. Dockerfile Structure

A basic Dockerfile looks like this:

```dockerfile
FROM ubuntu:latest

WORKDIR /app

COPY . .

RUN apt-get update

CMD ["echo", "Hello Docker"]
```

### Explanation

| Instruction | Description |
|---|---|
| FROM | Specifies the base image. |
| WORKDIR | Sets the working directory. |
| COPY | Copies files into the image. |
| RUN | Executes commands during image building. |
| CMD | Specifies the default command when the container starts. |

---

## 3. Important Dockerfile Instructions

### FROM

Defines the base image.

```dockerfile
FROM ubuntu:24.04
```

### WORKDIR

Sets the working directory inside the container.

```dockerfile
WORKDIR /app
```

### COPY

Copies files from the build context into the image.

```dockerfile
COPY app.py /app/
```

### ADD

Copies files and supports additional features such as local archive extraction.

```dockerfile
ADD files.tar.gz /app/
```

### RUN

Executes commands during image building.

```dockerfile
RUN apt-get update && apt-get install -y curl
```

### CMD

Specifies the default command or arguments when a container starts.

```dockerfile
CMD ["python", "app.py"]
```

### ENTRYPOINT

Defines the executable that runs when the container starts.

```dockerfile
ENTRYPOINT ["python"]
```

### EXPOSE

Documents the port on which the application listens.

```dockerfile
EXPOSE 8000
```

### ENV

Sets environment variables.

```dockerfile
ENV APP_ENV=production
```

### ARG

Defines build-time variables.

```dockerfile
ARG APP_VERSION=1.0
```

### USER

Sets the user for subsequent instructions and runtime.

```dockerfile
USER appuser
```

---

## 4. Create Your First Dockerfile

### Step 1: Create a Project Directory

```bash
mkdir basic-dockerfile
cd basic-dockerfile
```

### Step 2: Create an Application

Create a file named `app.py`.

```python
print("Hello from Docker!")
print("My first Docker application")
```

### Step 3: Create a Dockerfile

Create a file named `Dockerfile`.

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "app.py"]
```

### Step 4: Build the Docker Image

```bash
docker build -t my-first-docker-app .
```

### Step 5: Verify the Image

```bash
docker images
```

### Step 6: Run the Container

```bash
docker run --name first-container my-first-docker-app
```

Expected Output:

```text
Hello from Docker!
My first Docker application
```

---

## 5. Understanding RUN vs CMD vs ENTRYPOINT

| Feature | RUN | CMD | ENTRYPOINT |
|---|---|---|---|
| Execution | During image build | When container starts | When container starts |
| Purpose | Install dependencies and configure image | Default command or arguments | Main executable |
| Multiple Instructions | Multiple allowed | Last CMD takes effect | Multiple instructions are possible, but only the last takes effect |
| Override | Build-time instruction | Easily overridden at runtime | Can be overridden using --entrypoint |

Example:

```dockerfile
FROM ubuntu:24.04

RUN apt-get update

CMD ["echo", "Hello from CMD"]

ENTRYPOINT ["echo", "Hello from ENTRYPOINT"]
```

Note: When both CMD and ENTRYPOINT are present in this example, CMD supplies default arguments to ENTRYPOINT.

---

## 6. Understanding COPY vs ADD

| COPY | ADD |
|---|---|
| Copies files and directories | Copies files and directories |
| Simple and predictable | Supports additional features |
| Does not automatically extract archives | Automatically extracts supported local tar archives |
| Preferred for normal file copying | Use when its additional features are required |

Examples:

```dockerfile
COPY app.py /app/
```

```dockerfile
ADD application.tar.gz /app/
```

Best practice: Prefer COPY unless ADD provides a specific feature you need.

---

## 7. Docker Build Context

Docker build context is the set of files and directories made available to the Docker build process.

Example:

```bash
docker build -t myapp .
```

Here, `.` represents the current directory as the build context.

Example project structure:

```text
myapp/
│
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md
```

---

## 8. Using .dockerignore

The `.dockerignore` file excludes unnecessary files from the build context.

Example `.dockerignore`:

```text
.git
.gitignore
.venv/
__pycache__/
*.pyc
.env
node_modules/
```

Benefits:

- Reduces build context size.
- Improves build performance.
- Prevents unnecessary files from entering the build context.
- Helps avoid accidentally including sensitive files.

---

## 9. Useful Dockerfile Commands

### Build an Image

```bash
docker build -t myapp .
```

### Build Without Cache

```bash
docker build --no-cache -t myapp .
```

### Build Using a Different Dockerfile

```bash
docker build -f Dockerfile.dev -t myapp:dev .
```

### Run a Container

```bash
docker run myapp
```

### Run with Port Mapping

```bash
docker run -d -p 8080:80 myapp
```

### Inspect Image History

```bash
docker history myapp
```

---

## 10. Dockerfile Best Practices

1. Use trusted and lightweight base images.
2. Specify meaningful image tags.
3. Use WORKDIR instead of repeatedly changing directories.
4. Prefer COPY over ADD for ordinary file copying.
5. Combine related RUN commands where appropriate.
6. Use .dockerignore.
7. Avoid storing secrets in Dockerfiles.
8. Use non-root users where possible.
9. Use multi-stage builds for compiled applications.
10. Keep the image size as small as practical.

---

## 11. Practical Tasks

- [ ] Create your first Dockerfile.
- [ ] Build a custom Docker image.
- [ ] Run a container from that image.
- [ ] Experiment with FROM and WORKDIR.
- [ ] Understand RUN, CMD, and ENTRYPOINT.
- [ ] Experiment with COPY and ADD.
- [ ] Create a .dockerignore file.
- [ ] Inspect image layers using docker history.
- [ ] Build an image without cache.

---

## 12. Interview Questions

1. What is a Dockerfile?
2. What is the purpose of FROM?
3. What is the difference between RUN and CMD?
4. What is the difference between CMD and ENTRYPOINT?
5. What is the difference between COPY and ADD?
6. What is Docker build context?
7. What is the purpose of WORKDIR?
8. What is .dockerignore?
9. What is the difference between ARG and ENV?
10. How do you reduce Docker image size?

---

## 13. Conclusion

Dockerfiles automate the process of building Docker images.

Understanding Dockerfile instructions is essential for containerizing applications and creating efficient, reproducible deployment environments.
```

**Next file:** `basic-dockerfile/Dockerfile`

Say **Next** and we'll build the actual Dockerfile example, one file at a time.