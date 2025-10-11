# 🐳 Docker CLI Command Reference

A comprehensive cheatsheet of essential Docker commands for quick reference during development and operations.

---

## 📋 Table of Contents

- [🔧 Basic Docker Commands](#-basic-docker-commands)
- [📦 Image Management](#-image-management)
- [🏃 Container Operations](#-container-operations)
- [🎼 Docker Compose](#-docker-compose)
- [🌐 Network Management](#-network-management)
- [💾 Volume Management](#-volume-management)
- [📊 Monitoring & Debugging](#-monitoring--debugging)
- [🧹 Cleanup Commands](#-cleanup-commands)
- [🏗️ Build & Registry](#-build--registry)
- [💡 Quick Tips](#-quick-tips)

---

## 🔧 Basic Docker Commands

### System Information
```bash
# Check Docker version
docker --version
docker version

# Display system-wide information
docker info

# Show Docker disk usage
docker system df

# Display real-time events from the server
docker events
```

### Help & Documentation
```bash
# Get help for any command
docker --help
docker <command> --help

# Example: Get help for run command
docker run --help
```

---

## 📦 Image Management

### Pulling & Listing Images
```bash
# Pull an image from registry
docker pull <image>:<tag>
docker pull nginx:alpine
docker pull ubuntu:20.04

# List all local images
docker images
docker image ls

# Search for images on Docker Hub
docker search <term>
docker search nginx
```

### Building Images
```bash
# Build image from Dockerfile
docker build -t <name>:<tag> <path>
docker build -t myapp:latest .
docker build -t myapp:v1.0 ./app

# Build with build arguments
docker build --build-arg APP_VERSION=1.0 -t myapp .

# Build without cache
docker build --no-cache -t myapp .

# Build and tag multiple versions
docker build -t myapp:latest -t myapp:v1.0 .
```

### Tagging & Pushing
```bash
# Tag an image
docker tag <source> <target>
docker tag myapp:latest myuser/myapp:latest

# Push image to registry
docker push <image>:<tag>
docker push myuser/myapp:latest

# Save image to tar file
docker save <image> > <file>.tar
docker save myapp:latest > myapp.tar

# Load image from tar file
docker load < <file>.tar
docker load < myapp.tar
```

### Image Information
```bash
# Inspect image details
docker inspect <image>
docker inspect nginx:alpine

# Show image history/layers
docker history <image>
docker history nginx:alpine

# Remove images
docker rmi <image>
docker rmi nginx:alpine
docker rmi $(docker images -q)  # Remove all images
```

---

## 🏃 Container Operations

### Running Containers
```bash
# Run a container
docker run <image>
docker run nginx:alpine

# Run in detached mode (background)
docker run -d <image>
docker run -d nginx:alpine

# Run with port mapping
docker run -p <host-port>:<container-port> <image>
docker run -p 8080:80 nginx:alpine

# Run with name
docker run --name <name> <image>
docker run --name my-nginx nginx:alpine

# Run interactively
docker run -it <image> <command>
docker run -it ubuntu:20.04 bash
docker run -it alpine sh

# Run with environment variables
docker run -e VAR1=value1 -e VAR2=value2 <image>
docker run -e NODE_ENV=production node:alpine

# Run with volume mounting
docker run -v <host-path>:<container-path> <image>
docker run -v /host/data:/app/data nginx:alpine
docker run -v myvolume:/app/data nginx:alpine

# Run with working directory
docker run -w /app <image>

# Run with resource limits
docker run --memory="512m" --cpus="1.0" <image>

# Run with restart policy
docker run --restart=always <image>
docker run --restart=unless-stopped <image>
```

### Container Lifecycle
```bash
# List running containers
docker ps
docker container ls

# List all containers (including stopped)
docker ps -a
docker container ls -a

# Start a stopped container
docker start <container>
docker start my-nginx

# Stop a running container
docker stop <container>
docker stop my-nginx

# Restart a container
docker restart <container>
docker restart my-nginx

# Pause/unpause a container
docker pause <container>
docker unpause <container>

# Remove a container
docker rm <container>
docker rm my-nginx

# Remove a running container (force)
docker rm -f <container>
```

### Container Interaction
```bash
# Execute command in running container
docker exec <container> <command>
docker exec my-nginx ls -la

# Execute interactive shell
docker exec -it <container> <shell>
docker exec -it my-nginx sh
docker exec -it my-nginx bash

# Copy files between host and container
docker cp <src> <dest>
docker cp file.txt my-nginx:/app/
docker cp my-nginx:/app/logs ./logs

# Attach to running container
docker attach <container>

# View container logs
docker logs <container>
docker logs -f <container>  # Follow logs
docker logs --tail 50 <container>  # Last 50 lines
```

---

## 🎼 Docker Compose

### Basic Operations
```bash
# Start services (detached)
docker-compose up -d

# Start services (foreground)
docker-compose up

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v

# Restart services
docker-compose restart

# Build services
docker-compose build

# Build and start
docker-compose up --build
```

### Service Management
```bash
# List running services
docker-compose ps

# View service logs
docker-compose logs
docker-compose logs <service>
docker-compose logs -f <service>  # Follow logs

# Execute command in service
docker-compose exec <service> <command>
docker-compose exec web bash
docker-compose exec db psql -U postgres

# Scale services
docker-compose up -d --scale <service>=<count>
docker-compose up -d --scale web=3

# Pull latest images
docker-compose pull

# Validate compose file
docker-compose config
```

---

## 🌐 Network Management

### Basic Network Operations
```bash
# List networks
docker network ls

# Create network
docker network create <network>
docker network create my-network
docker network create --driver bridge my-bridge

# Inspect network
docker network inspect <network>
docker network inspect bridge

# Connect container to network
docker network connect <network> <container>
docker network connect my-network my-container

# Disconnect container from network
docker network disconnect <network> <container>

# Remove network
docker network rm <network>
docker network rm my-network

# Remove unused networks
docker network prune
```

### Network Types
```bash
# Create bridge network (default)
docker network create --driver bridge my-bridge

# Create overlay network (for swarm)
docker network create --driver overlay my-overlay

# Create host network (shares host networking)
docker run --network host <image>

# Create none network (no networking)
docker run --network none <image>
```

---

## 💾 Volume Management

### Volume Operations
```bash
# List volumes
docker volume ls

# Create volume
docker volume create <volume>
docker volume create my-volume

# Inspect volume
docker volume inspect <volume>
docker volume inspect my-volume

# Remove volume
docker volume rm <volume>
docker volume rm my-volume

# Remove unused volumes
docker volume prune

# Remove all volumes
docker volume rm $(docker volume ls -q)
```

### Volume Usage
```bash
# Mount named volume
docker run -v <volume>:<container-path> <image>
docker run -v my-volume:/app/data nginx

# Mount bind volume (host directory)
docker run -v <host-path>:<container-path> <image>
docker run -v /host/data:/app/data nginx

# Mount read-only volume
docker run -v <volume>:<container-path>:ro <image>
docker run -v my-volume:/app/data:ro nginx

# Create volume with specific driver
docker volume create --driver local my-local-volume
```

---

## 📊 Monitoring & Debugging

### Container Monitoring
```bash
# View container resource usage
docker stats
docker stats <container>
docker stats --no-stream  # One-time snapshot

# View container processes
docker top <container>

# Inspect container details
docker inspect <container>

# View container logs
docker logs <container>
docker logs -f <container>          # Follow logs
docker logs --since 2h <container>  # Logs since 2 hours ago
docker logs --tail 100 <container>  # Last 100 lines
```

### System Monitoring
```bash
# Show system events
docker events
docker events --since 2h

# Show disk usage
docker system df
docker system df -v  # Verbose output

# Show system information
docker info

# View Docker daemon logs (varies by OS)
# Linux: journalctl -u docker.service
# macOS: ~/Library/Containers/com.docker.docker/Data/log/
```

### Health Checks
```bash
# Run container with health check
docker run --health-cmd="curl -f http://localhost/" \
           --health-interval=30s \
           --health-timeout=3s \
           --health-retries=3 \
           nginx

# Check container health
docker inspect --format='{{.State.Health.Status}}' <container>
```

---

## 🧹 Cleanup Commands

### Remove Resources
```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune
docker image prune -a  # Remove all unused images

# Remove unused volumes
docker volume prune

# Remove unused networks
docker network prune

# Remove all unused resources
docker system prune
docker system prune -a  # More aggressive cleanup
docker system prune -a --volumes  # Include volumes
```

### Force Cleanup
```bash
# Stop all running containers
docker stop $(docker ps -q)

# Remove all containers
docker rm $(docker ps -aq)

# Remove all images
docker rmi $(docker images -q)

# Nuclear option - remove everything
docker system prune -a --volumes -f
```

### Selective Cleanup
```bash
# Remove containers older than 24 hours
docker container prune --filter "until=24h"

# Remove images not used in last 24 hours
docker image prune -a --filter "until=24h"

# Remove containers with specific label
docker container prune --filter "label=temp"

# Remove exited containers
docker rm $(docker ps -aq -f status=exited)
```

---

## 🏗️ Build & Registry

### Advanced Building
```bash
# Build with specific Dockerfile
docker build -f Dockerfile.prod -t myapp .

# Build with build context from URL
docker build -t myapp https://github.com/user/repo.git

# Multi-stage build target
docker build --target production -t myapp .

# Build with secrets (BuildKit)
docker build --secret id=mypassword,src=./password.txt .

# Build with cache from registry
docker build --cache-from myapp:latest -t myapp .
```

### Registry Operations
```bash
# Login to registry
docker login
docker login registry.example.com

# Logout from registry
docker logout
docker logout registry.example.com

# Tag for private registry
docker tag myapp:latest registry.example.com/myapp:latest

# Push to private registry
docker push registry.example.com/myapp:latest

# Pull from private registry
docker pull registry.example.com/myapp:latest
```

---

## 💡 Quick Tips

### Useful Aliases
```bash
# Add these to your ~/.bashrc or ~/.zshrc
alias dps='docker ps'
alias dpsa='docker ps -a'
alias di='docker images'
alias dex='docker exec -it'
alias dlog='docker logs -f'
alias dstop='docker stop $(docker ps -q)'
alias drm='docker rm $(docker ps -aq)'
alias dcp='docker-compose'
alias dcup='docker-compose up -d'
alias dcdown='docker-compose down'
```

### Format Output
```bash
# Custom format for ps
docker ps --format "table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}"

# Custom format for images
docker images --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}"

# JSON output
docker inspect <container> --format='{{json .State}}'

# Get container IP
docker inspect <container> --format='{{.NetworkSettings.IPAddress}}'

# Get container ports
docker inspect <container> --format='{{.NetworkSettings.Ports}}'
```

### Filtering
```bash
# Filter containers by status
docker ps -f status=running
docker ps -f status=exited

# Filter by name
docker ps -f name=web

# Filter by label
docker ps -f label=environment=production

# Filter images by reference
docker images -f reference="nginx:*"

# Filter by dangling
docker images -f dangling=true
```

### Environment Variables
```bash
# Set Docker host
export DOCKER_HOST=tcp://192.168.1.100:2376

# Enable BuildKit (faster builds)
export DOCKER_BUILDKIT=1

# Compose file path
export COMPOSE_FILE=docker-compose.prod.yml

# Compose project name
export COMPOSE_PROJECT_NAME=myproject
```

---

## 🚨 Emergency Commands

### When Things Go Wrong
```bash
# Kill all running containers
docker kill $(docker ps -q)

# Remove everything (DANGER!)
docker system prune -a --volumes -f
docker volume rm $(docker volume ls -q) 2>/dev/null
docker network rm $(docker network ls -q) 2>/dev/null

# Reset Docker Desktop (macOS/Windows)
# Go to Docker Desktop -> Troubleshoot -> Reset to factory defaults

# Check Docker daemon status
# Linux: systemctl status docker
# macOS: Docker Desktop app status
# Windows: Docker Desktop app status

# View Docker daemon logs
# Linux: journalctl -u docker.service
# macOS/Windows: Docker Desktop -> Troubleshoot -> Get Support
```

---

## 📚 Additional Resources

- **Official Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Docker Hub**: [https://hub.docker.com/](https://hub.docker.com/)
- **Dockerfile Reference**: [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
- **Compose File Reference**: [https://docs.docker.com/compose/compose-file/](https://docs.docker.com/compose/compose-file/)
- **Best Practices**: [https://docs.docker.com/develop/dev-best-practices/](https://docs.docker.com/develop/dev-best-practices/)

---
