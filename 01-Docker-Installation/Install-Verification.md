# Installation Verification

Use this checklist after installing Docker. Commands below work in PowerShell, Windows Terminal, macOS Terminal, and Linux shells unless noted.

## 1. Check the client versions

```bash
docker --version
docker compose version
```

These commands confirm that the Docker CLI and Compose plugin are available. They do not, by themselves, prove that the Docker Engine is running.

## 2. Check the Docker Engine connection

```bash
docker info
```

A successful response displays information about the client/server environment, storage driver, containers, images, and runtime.

If you see an error similar to `Cannot connect to the Docker daemon`:

- Windows/macOS: open Docker Desktop and wait until the engine is running.
- Ubuntu/Linux: check `sudo systemctl status docker`.
- Confirm that the active Docker context is the one you intend to use:

```bash
docker context ls
docker context show
```

## 3. Run the hello-world test

```bash
docker run --rm hello-world
```

Expected result: Docker downloads the small `hello-world` image if it is not already present, creates a container, prints a success message, and removes the stopped container because of `--rm`.

## 4. Run a web-server test

Start NGINX:

```bash
docker run -d --name toolkit-nginx -p 8080:80 nginx:alpine
```

Open this URL in your browser:

http://localhost:8080

You should see the NGINX welcome page.

Check the running container:

```bash
docker ps
docker logs toolkit-nginx
```

Stop and remove the test container:

```bash
docker stop toolkit-nginx
docker rm toolkit-nginx
```

## 5. Optional: verify Compose

Create a file named `compose.yaml` in a temporary test folder:

```yaml
services:
  web:
    image: nginx:alpine
    ports:
      - "8081:80"
```

Start it:

```bash
docker compose up -d
docker compose ps
```

Open http://localhost:8081, then clean up:

```bash
docker compose down
```

## Verification checklist

- [ ] `docker --version` prints a version.
- [ ] `docker compose version` prints a version.
- [ ] `docker info` returns server information.
- [ ] `docker run --rm hello-world` completes successfully.
- [ ] The NGINX test page opens at `http://localhost:8080`.
- [ ] The test container was stopped and removed.

## Cleanup and safety

The commands in this guide remove only the named test container or the Compose project created here. Avoid broad cleanup commands such as `docker system prune --volumes` unless you have checked exactly what data they will delete.
