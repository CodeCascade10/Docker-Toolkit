
# Docker Container Commands

## 1. Introduction

Docker container commands are used to create, start, stop, inspect, monitor, and manage Docker containers.

Containers are isolated environments created from Docker images.

This guide covers the most commonly used Docker container commands with practical examples.

---

## 2. Listing Containers

### List Running Containers

```bash
docker ps
```

### List All Containers

```bash
docker ps -a
```

### List Only Container IDs

```bash
docker ps -q
```

### List the Latest Created Container

```bash
docker ps -l
```

### Display Container Size

```bash
docker ps -s
```

---

## 3. Creating and Running Containers

### Run a Container

```bash
docker run nginx
```

### Run in Detached Mode

```bash
docker run -d nginx
```

### Run with a Custom Name

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

### Run with Environment Variables

```bash
docker run -d \
  --name myapp \
  -e APP_ENV=production \
  nginx
```

### Run an Interactive Container

```bash
docker run -it ubuntu bash
```

### Run a Container and Automatically Remove It

```bash
docker run --rm ubuntu echo "Hello Docker"
```

---

## 4. Starting, Stopping and Restarting Containers

### Start a Stopped Container

```bash
docker start mycontainer
```

### Stop a Running Container

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

### Kill a Container Immediately

```bash
docker kill mycontainer
```

---

## 5. Removing Containers

### Remove a Stopped Container

```bash
docker rm mycontainer
```

### Force Remove a Running Container

```bash
docker rm -f mycontainer
```

### Remove All Stopped Containers

```bash
docker container prune
```

### Remove All Containers

```bash
docker rm -f $(docker ps -aq)
```

**Warning:** Removing a container does not automatically remove its named volumes.

---

## 6. Executing Commands Inside Containers

### Open an Interactive Bash Shell

```bash
docker exec -it mycontainer bash
```

### Open an Interactive Shell Using sh

```bash
docker exec -it mycontainer sh
```

### Execute a Single Command

```bash
docker exec mycontainer ls
```

### Execute a Command as Root

```bash
docker exec -u root -it mycontainer bash
```

### Execute a Command in a Specific Working Directory

```bash
docker exec -w /app mycontainer pwd
```

---

## 7. Viewing Container Logs

### Display Container Logs

```bash
docker logs mycontainer
```

### Follow Logs Continuously

```bash
docker logs -f mycontainer
```

### Display the Last 100 Lines

```bash
docker logs --tail 100 mycontainer
```

### Display Logs with Timestamps

```bash
docker logs -t mycontainer
```

### Display Logs from the Last 10 Minutes

```bash
docker logs --since 10m mycontainer
```

---

## 8. Inspecting Containers

### Inspect Container Details

```bash
docker inspect mycontainer
```

### Display Container IP Address

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mycontainer
```

### Display Container Status

```bash
docker inspect -f '{{.State.Status}}' mycontainer
```

### Display Container Restart Count

```bash
docker inspect -f '{{.RestartCount}}' mycontainer
```

### Display Container Configuration

```bash
docker inspect -f '{{.Config}}' mycontainer
```

---

## 9. Container Resource Monitoring

### Display Live Resource Usage

```bash
docker stats
```

### Monitor a Specific Container

```bash
docker stats mycontainer
```

### Display Resource Usage Once

```bash
docker stats --no-stream
```

### Display Container Processes

```bash
docker top mycontainer
```

---

## 10. Copying Files Between Host and Container

### Copy a File from Host to Container

```bash
docker cp app.py mycontainer:/app/
```

### Copy a File from Container to Host

```bash
docker cp mycontainer:/app/app.py .
```

### Copy an Entire Directory

```bash
docker cp ./project mycontainer:/app/
```

---

## 11. Container Configuration Commands

### Rename a Container

```bash
docker rename oldname newname
```

### Update Container Resource Limits

```bash
docker update --memory 512m mycontainer
```

### Update CPU Limit

```bash
docker update --cpus 1.5 mycontainer
```

### Update Restart Policy

```bash
docker update --restart unless-stopped mycontainer
```

### Display Container Port Mappings

```bash
docker port mycontainer
```

---

## 12. Container Health and Status

### Display Container Health Information

```bash
docker inspect -f '{{.State.Health.Status}}' mycontainer
```

This requires a health check to be configured.

### View Container Events

```bash
docker events
```

### Display Recent Container Events

```bash
docker events --since 10m
```

---

## 13. Docker Container Commands Cheat Sheet

| Command | Description |
|---|---|
| docker ps | List running containers |
| docker ps -a | List all containers |
| docker run | Create and start a container |
| docker start | Start a stopped container |
| docker stop | Stop a running container |
| docker restart | Restart a container |
| docker pause | Pause a container |
| docker unpause | Resume a container |
| docker kill | Forcefully stop a container |
| docker rm | Remove a container |
| docker exec | Execute commands inside a container |
| docker logs | View container logs |
| docker inspect | Inspect container configuration |
| docker stats | Monitor resource usage |
| docker top | Display container processes |
| docker cp | Copy files to/from containers |
| docker rename | Rename a container |
| docker port | Display port mappings |
| docker update | Update container configuration |

---

## 14. Best Practices

1. Give meaningful names to containers.
2. Use detached mode for background services.
3. Check logs when troubleshooting.
4. Use resource limits for production containers.
5. Avoid running containers as root unnecessarily.
6. Configure appropriate restart policies.
7. Use health checks to monitor application health.
8. Remove unused containers regularly.
9. Use environment variables for configuration.
10. Avoid exposing unnecessary container ports.

---

## 15. Conclusion

Docker container commands are essential for managing containerized applications.

Understanding these commands helps developers and DevOps engineers deploy, monitor, troubleshoot, and maintain Docker containers efficiently.
