
# Go Dockerfile

This folder demonstrates how to containerize a Go application using Docker.

## Project Structure

```text
golang-dockerfile/
├── Dockerfile
├── go.mod
├── main.go
└── README.md
```

## Prerequisites

- Basic knowledge of Go
- Docker installed
- Understanding of Go modules

## Build the Docker Image

Run this command from inside the `golang-dockerfile` directory:

```bash
docker build -t go-docker-app .
```

## Run the Container

```bash
docker run --rm go-docker-app
```

## Expected Output

```text
Hello from Go Docker Container!
```

## What You'll Learn

- How to use an official Go base image
- How to compile Go applications inside Docker
- How to use multi-stage builds
- How to create smaller production images

## Cleanup

```bash
docker rmi go-docker-app
```
