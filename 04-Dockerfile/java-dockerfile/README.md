
# Java Dockerfile

This folder demonstrates how to containerize a Java application using Docker.

## Project Structure

```text
java-dockerfile/
├── Dockerfile
├── src/
│   └── Main.java
└── README.md
```

## Prerequisites

- Java knowledge
- Docker installed
- Basic understanding of Java compilation

## Build the Docker Image

Run this command from inside the `java-dockerfile` directory:

```bash
docker build -t java-docker-app .
```

## Run the Container

```bash
docker run --rm java-docker-app
```

## Expected Output

```text
Hello from Java Docker Container!
```

## What You'll Learn

- How to use a Java base image
- How to compile Java applications inside Docker
- How to execute Java applications inside containers
- How to use Docker multi-stage builds for Java applications

## Cleanup

```bash
docker rmi java-docker-app
```
