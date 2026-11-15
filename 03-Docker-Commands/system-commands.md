
# Docker System Commands

## 1. Introduction

Docker system commands are used to manage and monitor the overall Docker environment.

They help administrators check Docker information, monitor resource usage, manage disk space, inspect system events, and maintain Docker services.

This guide covers essential Docker system commands with practical examples.

---

## 2. Docker System Information

### Check Docker Version

```bash
docker version
```

### Display Docker System Information

```bash
docker info
```

### Display Docker Client Version

```bash
docker --version
```

### Display Docker Daemon Information

```bash
docker info
```

### Check Docker Context

```bash
docker context ls
```

### Display Current Docker Context

```bash
docker context show
```

---

## 3. Docker Disk Usage

### Check Docker Disk Usage

```bash
docker system df
```

### Display Detailed Disk Usage

```bash
docker system df -v
```

This displays disk usage for:
- Images
- Containers
- Local volumes
- Build cache

---

## 4. Docker Resource Monitoring

### Monitor Container Resource Usage

```bash
docker stats
```

### Monitor Without Continuous Updates

```bash
docker stats --no-stream
```

### Monitor a Specific Container

```bash
docker stats <container_name>
```

### Display Running Processes Inside a Container

```bash
docker top <container_name>
```

---

## 5. Docker System Events

Docker events provide information about activities happening inside the Docker Engine.

### Display Docker Events

```bash
docker events
```

### Display Events from the Last 10 Minutes

```bash
docker events --since 10m
```

### Display Events Until a Specific Time

```bash
docker events --until 2026-11-15T15:00:00
```

### Filter Events by Container

```bash
docker events --filter container=mycontainer
```

### Filter Events by Type

```bash
docker events --filter type=container
```

---

## 6. Docker Context Management

Docker contexts allow users to manage connections to different Docker daemons.

### List Available Contexts

```bash
docker context ls
```

### Display Current Context

```bash
docker context show
```

### Create a New Context

```bash
docker context create mycontext \
  --docker host=ssh://user@server
```

### Switch Docker Context

```bash
docker context use mycontext
```

### Inspect a Context

```bash
docker context inspect mycontext
```

### Remove a Context

```bash
docker context rm mycontext
```

---

## 7. Docker System Cleanup

### Remove Unused Docker Resources

```bash
docker system prune
```

### Remove All Unused Images

```bash
docker system prune -a
```

### Remove Unused Resources Including Volumes

```bash
docker system prune -a --volumes
```

**Warning:** Cleanup commands can permanently delete Docker resources. Verify important containers, images, and volumes before running them.

---

## 8. Docker Service Management (Linux)

### Check Docker Service Status

```bash
sudo systemctl status docker
```

### Start Docker Service

```bash
sudo systemctl start docker
```

### Stop Docker Service

```bash
sudo systemctl stop docker
```

### Restart Docker Service

```bash
sudo systemctl restart docker
```

### Enable Docker at System Startup

```bash
sudo systemctl enable docker
```

### Disable Docker at System Startup

```bash
sudo systemctl disable docker
```

### View Docker Service Logs

```bash
sudo journalctl -u docker
```

### Follow Docker Service Logs

```bash
sudo journalctl -u docker -f
```

---

## 9. Docker Information and Inspection

### Display Docker Root Directory

```bash
docker info --format '{{.DockerRootDir}}'
```

### Display Storage Driver

```bash
docker info --format '{{.Driver}}'
```

### Display Number of Containers

```bash
docker info --format '{{.Containers}}'
```

### Display Number of Images

```bash
docker info --format '{{.Images}}'
```

### Display Docker Server Version

```bash
docker info --format '{{.ServerVersion}}'
```

---

## 10. Docker System Commands Cheat Sheet

| Command | Description |
|---|---|
| docker version | Display Docker version |
| docker info | Display system information |
| docker system df | Check disk usage |
| docker system df -v | Detailed disk usage |
| docker stats | Monitor resource usage |
| docker events | Display Docker events |
| docker context ls | List Docker contexts |
| docker context show | Show current context |
| docker context use | Switch Docker context |
| docker system prune | Clean unused resources |
| systemctl status docker | Check Docker service |
| systemctl restart docker | Restart Docker service |
| journalctl -u docker | View Docker service logs |

---

## 11. Docker System Best Practices

1. Monitor Docker resource usage regularly.
2. Check disk utilization to prevent storage issues.
3. Remove unused Docker resources.
4. Monitor Docker daemon logs.
5. Keep Docker Engine updated.
6. Use Docker contexts carefully when managing remote servers.
7. Configure appropriate resource limits.
8. Monitor container health and performance.
9. Secure access to the Docker daemon.
10. Back up important persistent data.

---

## 12. Conclusion

Docker system commands help administrators manage the overall Docker environment.

They are essential for monitoring, troubleshooting, resource management, service administration, and maintaining a healthy Docker infrastructure.
