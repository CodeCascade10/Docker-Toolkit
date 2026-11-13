# Install Docker Engine on Ubuntu

> Docker's repository setup and supported Ubuntu releases can change. Follow the official guide for your Ubuntu release and CPU architecture.

## 1. Check your Ubuntu version

```bash
lsb_release -a
uname -m
```

## 2. Install Docker Engine

Follow Docker's official, maintained instructions:

[Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

The guide covers setting up Docker's apt repository, installing the Engine and CLI packages, and configuring the service. Prefer the official repository method rather than an old copied command sequence.

## 3. Verify the service

```bash
sudo systemctl status docker
sudo docker version
sudo docker info
sudo docker run --rm hello-world
```

If the service is not running, start it:

```bash
sudo systemctl start docker
```

To enable Docker to start automatically at boot:

```bash
sudo systemctl enable docker
```

## 4. Optional: use Docker without sudo

Read Docker's [Linux post-installation guide](https://docs.docker.com/engine/install/linux-postinstall/) before doing this.

**Security warning:** Membership in the `docker` group grants root-level privileges. Only add trusted users on a machine you administer.

## 5. Troubleshooting checks

```bash
systemctl is-active docker
sudo journalctl -u docker --no-pager -n 50
docker context ls
```

If you see a permission error, first verify the service is running and that your user has the intended permissions. Do not change socket permissions to `777`.
