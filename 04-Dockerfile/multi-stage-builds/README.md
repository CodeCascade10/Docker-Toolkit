
# Docker Multi-Stage Builds

This folder demonstrates how to use Docker multi-stage builds to create smaller, optimized production images.

## What Are Multi-Stage Builds?

Multi-stage builds allow you to use multiple `FROM` instructions in a single Dockerfile.

Each stage can have a separate purpose, such as:

- Installing dependencies
- Compiling source code
- Building application assets
- Preparing the production image

Only the required files are copied into the final stage.

## Project Structure

```text
multi-stage-builds/
├── Dockerfile
├── app.py
└── README.md
```

## Build the Docker Image

Run this command from inside the `multi-stage-builds` directory:

```bash
docker build -t multi-stage-demo .
```

## Run the Container

```bash
docker run --rm multi-stage-demo
```

## Expected Output

```text
Hello from Docker Multi-Stage Build!
```

## Benefits

1. Smaller final Docker images.
2. Reduced attack surface.
3. Build tools are excluded from the runtime image.
4. Better separation between build and runtime environments.
5. More efficient production deployments.

## Inspect the Image Size

```bash
docker images multi-stage-demo
```

## Cleanup

```bash
docker rmi multi-stage-demo
```
