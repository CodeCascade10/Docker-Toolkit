
# Docker Engine

## 1. Introduction

Docker Engine is an open-source containerization technology used to build and run containers.

It provides the core functionality required to create, manage, and execute Docker containers.

Docker Engine follows a client-server architecture and consists of three major components:

- Docker Daemon (dockerd)
- Docker CLI (Command Line Interface)
- Docker REST API

## 2. Docker Engine Architecture

```text
             Docker Client
               (Docker CLI)
                   |
                   |
              Docker API
                   |
                   v
            Docker Daemon
                (dockerd)
                   |
          +--------+--------+
          |        |        |
          v        v        v
       Images   Containers  Networks
                   |
                   v
              containerd
                   |
                   v
                 runc
                   |
                   v
             Linux Kernel
              (Namespaces
               & Cgroups)
```

## 3. Components of Docker Engine

### A. Docker Daemon (dockerd)

Docker Daemon is a background service responsible for managing Docker objects.

Responsibilities:

- Building Docker images.
- Creating and managing containers.
- Managing networks.
- Managing volumes.
- Communicating with Docker registries.
- Managing container lifecycle operations.

Check Docker Daemon status:

```bash
sudo systemctl status docker
```

Start Docker:

```bash
sudo systemctl start docker
```

Enable Docker at startup:

```bash
sudo systemctl enable docker
```

### B. Docker Client (Docker CLI)

Docker Client is the command-line interface used to interact with Docker Engine.

It sends commands to the Docker Daemon through the Docker API.

Examples:

```bash
docker version
docker info
docker ps
docker images
docker run nginx
```

### C. Docker REST API

Docker REST API allows applications and clients to communicate with Docker Daemon.

It supports operations such as:

- Creating containers.
- Starting and stopping containers.
- Building images.
- Managing networks.
- Managing volumes.

### D. containerd

containerd is a container runtime responsible for managing the container lifecycle.

Responsibilities:

- Managing container execution.
- Managing image transfers.
- Managing container storage.
- Supervising container processes.

### E. runc

runc is a low-level container runtime that creates and runs containers according to OCI specifications.

It uses Linux kernel features such as:

- Namespaces
- Control Groups (cgroups)
- Capabilities
- Seccomp

## 4. How Docker Engine Works

When a user executes:

```bash
docker run -d -p 8080:80 nginx
```

The following operations take place:

1. Docker CLI receives the command.
2. Docker CLI sends a request through the Docker REST API.
3. Docker Daemon processes the request.
4. Docker checks whether the Nginx image exists locally.
5. If unavailable, Docker pulls the image from a registry.
6. containerd manages the container lifecycle.
7. runc creates the container using Linux kernel features.
8. The Nginx application starts inside the container.
9. Port 8080 on the host maps to port 80 inside the container.

## 5. Docker Engine Installation

### Ubuntu

Update packages:

```bash
sudo apt update
```

Install Docker:

```bash
sudo apt install docker.io -y
```

Start Docker:

```bash
sudo systemctl start docker
```

Enable Docker:

```bash
sudo systemctl enable docker
```

Check Docker version:

```bash
docker --version
```

Verify installation:

```bash
sudo docker run hello-world
```

## 6. Docker Engine Important Commands

| Command | Description |
|---|---|
| docker version | Displays Docker version |
| docker info | Displays engine information |
| docker ps | Lists running containers |
| docker images | Lists Docker images |
| docker run | Creates and starts a container |
| docker pull | Downloads an image |
| docker build | Builds an image |
| docker network ls | Lists networks |
| docker volume ls | Lists volumes |
| docker system df | Shows Docker disk usage |
| docker system prune | Removes unused Docker data |

## 7. Docker Engine vs Docker Desktop

| Feature | Docker Engine | Docker Desktop |
|---|---|---|
| Purpose | Core container engine | Desktop development environment |
| CLI | Supported | Supported |
| Daemon | Core component | Runs engine components |
| GUI | Not included by default | Included |
| Linux Server | Commonly used | Not generally required |
| Windows/macOS | Requires a Linux environment for Linux containers | Provides integrated Linux environment |

## 8. Docker Engine vs Docker Daemon

| Docker Engine | Docker Daemon |
|---|---|
| Complete containerization technology | Background service |
| Includes client-server API architecture | Implements server-side operations |
| Provides container management functionality | Manages images, containers, networks, and volumes |
| Includes daemon and API components | Runs as dockerd |

## 9. Security Features

Docker Engine uses several Linux kernel security mechanisms:

### Namespaces

Provide isolation between containers.

Examples:
- PID namespace
- Network namespace
- Mount namespace
- IPC namespace
- UTS namespace
- User namespace

### Control Groups (cgroups)

Control and monitor resource usage.

Examples:
- CPU limits
- Memory limits
- Process limits

### Linux Capabilities

Allow fine-grained control over privileged operations.

### Seccomp

Restricts the system calls that a container can make.

## 10. Docker Engine Best Practices

1. Keep Docker Engine updated.
2. Use trusted Docker images.
3. Avoid running containers as root.
4. Limit container CPU and memory usage.
5. Use Docker networks appropriately.
6. Apply least-privilege access.
7. Avoid exposing the Docker API publicly.
8. Monitor Docker daemon logs.
9. Remove unused Docker resources.
10. Use image scanning tools to identify vulnerabilities.

## 11. Conclusion

Docker Engine is the core technology behind Docker containerization.

It provides the tools and services required to build images, create containers, manage resources, and run applications efficiently.

Understanding Docker Engine is essential for learning containerization, DevOps, Kubernetes, and cloud-native application deployment.
