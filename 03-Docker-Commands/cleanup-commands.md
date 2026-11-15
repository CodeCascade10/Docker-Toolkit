
# Docker Cleanup Commands

## 1. Introduction

Docker cleanup commands help remove unused Docker resources such as containers, images, networks, build cache, and volumes.

Regular cleanup helps free disk space and maintain a clean Docker environment.

## 2. Container Cleanup

### Remove a Stopped Container

```bash
docker rm <container_id>
```

### Remove All Stopped Containers

```bash
docker container prune
```

### Force Remove a Running Container

```bash
docker rm -f <container_id>
```

### Remove All Containers

```bash
docker rm -f $(docker ps -aq)
```

## 3. Image Cleanup

### Remove an Image

```bash
docker rmi <image_id>
```

### Remove All Unused Images

```bash
docker image prune
```

### Remove All Unused Images Including Tagged Images

```bash
docker image prune -a
```

### Remove All Images

```bash
docker rmi -f $(docker images -aq)
```

## 4. Volume Cleanup

### List All Volumes

```bash
docker volume ls
```

### Remove a Volume

```bash
docker volume rm <volume_name>
```

### Remove All Unused Volumes

```bash
docker volume prune
```

## 5. Network Cleanup

### List Networks

```bash
docker network ls
```

### Remove a Network

```bash
docker network rm <network_name>
```

### Remove All Unused Networks

```bash
docker network prune
```

## 6. Build Cache Cleanup

### Remove Build Cache

```bash
docker builder prune
```

### Remove All Build Cache

```bash
docker builder prune -a
```

## 7. Complete Docker System Cleanup

### Remove Unused Containers, Networks, Images and Build Cache

```bash
docker system prune
```

### Remove All Unused Images Too

```bash
docker system prune -a
```

### Remove Unused Volumes Along With Other Resources

```bash
docker system prune -a --volumes
```

## 8. Monitor Docker Disk Usage

### Check Docker Disk Usage

```bash
docker system df
```

### Detailed Disk Usage

```bash
docker system df -v
```

## 9. Important Docker Cleanup Commands Summary

| Command | Purpose |
|---|---|
| docker container prune | Remove stopped containers |
| docker image prune | Remove dangling images |
| docker image prune -a | Remove unused images |
| docker volume prune | Remove unused volumes |
| docker network prune | Remove unused networks |
| docker builder prune | Remove build cache |
| docker system prune | Clean unused resources |
| docker system df | Check disk usage |

## 10. Cleanup Best Practices

1. Check running containers before removing resources.
2. Remove unused containers regularly.
3. Avoid deleting volumes containing important data.
4. Check disk usage before performing cleanup.
5. Use prune commands carefully.
6. Never remove production resources without verification.
7. Back up important data before cleanup.

## 11. Important Warning

Docker cleanup commands can permanently delete resources.

Be especially careful with:

```bash
docker system prune -a --volumes
```

This can remove unused images, containers, networks, build cache, and volumes. Always verify which resources are safe to delete.

## 12. Conclusion

Docker cleanup commands help maintain an efficient Docker environment by removing unnecessary resources and freeing disk space.
