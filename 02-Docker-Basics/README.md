
# 02 - Docker Basics

Welcome to the **Docker Basics** section of Docker Toolkit!

This section covers the fundamental concepts of Docker, including its architecture, images, containers, Docker Engine, and Docker Registry.

The goal is to understand how Docker works internally and how to manage containerized applications.

---

## 📚 Table of Contents

| No. | Topic | Description |
|---|---|---|
| 01 | [Docker Architecture](./docker-architecture.md) | Understand Docker's client-server architecture and its components. |
| 02 | [Docker Images](./images.md) | Learn how Docker images are created, stored, and managed. |
| 03 | [Docker Containers](./containers.md) | Understand container lifecycle and container management. |
| 04 | [Docker Engine](./docker-engine.md) | Explore Docker Daemon, Docker CLI, containerd, and runc. |
| 05 | [Docker Registry](./docker-registry.md) | Learn how to push, pull, and manage Docker images. |

---

## 🎯 Learning Objectives

After completing this section, you should be able to:

- Understand Docker architecture.
- Explain how Docker Engine works.
- Differentiate between Docker images and containers.
- Understand Docker image layers.
- Create and manage Docker containers.
- Work with Docker Hub and private registries.
- Push and pull Docker images.
- Understand the container execution process.

---

## 🛠️ Essential Docker Commands

### Check Docker Installation

```bash
docker --version
docker version
docker info
```

### Image Management

```bash
docker pull nginx
docker images
docker build -t myapp .
docker rmi nginx
```

### Container Management

```bash
docker run -d -p 8080:80 nginx
docker ps
docker ps -a
docker stop <container_id>
docker start <container_id>
docker rm <container_id>
```

### Registry Management

```bash
docker login
docker tag myapp username/myapp:v1
docker push username/myapp:v1
docker pull username/myapp:v1
```

---

## 🏗️ Docker Workflow

```text
       Developer
           |
           v
       Docker CLI
           |
           v
      Docker Engine
           |
           v
       Docker Image
           |
           v
      Docker Container
           |
           v
    Running Application
```

---

## 💡 Important Concepts

| Concept | Meaning |
|---|---|
| Docker Image | Blueprint used to create containers |
| Docker Container | Isolated running instance of an image |
| Docker Engine | Core technology responsible for managing containers |
| Docker Daemon | Background service that manages Docker objects |
| Docker Registry | Platform for storing and distributing images |
| Docker Repository | Collection of related image versions |
| Docker Tag | Identifies a particular image version |
| containerd | Container runtime responsible for lifecycle management |
| runc | Low-level runtime that creates and runs containers |

---

## 🎓 Interview Preparation

Important questions to practice:

1. What is Docker and why is it used?
2. Explain Docker architecture.
3. What is the difference between Docker Image and Container?
4. What are Docker image layers?
5. What is Docker Engine?
6. What is the difference between Docker Daemon and Docker CLI?
7. What are containerd and runc?
8. What is Docker Hub?
9. What is the difference between Docker Registry and Repository?
10. How do you push an image to Docker Hub?
11. What happens internally when you execute `docker run nginx`?
12. How are Docker containers different from virtual machines?

---

## 🚀 Practical Tasks

- [ ] Install Docker Engine.
- [ ] Verify Docker installation.
- [ ] Pull the Nginx image.
- [ ] List available Docker images.
- [ ] Run an Nginx container.
- [ ] Access Nginx through a browser.
- [ ] Inspect a running container.
- [ ] Stop and remove a container.
- [ ] Build a custom Docker image.
- [ ] Push your image to Docker Hub.
- [ ] Pull your custom image and run it again.

---

## 📖 Recommended Learning Order

1. Docker Architecture
2. Docker Images
3. Docker Containers
4. Docker Engine
5. Docker Registry

---

## 🔗 Useful Resources

- [Official Docker Documentation](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Get Started Guide](https://docs.docker.com/get-started/)
- [Docker Engine Documentation](https://docs.docker.com/engine/)

---

**Previous:** [01 - Prerequisites](../01-Prerequisites/README.md)

**Next:** 03 - Dockerfile and Image Building

---

⭐ If you find this repository helpful, consider giving it a star!
