
# Docker Volume Commands

## 1. Introduction

Docker volumes are used to persist data generated and used by Docker containers.

Container data stored only in the container's writable layer can be lost when the container is removed.

Volumes provide persistent storage independent of a container's lifecycle.

This guide covers essential Docker volume commands with practical examples.

---

## 2. Listing Docker Volumes

### List All Volumes

```bash
docker volume ls
```

### List Only Volume Names

```bash
docker volume ls -q
```

### Filter Volumes by Driver

```bash
docker volume ls --filter driver=local
```

### Display Volume Details

```bash
docker volume inspect myvolume
```

---

## 3. Creating Docker Volumes

### Create a Volume

```bash
docker volume create myvolume
```

### Create a Volume with a Specific Driver

```bash
docker volume create \
  --driver local \
  myvolume
```

### Create a Volume with Labels

```bash
docker volume create \
  --label environment=production \
  myvolume
```

### Create a Volume with Multiple Labels

```bash
docker volume create \
  --label environment=production \
  --label project=myapp \
  myvolume
```

---

## 4. Using Volumes with Containers

### Mount a Volume into a Container

```bash
docker run -d \
  --name mycontainer \
  -v myvolume:/app/data \
  nginx
```

Here:
- `myvolume` = Docker volume name.
- `/app/data` = Mount path inside the container.

### Use the --mount Flag

```bash
docker run -d \
  --name mycontainer \
  --mount source=myvolume,target=/app/data \
  nginx
```

### Mount a Read-Only Volume

```bash
docker run -d \
  --name mycontainer \
  --mount source=myvolume,target=/app/data,readonly \
  nginx
```

### Mount an Existing Volume

```bash
docker run -d \
  --name newcontainer \
  --mount source=myvolume,target=/data \
  nginx
```

---

## 5. Removing Docker Volumes

### Remove a Specific Volume

```bash
docker volume rm myvolume
```

### Remove All Unused Volumes

```bash
docker volume prune
```

### Remove Unused Volumes Without Confirmation

```bash
docker volume prune -f
```

### Remove All Unused Anonymous Volumes

```bash
docker volume prune --all
```

**Warning:** Docker cannot remove a volume that is currently in use by a container. Removing volumes can permanently delete stored data.

---

## 6. Inspecting Docker Volumes

### Inspect Volume Details

```bash
docker volume inspect myvolume
```

### Display Volume Mountpoint

```bash
docker volume inspect \
  -f '{{.Mountpoint}}' myvolume
```

### Display Volume Driver

```bash
docker volume inspect \
  -f '{{.Driver}}' myvolume
```

### Display Volume Labels

```bash
docker volume inspect \
  -f '{{.Labels}}' myvolume
```

---

## 7. Copying Data into Volumes

### Step 1: Create a Volume

```bash
docker volume create myvolume
```

### Step 2: Create a Container

```bash
docker run -d \
  --name mycontainer \
  -v myvolume:/data \
  nginx
```

### Step 3: Create a File Inside the Volume

```bash
docker exec mycontainer sh -c \
  "echo 'Hello Docker Volume' > /data/test.txt"
```

### Step 4: Verify the File

```bash
docker exec mycontainer cat /data/test.txt
```

### Step 5: Remove the Container

```bash
docker rm -f mycontainer
```

### Step 6: Create Another Container Using the Same Volume

```bash
docker run --rm \
  -v myvolume:/data \
  alpine cat /data/test.txt
```

Expected Output:

```text
Hello Docker Volume
```

This demonstrates that volume data persists even after the original container is removed.

---

## 8. Backup and Restore Docker Volumes

### Backup a Volume

```bash
docker run --rm \
  -v myvolume:/data:ro \
  -v "$PWD":/backup \
  alpine \
  tar czf /backup/myvolume-backup.tar.gz -C /data .
```

This creates a compressed backup of the volume in the current host directory.

### Restore a Volume

First, create a new volume:

```bash
docker volume create restored-volume
```

Restore the backup:

```bash
docker run --rm \
  -v restored-volume:/data \
  -v "$PWD":/backup:ro \
  alpine \
  tar xzf /backup/myvolume-backup.tar.gz -C /data
```

Note: The commands above use Linux/macOS shell syntax. On Windows, use a compatible shell and adjust the host path if necessary.

---

## 9. Docker Volume Drivers

Docker supports volume drivers that allow data to be stored using different storage backends.

### List Available Volume Drivers

```bash
docker info
```

### Create a Volume Using the Local Driver

```bash
docker volume create \
  --driver local \
  myvolume
```

### Inspect the Volume Driver

```bash
docker volume inspect myvolume
```

Common storage options include:

- Local filesystem storage.
- NFS-based storage through supported configurations.
- Cloud and third-party storage plugins.

---

## 10. Docker Volumes vs Bind Mounts

| Feature | Docker Volumes | Bind Mounts |
|---|---|---|
| Storage Location | Docker-managed | User-specified host path |
| Management | Docker CLI | Host filesystem |
| Portability | Easier to manage | Depends on host paths |
| Backup | Can use Docker tools | Use host backup tools |
| Use Case | Persistent application data | Development and file sharing |

### Volume Example

```bash
docker run -d \
  -v myvolume:/app/data \
  nginx
```

### Bind Mount Example

```bash
docker run -d \
  --mount type=bind,source=/home/user/app,target=/app \
  nginx
```

---

## 11. Docker Volume Commands Cheat Sheet

| Command | Description |
|---|---|
| docker volume ls | List all volumes |
| docker volume create | Create a volume |
| docker volume inspect | Inspect volume details |
| docker volume rm | Remove a volume |
| docker volume prune | Remove unused volumes |
| docker volume prune -a | Remove all unused volumes, including anonymous ones |
| docker run -v | Mount a volume |
| docker run --mount | Mount storage using explicit options |

---

## 12. Docker Volume Best Practices

1. Use named volumes for persistent application data.
2. Avoid storing important data only inside containers.
3. Back up volumes regularly.
4. Use read-only mounts wherever possible.
5. Monitor volume storage usage.
6. Avoid removing volumes without checking their contents.
7. Use appropriate volume drivers.
8. Separate application data from container images.
9. Test backup and restore procedures.
10. Use meaningful volume names.

---

## 13. Conclusion

Docker volumes provide persistent storage for containerized applications.

They allow data to survive container removal and recreation, making them essential for databases, backend applications, and production workloads.
