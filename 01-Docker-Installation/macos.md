# Install Docker Desktop on macOS

> Check Docker's current macOS and processor requirements before installing.

## 1. Identify your Mac processor

```bash
uname -m
```

Common output:
- `arm64` — Apple silicon
- `x86_64` — Intel

## 2. Install Docker Desktop

1. Open the [official Docker Desktop for Mac guide](https://docs.docker.com/desktop/setup/install/mac-install/).
2. Download the installer appropriate for your Mac.
3. Open the downloaded installer and follow Docker's installation steps.
4. Launch Docker Desktop.
5. Wait until Docker reports that the engine is running.

## 3. Verify from Terminal

```bash
docker --version
docker compose version
docker info
docker run --rm hello-world
```

If the CLI cannot connect to the daemon, open Docker Desktop and wait for startup to finish.

## 4. Troubleshooting

- Confirm that your macOS version and processor are supported.
- Make sure Docker Desktop has completed startup.
- Review the [Docker Desktop troubleshooting guide](https://docs.docker.com/desktop/troubleshoot/overview/).

## Notes

Docker Desktop is the recommended starting point for most macOS developers. Use only Docker's official download and documentation.
