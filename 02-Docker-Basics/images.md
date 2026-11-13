
# Docker Images

## 1. Introduction

A Docker Image is a lightweight, standalone, executable package that contains everything required to run an application.

It includes:
- Application source code
- Runtime environment
- System libraries
- Dependencies
- Configuration files

Docker images are used to create Docker containers.

## 2. Docker Image Architecture

```text
          Docker Registry
             (Docker Hub)
                  |
                  | docker pull
                  v
             Docker Image
                  |
                  | docker run
                  v
             Container
                  |
                  v
           Running Application
```

## 3. Docker Image Layers

Docker images are built using multiple read-only layers.

Each instruction in a Dockerfile can create a new image layer.

Example Dockerfile:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Image layer structure:

```text
        Docker Image
             |
      +--------------+
      | Application  |  COPY . .
      +--------------+
      | Dependencies |  RUN pip install
      +--------------+
      | Requirements |  COPY requirements.txt
      +--------------+
      | Base Image   |  FROM python:3.12-slim
      +--------------+
```

## 4. Important Docker Image Commands

### Download an Image

```bash
docker pull nginx
```

### List Images

```bash
docker images
```

### Build an Image

```bash
docker build -t myapp:latest .
```

### Inspect an Image

```bash
docker inspect nginx
```

### Remove an Image

```bash
docker rmi nginx
```

### Tag an Image

```bash
docker tag myapp:latest username/myapp:v1
```

### Push an Image to Docker Hub

```bash
docker login

docker push username/myapp:v1
```

### View Image History

```bash
docker history nginx
```

## 5. Docker Image vs Container

| Docker Image | Docker Container |
|---|---|
| Blueprint/template | Running instance |
| Read-only layers | Writable container layer |
| Used to create containers | Runs applications |
| Can create multiple containers | Created from an image |

## 6. Docker Image Naming Convention

```text
registry/username/repository:tag
```

Example:

```text
docker.io/knaskar10/myapp:v1
```

Components:
- Registry: docker.io
- Username: knaskar10
- Repository: myapp
- Tag: v1

## 7. Docker Image Optimization

Best practices:

1. Use lightweight base images.
2. Use multi-stage builds.
3. Avoid unnecessary dependencies.
4. Use `.dockerignore`.
5. Combine related RUN commands where appropriate.
6. Use specific image tags instead of `latest`.
7. Keep images small and secure.

## 8. Docker Image vs Virtual Machine Image

| Feature | Docker Image | VM Image |
|---|---|---|
| Size | Usually smaller | Usually larger |
| OS | Shares host kernel | Includes guest OS |
| Startup | Fast | Slower |
| Execution | Container | Virtual machine |

## 9. Conclusion

Docker images provide a consistent and portable way to package applications.

They are the foundation of containerization and make application deployment easier across development, testing, and production environments.
