
# Docker Architecture

## 1. Introduction

Docker is a containerization platform that allows developers to package applications and their dependencies into lightweight, portable containers.

Docker uses a client-server architecture to build, run, and manage containers.

## 2. Docker Architecture Diagram

```text
             Docker Client
          (CLI / Docker Desktop)
                   |
                   | Docker API
                   v
             Docker Daemon
                (dockerd)
                   |
          +--------+--------+
          |        |        |
          v        v        v
       Images   Containers Networks
          |
          v
      Docker Registry
     (Docker Hub / ECR)
```

## 3. Main Components

### Docker Client

- Provides the command-line interface.
- Sends commands to the Docker Daemon.
- Communicates through the Docker REST API.

Example:

```bash
docker run nginx
docker build -t myapp .
docker ps
```

### Docker Daemon

- Runs in the background.
- Manages Docker objects.
- Builds images.
- Creates and manages containers.
- Handles Docker networks and volumes.

### Docker Images

- Read-only templates used to create containers.
- Contain application code and dependencies.
- Can be stored in Docker registries.

Example:

```bash
docker pull nginx
docker images
```

### Docker Containers

- Running instances of Docker images.
- Provide isolated application environments.
- Can be started, stopped, and removed.

Example:

```bash
docker run -d -p 8080:80 nginx
docker ps
docker stop <container_id>
```

### Docker Registry

- Stores and distributes Docker images.
- Docker Hub is a popular public registry.
- Private registries include AWS ECR and GitHub Container Registry.

Example:

```bash
docker login
docker push username/myapp:latest
docker pull nginx
```

## 4. How Docker Works

1. Developer enters a Docker command.
2. Docker Client sends the request to Docker Daemon.
3. Docker Daemon processes the request.
4. If required, the daemon pulls an image from a registry.
5. Docker creates a container from the image.
6. The application runs inside the container.

## 5. Important Docker Commands

| Command | Description |
|---|---|
| docker version | Displays Docker version |
| docker info | Shows Docker system information |
| docker images | Lists available images |
| docker ps | Lists running containers |
| docker ps -a | Lists all containers |
| docker pull nginx | Downloads an image |
| docker build -t app . | Builds an image |
| docker run nginx | Runs a container |
| docker stop ID | Stops a container |
| docker rm ID | Removes a container |
| docker rmi IMAGE | Removes an image |

## 6. Docker Architecture Advantages

- Portability across environments.
- Lightweight compared to virtual machines.
- Faster application deployment.
- Application isolation.
- Efficient resource utilization.
- Easy scalability.
- Consistent development and production environments.

## 7. Docker vs Virtual Machines

| Feature | Docker | Virtual Machine |
|---|---|---|
| Architecture | Container-based | Hypervisor-based |
| OS | Shares host kernel | Separate guest OS |
| Startup | Fast | Relatively slow |
| Resource Usage | Low | Higher |
| Portability | High | Depends on VM setup |
| Isolation | Process-level | Hardware-level virtualization |

## 8. Conclusion

Docker simplifies application development, deployment, and management through containerization.

Its client-server architecture makes it possible to build, distribute, and run applications consistently across different environments.
