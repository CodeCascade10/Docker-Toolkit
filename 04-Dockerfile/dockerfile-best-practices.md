
# Dockerfile Best Practices

This document covers best practices for writing secure, efficient, and maintainable Dockerfiles.

## 1. Use Official Base Images

Prefer official and trusted images.

```dockerfile
FROM python:3.12-slim
```

Avoid unnecessarily large images when smaller alternatives are available.

## 2. Use Specific Image Tags

Avoid using the `latest` tag in production.

```dockerfile
FROM node:22-alpine
```

Specific tags make builds more predictable.

## 3. Use Multi-Stage Builds

Separate build dependencies from runtime dependencies.

```dockerfile
FROM golang:1.25-alpine AS builder

WORKDIR /app
COPY . .
RUN go build -o app .

FROM alpine:3.22

WORKDIR /app
COPY --from=builder /app/app .

CMD ["./app"]
```

## 4. Minimize the Number of Layers

Combine related commands where appropriate.

```dockerfile
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*
```

## 5. Use .dockerignore

Exclude unnecessary files from the build context.

Example `.dockerignore`:

```text
node_modules/
.git/
.env
*.log
__pycache__/
```

## 6. Run Containers as a Non-Root User

Avoid running applications as root unless absolutely necessary.

```dockerfile
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

USER appuser
```

## 7. Use COPY Instead of ADD

Use `COPY` for ordinary file and directory copying.

```dockerfile
COPY app.py /app/
```

Use `ADD` only when its additional features are specifically needed.

## 8. Optimize Docker Build Cache

Copy dependency files before application source code.

```dockerfile
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
```

This helps Docker reuse the dependency installation layer when application code changes.

## 9. Avoid Storing Secrets in Images

Never hardcode passwords, API keys, or tokens in a Dockerfile.

Bad:

```dockerfile
ENV API_KEY="my-secret-key"
```

Use runtime environment variables or Docker secrets instead.

## 10. Use Exec Form for CMD

Prefer JSON/exec form over shell form.

```dockerfile
CMD ["python", "app.py"]
```

This allows the application to receive signals more directly.

## 11. Set a Working Directory

Use `WORKDIR` instead of repeatedly using `cd`.

```dockerfile
WORKDIR /app
```

## 12. Keep Images Small

- Choose lightweight base images where appropriate.
- Remove package-manager caches.
- Avoid installing unnecessary tools.
- Use multi-stage builds.
- Exclude unnecessary files using `.dockerignore`.

## 13. Scan Images for Vulnerabilities

Use Docker Scout or other image-scanning tools.

```bash
docker scout quickview my-image:latest
```

## 14. Use HEALTHCHECK When Appropriate

Define a health check for applications that need container health monitoring.

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s \
  CMD curl -f http://localhost:8000/health || exit 1
```

Make sure the required health-check utility is installed in the image.

## 15. Use Labels for Image Metadata

```dockerfile
LABEL maintainer="your-name"
LABEL version="1.0"
LABEL description="Sample Docker application"
```

## Quick Checklist

- [ ] Use trusted base images.
- [ ] Pin image versions appropriately.
- [ ] Use multi-stage builds where useful.
- [ ] Minimize image size.
- [ ] Add a `.dockerignore` file.
- [ ] Run as a non-root user.
- [ ] Never hardcode secrets.
- [ ] Optimize build-cache usage.
- [ ] Use exec-form `CMD`.
- [ ] Scan images for vulnerabilities.
- [ ] Add health checks when appropriate.
- [ ] Document important build and runtime settings.

## Further Learning

- Dockerfile reference: https://docs.docker.com/reference/dockerfile/
- Docker build best practices: https://docs.docker.com/build/building/best-practices/
- Docker Scout: https://docs.docker.com/scout/
