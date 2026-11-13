# Install Docker on Windows

> These instructions are for supported Windows 10/11 systems. Check Docker's current requirements before installing.

## 1. Check prerequisites

- A supported Windows version and hardware virtualization enabled in BIOS/UEFI.
- WSL 2 available if you plan to use the WSL 2 backend.
- Administrator access to install software.

Check WSL from PowerShell:

```powershell
wsl --status
```

If WSL is not installed or needs updating, run PowerShell as Administrator:

```powershell
wsl --install
wsl --update
```

Restart Windows if prompted. For the latest details, see [Microsoft's WSL installation guide](https://learn.microsoft.com/windows/wsl/install).

## 2. Install Docker Desktop

1. Open the [official Docker Desktop for Windows guide](https://docs.docker.com/desktop/setup/install/windows-install/).
2. Download the installer from Docker's official download page.
3. Run the installer and follow its prompts. Select the WSL 2 backend when appropriate for your setup.
4. Start Docker Desktop.
5. Wait until Docker Desktop reports that the engine is running.

Do not download installers from unofficial websites.

## 3. Verify from PowerShell

```powershell
docker --version
docker compose version
docker info
docker run --rm hello-world
```

If `docker info` reports that it cannot connect to the daemon, start Docker Desktop and retry.

## 4. Common checks

```powershell
wsl --status
wsl --list --verbose
```

If Docker Desktop does not start, check virtualization, WSL status, Windows updates, and the [Docker Desktop troubleshooting guide](https://docs.docker.com/desktop/troubleshoot/overview/).

## Notes

- Docker commands can be run from PowerShell, Windows Terminal, or a configured WSL distribution.
- Keep Docker Desktop updated.
- The exact supported Windows editions and requirements can change; use the official guide as the source of truth.
