
# Docker Registry

## 1. Introduction

A Docker Registry is a storage and distribution system used to store, manage, and distribute Docker images.

Developers can push images to a registry and pull them whenever required.

Docker registries can be:

- Public registries
- Private registries

**Popular Docker Registries:**

- Docker Hub
- Amazon Elastic Container Registry (ECR)
- GitHub Container Registry (GHCR)
- Google Artifact Registry
- Azure Container Registry (ACR)

## 2. Docker Registry Architecture

```text
             Developer
                 |
                 |
          Build Docker Image
                 |
                 v
             Docker CLI
                 |
          +------+------+
          |             |
          |             |
       docker push   docker pull
          |             ^
          v             |
       +-------------------+
       |  Docker Registry  |
       |                   |
       |   Docker Images   |
       |                   |
       +-------------------+
                 |
                 v
          Docker Containers
```

## 3. How Docker Registry Works

### Step 1: Build an Image

```bash
docker build -t myapp:latest .
```

### Step 2: Login to Docker Hub

```bash
docker login
```

### Step 3: Tag the Image

```bash
docker tag myapp:latest username/myapp:v1
```

### Step 4: Push the Image

```bash
docker push username/myapp:v1
```

### Step 5: Pull the Image

```bash
docker pull username/myapp:v1
```

### Step 6: Run the Container

```bash
docker run -d -p 8080:80 username/myapp:v1
```

## 4. Docker Hub

Docker Hub is a cloud-based registry service used to store and distribute Docker images.

Features:

- Public and private repositories.
- Official Docker images.
- Automated builds.
- Image tagging and versioning.
- Access control.
- Image sharing.

Website: https://hub.docker.com/

### Docker Hub Commands

Login:

```bash
docker login
```

Search for an image:

```bash
docker search nginx
```

Pull an image:

```bash
docker pull nginx
```

Tag an image:

```bash
docker tag nginx username/nginx:v1
```

Push an image:

```bash
docker push username/nginx:v1
```

Logout:

```bash
docker logout
```

## 5. Docker Image Naming Convention

Docker images follow this naming structure:

```text
[REGISTRY]/[USERNAME]/[REPOSITORY]:[TAG]
```

Example:

```text
docker.io/knaskar10/myapp:v1
```

Components:

| Component | Description |
|---|---|
| docker.io | Registry |
| knaskar10 | Docker Hub username |
| myapp | Repository name |
| v1 | Image tag |

Note: Registry and namespace components can be omitted when Docker uses its default registry and namespace conventions.

## 6. Public Registry vs Private Registry

| Feature | Public Registry | Private Registry |
|---|---|---|
| Access | Publicly accessible images | Restricted access |
| Security | Depends on repository settings | Access-controlled |
| Usage | Sharing public images | Organization applications |
| Cost | Often free tiers available | Depends on provider |
| Examples | Docker Hub public repositories | Private ECR repositories |

## 7. Popular Docker Registries

### A. Docker Hub

- Official Docker registry service.
- Supports public and private repositories.
- Provides official images.

Website: https://hub.docker.com/

### B. Amazon ECR

Amazon Elastic Container Registry is a managed container image registry provided by AWS.

Features:

- Private and public repositories.
- IAM-based access control.
- Image scanning.
- Integration with ECS and EKS.

Website: https://aws.amazon.com/ecr/

### C. GitHub Container Registry

GHCR allows developers to store and manage container images alongside GitHub projects.

Features:

- GitHub repository integration.
- Access control.
- Package management.
- CI/CD integration.

Website: https://ghcr.io/

### D. Google Artifact Registry

A managed service from Google Cloud for storing and managing container images and other artifacts.

Website: https://cloud.google.com/artifact-registry

### E. Azure Container Registry

A managed container registry provided by Microsoft Azure.

Website: https://azure.microsoft.com/products/container-registry

## 8. Docker Registry vs Docker Repository

| Docker Registry | Docker Repository |
|---|---|
| Stores multiple repositories | Stores related image versions |
| Acts as a distribution service | Organizes images |
| Example: Docker Hub | Example: nginx |
| Contains multiple repositories | Contains multiple tags |

Example:

```text
Docker Hub (Registry)
       |
       +------ nginx (Repository)
       |          |
       |          +--- latest
       |          +--- 1.27
       |
       +------ redis (Repository)
                  |
                  +--- latest
                  +--- 7
```

## 9. Image Versioning and Tagging

Tags help identify different versions of Docker images.

Examples:

```bash
docker tag myapp username/myapp:v1
docker tag myapp username/myapp:v2
docker tag myapp username/myapp:production
```

List images:

```bash
docker images
```

Best practices:

1. Use meaningful image tags.
2. Avoid relying only on the `latest` tag.
3. Use version numbers.
4. Keep production and development tags separate.
5. Use immutable image digests when reproducibility is important.

## 10. Docker Registry Security Best Practices

1. Use strong authentication.
2. Enable multi-factor authentication where available.
3. Use private repositories for confidential images.
4. Scan images for vulnerabilities.
5. Avoid storing passwords in Dockerfiles.
6. Use access tokens instead of account passwords where supported.
7. Apply least-privilege access.
8. Use trusted base images.
9. Remove unused images and tags.
10. Never expose registry credentials in GitHub repositories.

## 11. Important Docker Registry Commands

| Command | Description |
|---|---|
| docker login | Authenticate with registry |
| docker logout | Log out from registry |
| docker search | Search Docker Hub images |
| docker pull | Download an image |
| docker push | Upload an image |
| docker tag | Assign an image tag |
| docker images | List local images |
| docker manifest inspect | Inspect image manifest |
| docker image inspect | Inspect local image details |

## 12. Real-World DevOps Workflow

```text
       Developer
           |
           v
      Write Code
           |
           v
       GitHub Repo
           |
           v
      Docker Build
           |
           v
      Docker Image
           |
           v
      Docker Push
           |
           v
      Docker Hub / ECR
           |
           v
      Kubernetes Cluster
           |
           v
       Running Pods
```

## 13. Conclusion

Docker Registry plays an important role in containerization by providing a centralized platform to store, manage, and distribute Docker images.

It is widely used in CI/CD pipelines, cloud deployments, and Kubernetes environments.
