
# Node.js Dockerfile

## 1. Introduction

Docker allows us to containerize Node.js applications by packaging the Node.js runtime, application source code, dependencies, and configuration into a Docker image.

This makes Node.js applications portable and consistent across development, testing, and production environments.

In this section, we will learn how to:

- Create a Node.js Dockerfile.
- Install dependencies using npm.
- Build Docker images.
- Run Node.js applications inside containers.
- Expose application ports.
- Use environment variables.
- Optimize Node.js Docker images.
- Apply Dockerfile security best practices.

---

## 2. Project Structure

```text
node-dockerfile/
│
├── Dockerfile
├── app.js
├── package.json
├── package-lock.json
├── .dockerignore
└── README.md
```

---

## 3. Create a Node.js Application

Create a file named `app.js`.

```javascript
const express = require("express");

const app = express();

const PORT = process.env.PORT || 3000;

app.get("/", (req, res) => {
    res.json({
        message: "Hello from Node.js Docker!",
        status: "Running successfully"
    });
});

app.get("/about", (req, res) => {
    res.json({
        application: "Node.js Docker Demo",
        version: "1.0.0"
    });
});

app.get("/health", (req, res) => {
    res.json({
        status: "healthy"
    });
});

app.listen(PORT, "0.0.0.0", () => {
    console.log(`Server running on port ${PORT}`);
});
```

---

## 4. Create package.json

Create a file named `package.json`.

```json
{
  "name": "node-docker-app",
  "version": "1.0.0",
  "description": "Node.js application running inside Docker",
  "main": "app.js",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "^5.1.0"
  }
}
```

Install dependencies and generate `package-lock.json`:

```bash
npm install
```

---

## 5. Create Dockerfile

Create a file named `Dockerfile`.

```dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package*.json ./

RUN npm ci

COPY . .

ENV NODE_ENV=production

EXPOSE 3000

CMD ["npm", "start"]
```

### Dockerfile Explanation

| Instruction | Purpose |
|---|---|
| FROM | Uses Node.js base image |
| WORKDIR | Sets application directory |
| COPY | Copies package files |
| RUN | Installs dependencies |
| ENV | Sets environment variables |
| EXPOSE | Documents application port |
| CMD | Starts Node.js application |

---

## 6. Create .dockerignore

```text
node_modules/
npm-debug.log
.git/
.gitignore
.env
.env.*
!.env.example
.vscode/
.idea/
coverage/
*.log
.DS_Store
Thumbs.db
```

This prevents unnecessary files from entering the Docker build context.

---

## 7. Build Docker Image

```bash
docker build -t node-docker-app .
```

Verify the image:

```bash
docker images
```

---

## 8. Run Docker Container

```bash
docker run -d \
  --name node-container \
  -p 3000:3000 \
  node-docker-app
```

Check running containers:

```bash
docker ps
```

---

## 9. Test the Application

Open your browser:

```text
http://localhost:3000
```

Test health endpoint:

```text
http://localhost:3000/health
```

Test using curl:

```bash
curl http://localhost:3000
```

Expected response:

```json
{
    "message": "Hello from Node.js Docker!",
    "status": "Running successfully"
}
```

---

## 10. Useful Docker Commands

### View Container Logs

```bash
docker logs node-container
```

### Enter Container

```bash
docker exec -it node-container sh
```

### Stop Container

```bash
docker stop node-container
```

### Remove Container

```bash
docker rm node-container
```

### Remove Image

```bash
docker rmi node-docker-app
```

---

## 11. Docker Image Optimization

Best practices:

1. Use lightweight Node.js base images.
2. Use Alpine images where appropriate.
3. Copy package files before application source code.
4. Use `npm ci` for reproducible dependency installation.
5. Create a `.dockerignore` file.
6. Avoid copying `node_modules` from the host.
7. Use multi-stage builds where beneficial.
8. Run applications as a non-root user.
9. Avoid storing secrets inside Docker images.
10. Keep dependencies updated.

---

## 12. Practical Tasks

- [ ] Create a Node.js application.
- [ ] Create package.json.
- [ ] Generate package-lock.json.
- [ ] Write a Dockerfile.
- [ ] Create .dockerignore.
- [ ] Build a Docker image.
- [ ] Run the Node.js container.
- [ ] Access the application through localhost.
- [ ] Test the health endpoint.
- [ ] Check container logs.
- [ ] Stop and remove the container.

---

## 13. Interview Questions

1. How do you containerize a Node.js application?
2. What is the purpose of package.json?
3. What is package-lock.json?
4. What is the difference between npm install and npm ci?
5. Why do we use node:alpine?
6. What is the purpose of WORKDIR?
7. Why should node_modules be included in .dockerignore?
8. How do you optimize a Node.js Docker image?
9. Why should applications listen on 0.0.0.0 inside Docker?
10. How do you debug a Node.js container?

---

## 14. Conclusion

Docker simplifies Node.js application deployment by packaging the application and its dependencies into portable containers.

Understanding Node.js Dockerfiles is useful for backend development, microservices, CI/CD pipelines, and cloud-native deployments.
```

**Next file:** `04-Dockerfile/node-dockerfile/Dockerfile`

Say **Next** when ready! 🚀