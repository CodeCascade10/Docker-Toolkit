
# Docker Containers

## 1. Introduction

A Docker Container is a lightweight, isolated, executable environment created from a Docker Image.

It contains everything required to run an application, including its code, dependencies, libraries, and runtime.

Containers share the host operating system kernel, making them lightweight and faster than traditional virtual machines.

## 2. Container Architecture

```text
              Docker Image
                   |
                   | docker run
                   v
             Docker Container
                   |
          +--------+--------+
          |        |        |
          v        v        v
       Process  Filesystem  Network
          |
          v
     Running Application
```

## 3. Lifecycle of a Docker Container

```text
       docker create
              |
              v
          Created
              |
       docker start
              |
              v
          Running
           /   \
          /     \
 docker pause  docker stop
      |             |
      v             v
    Paused        Stopped
      |             |
 docker unpause  docker start
      |             |
      +------<------+
                    |
               docker rm
                    |
                    v
                 Removed
```

## 4. Important Docker Container Commands

### Create a Container

```bash
docker create --name mycontainer nginx
```

### Run a Container

```bash
docker run nginx
```

### Run in Detached Mode

```bash
docker run -d --name mycontainer nginx
```

### Run with Port Mapping

```bash
docker run -d -p 8080:80 nginx
```

Here:
- 8080 = Host port
- 80 = Container port

### List Running Containers

```bash
docker ps
```

### List All Containers

```bash
docker ps -a
```

### Start a Container

```bash
docker start mycontainer
```

### Stop a Container

```bash
docker stop mycontainer
```

### Restart a Container

```bash
docker restart mycontainer
```

### Pause a Container

```bash
docker pause mycontainer
```

### Unpause a Container

```bash
docker unpause mycontainer
```

### Remove a Container

```bash
docker rm mycontainer
```

### Force Remove a Container

```bash
docker rm -f mycontainer
```

## 5. Accessing Containers

### Execute Commands Inside a Container

```bash
docker exec -it mycontainer bash
```

For lightweight images that don't have Bash:

```bash
docker exec -it mycontainer sh
```

### View Container Logs

```bash
docker logs mycontainer
```

Follow logs continuously:

```bash
docker logs -f mycontainer
```

### Inspect Container Details

```bash
docker inspect mycontainer
```

### View Container Resource Usage

```bash
docker stats
```

## 6. Port Mapping

Port mapping allows applications running inside containers to be accessed from the host machine.

Example:

```bash
docker run -d -p 5000:5000 myapp
```

```text
        Host Machine
       localhost:5000
              |
              |
         Port Mapping
              |
              v
       Docker Container
        Port 5000
              |
              v
        Running App
```

## 7. Container Storage

By default, data stored inside a container's writable layer is tied to that container's lifecycle.

Docker provides volumes and bind mounts for persistent storage.

Example using a volume:

```bash
docker volume create myvolume

docker run -d \
  --name mycontainer \
  -v myvolume:/app/data \
  nginx
```

## 8. Container Networking

Containers can communicate through Docker networks.

Create a network:

```bash
docker network create mynetwork
```

Run a container inside the network:

```bash
docker run -d \
  --name web \
  --network mynetwork \
  nginx
```

List networks:

```bash
docker network ls
```

## 9. Docker Container vs Virtual Machine

| Feature | Container | Virtual Machine |
|---|---|---|
| OS | Shares host kernel | Separate guest OS |
| Startup | Fast | Slower |
| Size | Lightweight | Usually larger |
| Isolation | Process-level | Hardware-level |
| Resource Usage | Lower | Higher |
| Portability | High | Depends on VM setup |

## 10. Docker Container Best Practices

1. Use lightweight base images.
2. Run only necessary processes.
3. Avoid running containers as root where possible.
4. Use volumes for persistent data.
5. Configure health checks.
6. Set CPU and memory limits.
7. Regularly update container images.
8. Remove unused containers.
9. Use Docker networks for communication.
10. Monitor container logs and resource usage.

## 11. Useful Docker Commands Summary

| Command | Purpose |
|---|---|
| docker run | Create and start a container |
| docker create | Create a container |
| docker start | Start a stopped container |
| docker stop | Stop a running container |
| docker restart | Restart a container |
| docker pause | Pause processes |
| docker unpause | Resume processes |
| docker ps | List running containers |
| docker ps -a | List all containers |
| docker exec | Execute a command inside |
| docker logs | View container logs |
| docker inspect | Inspect container details |
| docker stats | Monitor resource usage |
| docker rm | Remove a container |

## 12. Conclusion

Docker containers provide lightweight, isolated, and portable environments for running applications.

They simplify application deployment, improve resource utilization, and ensure consistency across development, testing, and production environments.
