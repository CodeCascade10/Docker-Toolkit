
# Docker Troubleshooting Commands

## 1. Introduction

Docker troubleshooting commands help identify, diagnose, and resolve problems related to Docker containers, images, networks, volumes, and Docker Engine.

Common Docker issues include:

- Containers failing to start.
- Port conflicts.
- Image pull failures.
- Network connectivity problems.
- Container crashes.
- Storage issues.
- Docker daemon errors.

This guide covers commonly used troubleshooting commands and solutions.

---

## 2. Docker Installation Issues

### Check Docker Version

```bash
docker --version
```

### Check Docker Engine Status

```bash
sudo systemctl status docker
```

### Start Docker Engine

```bash
sudo systemctl start docker
```

### Restart Docker Engine

```bash
sudo systemctl restart docker
```

### Check Docker Information

```bash
docker info
```

### Verify Docker Installation

```bash
sudo docker run hello-world
```

---

## 3. Container Troubleshooting

### List All Containers

```bash
docker ps -a
```

### Check Container Logs

```bash
docker logs <container_name>
```

### Follow Container Logs

```bash
docker logs -f <container_name>
```

### Inspect Container Details

```bash
docker inspect <container_name>
```

### Check Container Processes

```bash
docker top <container_name>
```

### Check Container Resource Usage

```bash
docker stats
```

### Restart a Container

```bash
docker restart <container_name>
```

---

## 4. Container Fails to Start

### Check Container Status

```bash
docker ps -a
```

### Inspect Container State

```bash
docker inspect <container_name>
```

### Check Container Logs

```bash
docker logs <container_name>
```

### Try Running the Container Interactively

```bash
docker run -it ubuntu bash
```

Possible reasons:

- Incorrect application configuration.
- Missing environment variables.
- Application startup errors.
- Missing dependencies.
- Incorrect container command.

---

## 5. Port Conflict Issues

A port conflict occurs when another process is already using the requested host port.

### Check Container Port Mapping

```bash
docker port <container_name>
```

### Check Running Containers

```bash
docker ps
```

### Linux: Check Port Usage

```bash
sudo ss -tulpn
```

### Windows PowerShell: Check Port Usage

```powershell
netstat -ano | findstr :8080
```

### Run the Container on Another Port

```bash
docker run -d -p 8081:80 nginx
```

---

## 6. Docker Image Troubleshooting

### List Available Images

```bash
docker images
```

### Inspect an Image

```bash
docker image inspect nginx
```

### Check Image History

```bash
docker history nginx
```

### Pull an Image Again

```bash
docker pull nginx:latest
```

### Remove an Image

```bash
docker rmi <image_name>
```

### Build Without Cache

```bash
docker build --no-cache -t myapp .
```

Common image-related problems:

- Image not found.
- Incorrect image tag.
- Registry authentication failure.
- Network connectivity problems.
- Insufficient disk space.

---

## 7. Docker Network Troubleshooting

### List Networks

```bash
docker network ls
```

### Inspect a Network

```bash
docker network inspect <network_name>
```

### Check Container IP Address

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_name>
```

### Connect a Container to a Network

```bash
docker network connect <network_name> <container_name>
```

### Test Container Connectivity

```bash
docker exec <container_name> ping <target>
```

Note: The container image must contain the ping utility.

Common networking problems:

- Containers cannot communicate.
- Incorrect port mapping.
- DNS resolution failures.
- Containers attached to different networks.
- Firewall restrictions.

---

## 8. Docker Volume Troubleshooting

### List Volumes

```bash
docker volume ls
```

### Inspect a Volume

```bash
docker volume inspect <volume_name>
```

### Check Container Mounts

```bash
docker inspect -f '{{json .Mounts}}' <container_name>
```

### Create a Volume

```bash
docker volume create myvolume
```

### Attach a Volume to a Container

```bash
docker run -d \
  --name mycontainer \
  -v myvolume:/data \
  nginx
```

Common volume problems:

- Incorrect mount path.
- Permission issues.
- Missing volume.
- Incorrect file ownership.
- Insufficient storage.

---

## 9. Docker Resource and Disk Issues

### Check Docker Disk Usage

```bash
docker system df
```

### Detailed Disk Usage

```bash
docker system df -v
```

### Check Container Resource Usage

```bash
docker stats
```

### Remove Unused Containers

```bash
docker container prune
```

### Remove Unused Images

```bash
docker image prune -a
```

### Remove Unused Networks

```bash
docker network prune
```

### Remove Build Cache

```bash
docker builder prune
```

Warning: Review resources before cleanup. Avoid deleting volumes containing important data.

---

## 10. Docker Daemon Troubleshooting

### Check Docker Service

```bash
sudo systemctl status docker
```

### Restart Docker Service

```bash
sudo systemctl restart docker
```

### View Docker Daemon Logs

```bash
sudo journalctl -u docker
```

### Follow Docker Daemon Logs

```bash
sudo journalctl -u docker -f
```

### Check Docker Socket

```bash
ls -l /var/run/docker.sock
```

Common daemon problems:

- Docker service is stopped.
- Docker socket permission errors.
- Incorrect daemon configuration.
- Storage driver problems.
- Insufficient system resources.

---

## 11. Common Docker Errors and Solutions

| Error | Possible Solution |
|---|---|
| Cannot connect to Docker daemon | Start or restart Docker service |
| Port already allocated | Use another host port |
| Image not found | Verify image name and tag |
| Permission denied | Check Docker socket permissions |
| Container exited | Inspect logs and exit code |
| No space left on device | Check disk usage and clean unused resources |
| Network not found | Create or verify the network |
| Container name already in use | Rename or remove the existing container |
| Bind source path does not exist | Verify the host directory |
| Connection refused | Verify application status and listening port |

---

## 12. Useful Docker Debugging Commands

### Inspect Container Configuration

```bash
docker inspect <container_name>
```

### Display Container Logs

```bash
docker logs <container_name>
```

### Execute a Shell Inside a Container

```bash
docker exec -it <container_name> sh
```

### Display Container Processes

```bash
docker top <container_name>
```

### Display Docker Events

```bash
docker events
```

### Check Docker System Information

```bash
docker info
```

---

## 13. Docker Troubleshooting Best Practices

1. Always check container status first.
2. Examine container logs before restarting.
3. Use Docker inspect to investigate configuration.
4. Check port mappings and network settings.
5. Monitor CPU, memory, and disk usage.
6. Verify image names and tags.
7. Check Docker daemon status.
8. Avoid unnecessary container deletion.
9. Back up important volume data.
10. Document recurring errors and their solutions.

---

## 14. Troubleshooting Workflow

```text
       Docker Issue
            |
            v
     Check Container Status
            |
            v
       Check Logs
            |
            v
      Inspect Container
            |
            v
    Check Network & Ports
            |
            v
    Check Resource Usage
            |
            v
     Identify Root Cause
            |
            v
       Apply Fix
            |
            v
       Verify Solution
```

---

## 15. Conclusion

Docker troubleshooting commands are essential for diagnosing and resolving containerization problems.

Understanding logs, container inspection, networking, storage, and resource monitoring helps DevOps engineers maintain reliable Docker environments.
