
# Docker Image Commands

## 1. Introduction

Docker image commands are used to download, build, list, inspect, tag, push, pull, and remove Docker images.

Docker images act as templates for creating Docker containers.

This guide covers essential Docker image commands with practical examples.

---

## 2. Downloading Docker Images

### Pull an Image from Docker Hub

```bash
docker pull nginx
```

### Pull a Specific Image Version

```bash
docker pull nginx:1.27
```

### Pull an Ubuntu Image

```bash
docker pull ubuntu:latest
```

### Pull an Image from a Private Registry

```bash
docker pull registry.example.com/myapp:v1
```

---

## 3. Listing Docker Images

### List All Images

```bash
docker images
```

### List Only Image IDs

```bash
docker images -q
```

### Display All Images Including Intermediate Images

```bash
docker images -a
```

### Display Images with Their Digests

```bash
docker images --digests
```

### Filter Images by Name

```bash
docker images nginx
```

---

## 4. Building Docker Images

### Build an Image from a Dockerfile

```bash
docker build -t myapp .
```

### Build an Image with a Specific Tag

```bash
docker build -t myapp:v1 .
```

### Build Without Using Cache

```bash
docker build --no-cache -t myapp:v1 .
```

### Build Using a Different Dockerfile

```bash
docker build -f Dockerfile.dev -t myapp:dev .
```

### Build with Build Arguments

```bash
docker build \
  --build-arg APP_ENV=production \
  -t myapp:production .
```

### Build with a Specific Platform

```bash
docker build --platform linux/amd64 -t myapp:v1 .
```

---

## 5. Tagging Docker Images

Tags are used to identify different versions of Docker images.

### Tag an Image

```bash
docker tag nginx nginx:custom
```

### Tag an Image for Docker Hub

```bash
docker tag myapp:latest username/myapp:v1
```

### Tag an Image for a Private Registry

```bash
docker tag myapp:v1 registry.example.com/myapp:v1
```

### List Tagged Images

```bash
docker images
```

---

## 6. Removing Docker Images

### Remove an Image

```bash
docker rmi nginx
```

### Remove an Image Using Its ID

```bash
docker rmi <image_id>
```

### Force Remove an Image

```bash
docker rmi -f nginx
```

### Remove All Images

```bash
docker rmi -f $(docker images -aq)
```

### Remove Unused Images

```bash
docker image prune
```

### Remove All Unused Images

```bash
docker image prune -a
```

---

## 7. Inspecting Docker Images

### Inspect Image Details

```bash
docker image inspect nginx
```

### View Image History

```bash
docker history nginx
```

### Display Image Size

```bash
docker images
```

### Inspect Image Manifest

```bash
docker manifest inspect nginx:latest
```

Note: `docker manifest inspect` inspects the image manifest available from a registry.

---

## 8. Pushing Images to Docker Hub

### Step 1: Login to Docker Hub

```bash
docker login
```

### Step 2: Tag Your Image

```bash
docker tag myapp:latest username/myapp:v1
```

### Step 3: Push Your Image

```bash
docker push username/myapp:v1
```

### Step 4: Verify the Image

Visit:

https://hub.docker.com/

Your repository should contain the uploaded image tag.

---

## 9. Saving and Loading Docker Images

Docker provides commands to export images into archive files and load them later.

### Save an Image to a TAR File

```bash
docker save -o myapp.tar myapp:v1
```

### Load an Image from a TAR File

```bash
docker load -i myapp.tar
```

### Save Multiple Images

```bash
docker save -o images.tar nginx:latest ubuntu:latest
```

Note: `docker save` and `docker load` preserve image information and tags.

---

## 10. Exporting and Importing Containers

These commands work with container filesystems rather than Docker image archives.

### Export a Container

```bash
docker export -o container.tar mycontainer
```

### Import a Container Filesystem as an Image

```bash
docker import container.tar myimported-image:v1
```

**Important difference:**

- `docker save` saves Docker images.
- `docker load` restores Docker images.
- `docker export` exports a container filesystem.
- `docker import` creates an image from an exported filesystem.

---

## 11. Image Filtering and Searching

### Search Docker Hub

```bash
docker search nginx
```

### Filter Images by Reference

```bash
docker images --filter reference='nginx:*'
```

### Display Dangling Images

```bash
docker images -f dangling=true
```

### Display Images Created Before a Certain Image

```bash
docker images --filter before=nginx
```

---

## 12. Docker Image Commands Cheat Sheet

| Command | Description |
|---|---|
| docker pull | Download an image |
| docker build | Build an image |
| docker images | List images |
| docker images -q | List image IDs |
| docker tag | Tag an image |
| docker push | Upload an image |
| docker rmi | Remove an image |
| docker image prune | Remove dangling images |
| docker image inspect | Inspect image details |
| docker history | Display image history |
| docker save | Save images to an archive |
| docker load | Load images from an archive |
| docker export | Export container filesystem |
| docker import | Create an image from a filesystem archive |
| docker search | Search Docker Hub |
| docker manifest inspect | Inspect registry image manifest |

---

## 13. Docker Image Best Practices

1. Use lightweight base images.
2. Use meaningful image tags.
3. Avoid using only the `latest` tag.
4. Remove unnecessary dependencies.
5. Use multi-stage builds.
6. Use `.dockerignore` to exclude unnecessary files.
7. Scan images for vulnerabilities.
8. Use trusted base images.
9. Optimize image layers.
10. Keep production images small and secure.

---

## 14. Conclusion

Docker image commands are essential for managing the complete image lifecycle.

They help developers build, distribute, version, inspect, and optimize container images efficiently.
