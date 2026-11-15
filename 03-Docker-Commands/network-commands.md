
# Docker Network Commands

## 1. Introduction

Docker networking allows containers to communicate with each other, the host machine, and external networks.

Docker provides different network drivers to support different communication requirements.

This guide covers essential Docker network commands with practical examples.

---

## 2. Listing Docker Networks

### List All Networks

```bash
docker network ls
```

### Display Network Details

```bash
docker network inspect bridge
```

### Display Network IDs

```bash
docker network ls -q
```

### Filter Networks by Driver

```bash
docker network ls --filter driver=bridge
```

---

## 3. Creating Docker Networks

### Create a Bridge Network

```bash
docker network create mynetwork
```

### Create a Network with a Specific Driver

```bash
docker network create --driver bridge mynetwork
```

### Create a Network with a Subnet

```bash
docker network create \
  --subnet 172.20.0.0/16 \
  mynetwork
```

### Create a Network with a Gateway

```bash
docker network create \
  --subnet 172.20.0.0/16 \
  --gateway 172.20.0.1 \
  mynetwork
```

### Create an Internal Network

```bash
docker network create \
  --internal \
  internal-network
```

An internal network restricts external connectivity through that network.

---

## 4. Connecting Containers to Networks

### Run a Container on a Specific Network

```bash
docker run -d \
  --name web \
  --network mynetwork \
  nginx
```

### Connect an Existing Container

```bash
docker network connect mynetwork web
```

### Connect a Container with a Custom IP

```bash
docker network connect \
  --ip 172.20.0.10 \
  mynetwork web
```

Note: The requested IP must belong to the network subnet and must be available.

### Connect with an Alias

```bash
docker network connect \
  --alias webserver \
  mynetwork web
```

---

## 5. Disconnecting Containers from Networks

### Disconnect a Container

```bash
docker network disconnect mynetwork web
```

### Force Disconnect a Container

```bash
docker network disconnect -f mynetwork web
```

---

## 6. Removing Docker Networks

### Remove a Network

```bash
docker network rm mynetwork
```

### Remove All Unused Networks

```bash
docker network prune
```

### Remove Unused Networks Without Confirmation

```bash
docker network prune -f
```

**Warning:** A network cannot normally be removed while containers are connected to it.

---

## 7. Docker Network Drivers

Docker supports different network drivers.

### Bridge Network

The default network driver for standalone Docker containers.

```bash
docker network create --driver bridge bridge-network
```

Use case:
- Communication between containers on the same Docker host.
- Isolated application environments.

### Host Network

Uses the host machine's network stack instead of providing a separate container network namespace.

```bash
docker run -d \
  --network host \
  nginx
```

Use case:
- Applications that need direct access to host networking.

Note: Host networking behaves differently across Linux, Windows, and macOS Docker environments.

### None Network

Disables normal container networking.

```bash
docker run -d \
  --network none \
  --name isolated-container \
  alpine sleep 3600
```

Use case:
- Isolated containers that do not require network connectivity.

### Overlay Network

Allows containers running on different Docker hosts to communicate through an overlay network.

```bash
docker network create \
  --driver overlay \
  my-overlay
```

Note: Overlay networking is commonly used with Docker Swarm.

### Macvlan Network

Assigns containers their own MAC addresses, allowing them to appear as physical devices on the network.

```bash
docker network create \
  -d macvlan \
  --subnet=192.168.1.0/24 \
  --gateway=192.168.1.1 \
  -o parent=eth0 \
  my-macvlan
```

Note: Replace `eth0`, subnet, and gateway with values appropriate for your network.

---

## 8. Container-to-Container Communication

Containers attached to the same user-defined bridge network can communicate using container names.

### Step 1: Create a Network

```bash
docker network create app-network
```

### Step 2: Run a Backend Container

```bash
docker run -d \
  --name backend \
  --network app-network \
  nginx
```

### Step 3: Run a Client Container

```bash
docker run --rm \
  --network app-network \
  alpine \
  ping -c 4 backend
```

The client container can resolve `backend` through Docker's embedded DNS.

---

## 9. Port Mapping Commands

### Map a Host Port to a Container Port

```bash
docker run -d \
  -p 8080:80 \
  nginx
```

### Map a Specific Host IP

```bash
docker run -d \
  -p 127.0.0.1:8080:80 \
  nginx
```

### Map a Random Host Port

```bash
docker run -d \
  -P \
  nginx
```

### Display Port Mappings

```bash
docker port <container_name>
```

---

## 10. DNS and Network Inspection

### Inspect Network Configuration

```bash
docker network inspect mynetwork
```

### Inspect Container Network Settings

```bash
docker inspect <container_name>
```

### Display Container IP Address

```bash
docker inspect \
  -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' \
  <container_name>
```

### Test Container Connectivity

```bash
docker exec -it web ping backend
```

Note: The container image must include the `ping` utility.

---

## 11. Docker Networking Practical Example

### Create a Two-Container Application Network

Step 1: Create a network.

```bash
docker network create two-tier-network
```

Step 2: Start a backend container.

```bash
docker run -d \
  --name backend \
  --network two-tier-network \
  nginx
```

Step 3: Start a client container.

```bash
docker run -d \
  --name client \
  --network two-tier-network \
  alpine sleep 3600
```

Step 4: Test communication.

```bash
docker exec client ping -c 4 backend
```

Step 5: Inspect the network.

```bash
docker network inspect two-tier-network
```

Step 6: Clean up.

```bash
docker rm -f client backend
docker network rm two-tier-network
```

---

## 12. Docker Network Commands Cheat Sheet

| Command | Description |
|---|---|
| docker network ls | List networks |
| docker network create | Create a network |
| docker network inspect | Inspect network details |
| docker network connect | Connect a container |
| docker network disconnect | Disconnect a container |
| docker network rm | Remove a network |
| docker network prune | Remove unused networks |
| docker network ls -q | List network IDs |
| docker port | Display port mappings |

---

## 13. Docker Networking Best Practices

1. Use user-defined bridge networks for application communication.
2. Avoid exposing unnecessary ports.
3. Use meaningful network names.
4. Use internal networks for isolated communication.
5. Inspect network configurations when troubleshooting.
6. Use container names instead of hardcoded IP addresses.
7. Separate frontend and backend networks when appropriate.
8. Avoid unnecessary network connections.
9. Use overlay networks for multi-host Docker Swarm applications.
10. Apply appropriate network security controls.

---

## 14. Conclusion

Docker networking enables communication between containers and external systems.

Understanding network drivers, port mapping, DNS resolution, and network management is essential for building multi-container applications and working with Docker in production environments.
