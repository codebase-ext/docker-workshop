# 🐳 Docker & Containers Workshop - Hands-On Guide

## 📋 Workshop Overview
**Duration:** 2 Hours Hands-On Session  
**Prerequisites:** Docker Desktop installed on your machine  
**Goal:** Zero to "Ya, I know Docker - It's simple...Let me show you" Knowledge

---

## 📋 Prerequisites & Docker Installation

### 🔧 System Requirements
- **Operating System:** Windows 10/11, macOS 10.15+, or Linux (Ubuntu 18.04+, CentOS 7+)
- **RAM:** Minimum 4GB (8GB recommended)
- **Disk Space:** At least 10GB free space
- **Internet Connection:** Required for downloading Docker images

### 🐳 Docker Installation Guide

#### **For Windows:**
1. **Download Docker Desktop for Windows**
   - Visit: [https://docs.docker.com/desktop/install/windows-install/](https://docs.docker.com/desktop/install/windows-install/)
   - Click "Download Docker Desktop for Windows"

2. **System Requirements:**
   - Windows 10 64-bit: Pro, Enterprise, or Education (Build 19041 or higher)
   - OR Windows 11 64-bit
   - WSL 2 feature enabled
   - Hyper-V and Containers Windows features enabled

3. **Installation Steps:**
   ```bash
   # Run the downloaded Docker Desktop Installer.exe
   # Follow the installation wizard
   # Restart your computer when prompted
   # Start Docker Desktop from Start menu
   ```

4. **Enable WSL 2 (if not already enabled):**
   ```powershell
   # Run in PowerShell as Administrator
   dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
   dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
   ```

#### **For macOS:**
1. **Download Docker Desktop for Mac**
   - Intel Macs: [https://docs.docker.com/desktop/install/mac-install/](https://docs.docker.com/desktop/install/mac-install/)
   - Apple Silicon (M1/M2): Same link, choose Apple Silicon version

2. **System Requirements:**
   - macOS 10.15 (Catalina) or newer
   - 4GB RAM minimum

3. **Installation Steps:**
   ```bash
   # Download Docker.dmg
   # Double-click Docker.dmg to open installer
   # Drag Docker icon to Applications folder
   # Launch Docker from Applications
   # Grant permissions when prompted
   ```

#### **For Linux (Ubuntu/Debian):**
1. **Official Installation Method:**
   ```bash
   # Update package index
   sudo apt-get update
   
   # Install prerequisites
   sudo apt-get install ca-certificates curl gnupg lsb-release
   
   # Add Docker's official GPG key
   sudo mkdir -p /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   
   # Set up repository
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   
   # Install Docker Engine
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
   
   # Add your user to docker group
   sudo usermod -aG docker $USER
   
   # Log out and back in, or run:
   newgrp docker
   ```

2. **For other Linux distributions:**
   - CentOS/RHEL: [https://docs.docker.com/engine/install/centos/](https://docs.docker.com/engine/install/centos/)
   - Fedora: [https://docs.docker.com/engine/install/fedora/](https://docs.docker.com/engine/install/fedora/)
   - Arch Linux: [https://docs.docker.com/engine/install/archlinux/](https://docs.docker.com/engine/install/archlinux/)

### 🔍 Verify Installation
After installation, verify Docker is working:

```bash
# Check Docker version
docker --version

# Check Docker Compose version  
docker compose version

# Test Docker installation
docker run hello-world

# Check Docker system info
docker info
```

**Expected Output:**
```
Docker version 28.x.x, build xxxxxxx
Docker Compose version v2.x.x
Hello from Docker! (from hello-world test)
```

**💡 Version Note:** This workshop is designed for Docker 28.x.x (the latest version as of October 2025). Most features will work with Docker 20.x.x or newer, but some advanced features may require the latest version.

### 🚨 Troubleshooting Installation Issues

#### **Common Windows Issues:**
- **"WSL 2 installation is incomplete"**: Install WSL 2 Linux kernel update package
- **"Hardware assisted virtualization and data execution protection must be enabled"**: Enable Hyper-V in Windows features
- **Permission denied**: Make sure you're in the "docker-users" group

#### **Common macOS Issues:**
- **"Docker Desktop requires macOS 10.15 or newer"**: Update your macOS version
- **Permission denied**: Grant necessary permissions in System Preferences > Security & Privacy

#### **Common Linux Issues:**
- **"Permission denied"**: Make sure your user is in the docker group: `sudo usermod -aG docker $USER`
- **"Cannot connect to Docker daemon"**: Start Docker service: `sudo systemctl start docker`
- **Package conflicts**: Remove old Docker versions first: `sudo apt-get remove docker docker-engine docker.io`

### 📚 Additional Resources
- **Official Docker Documentation**: [https://docs.docker.com/](https://docs.docker.com/)
- **Docker Hub (Image Registry)**: [https://hub.docker.com/](https://hub.docker.com/)
- **Docker Desktop Manual**: [https://docs.docker.com/desktop/](https://docs.docker.com/desktop/)
- **Docker Learning Resources**: [https://docs.docker.com/get-started/](https://docs.docker.com/get-started/)
- **Community Forums**: [https://forums.docker.com/](https://forums.docker.com/)

### ⚠️ Important Notes Before Starting Workshop
1. **Ensure Docker Desktop is running** before starting the workshop
2. **Test the hello-world container** to verify everything works
3. **Have a stable internet connection** for downloading images
4. **Close resource-intensive applications** to free up system resources
5. **Have administrator/sudo access** in case additional setup is needed

### 🌐 Optional: Docker Hub Account Setup
For sharing your images with the community, you can create a Docker Hub account. This is optional for the main workshop but recommended for real-world usage.

**👉 Complete Docker Hub Setup Guide:** [docker-hub.md](docker-hub.md)

This comprehensive guide covers:
- Creating a Docker Hub account
- Building and publishing images
- Sharing with the community
- Best practices and security
- Advanced tagging strategies

---

## 🚀 Part 1: Environment Setup & Verification (15 minutes)

### Step 1: 🔍 Verify Docker Installation
*Confirm Docker is properly installed and running on your system*

**If you haven't installed Docker yet, please complete the Prerequisites section above first.**

Open your terminal/command prompt:

**For Mac:**
- Press `Cmd + Space`, type "Terminal", press Enter
- Or open Applications > Utilities > Terminal

**For Windows:**
- Press `Windows + R`, type "cmd", press Enter
- Or press `Windows + X`, select "Command Prompt" or "PowerShell"
- Or search "cmd" in Start menu

Run the following command:
```bash
docker --version
```

Expected output format:
```
Docker version 28.x.x, build xxxxxxx
```

**If you get an error:**
- Make sure Docker Desktop is running (check system tray/menu bar)
- On Windows: Ensure WSL 2 is properly configured
- On Linux: Check if Docker service is running: `sudo systemctl status docker`
- Refer to the installation troubleshooting section above











### Step 2: ⚙️ Check Docker Service Status
*Ensure Docker daemon is running and accessible*

```bash
docker info
```

Verify that Docker daemon is running and you can see system information.











### Step 3: 👋 Test Docker with Hello World
*Run your first container to verify everything works*

```bash
docker run hello-world
```

Expected output should include:
```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```











### Step 4: 📁 Create Workshop Directory Structure
*Set up organized folders for all workshop exercises*

**For Mac/Linux:**
```bash
mkdir workshop
cd workshop
mkdir flask-app angular-app full-stack-app
```

**For Windows (Command Prompt):**
```cmd
mkdir workshop
cd workshop
mkdir flask-app angular-app full-stack-app
```

**For Windows (PowerShell):**
```powershell
mkdir workshop
cd workshop
mkdir flask-app, angular-app, full-stack-app
```

Verify directory structure:

**For Mac/Linux:**
```bash
ls -la
```

**For Windows:**
```cmd
dir
```











---

## 🔧 Part 2: Docker Fundamentals (30 minutes)

### Step 5: 📦 Working with Docker Images
*Learn to manage and download Docker images*

List available images:
```bash
docker images
```

Pull a basic image:
```bash
docker pull nginx:alpine
```

Check images again:
```bash
docker images
```











### Step 6: 🏃 Running Your First Container
*Launch and test your first web server container*

Run nginx container:
```bash
docker run -d -p 8080:80 --name my-nginx nginx:alpine
```

Verify container is running:
```bash
docker ps
```

Test the container:
```bash
curl http://localhost:8080
```

Or open browser to `http://localhost:8080`











### Step 7: 🎛️ Container Management Commands
*Master the essential container lifecycle operations*

Stop the container:
```bash
docker stop my-nginx
```

Start the container:
```bash
docker start my-nginx
```

Remove the container:
```bash
docker rm -f my-nginx
```











### Step 8: 🔍 Exploring Container Internals
*Peek inside a running container to understand its environment*

Run an interactive container:
```bash
docker run -it alpine:latest sh
```

Inside the container, run:
```bash
ls -la
cat /etc/os-release
exit
```











---

## 🏗️ Part 3: Building Custom Docker Images (20 minutes)

### Step 9: 📝 Create a Simple Dockerfile
*Build your first custom Docker image from scratch*

**For Mac/Linux:**
```bash
cd workshop
mkdir simple-app
cd simple-app
```

**For Windows:**
```cmd
cd workshop
mkdir simple-app
cd simple-app
```

Create a file named `Dockerfile`:

**💡 Creating Files:**
- **Visual Studio Code**: `code Dockerfile` (if installed) or create via File > New File
- **Windows Notepad**: Right-click > New > Text Document, rename to `Dockerfile` (remove .txt extension)
- **Mac TextEdit**: File > New, then save as `Dockerfile` (Format > Make Plain Text)
- **Terminal/Command Prompt**: Use `touch Dockerfile` (Mac/Linux) or `type nul > Dockerfile` (Windows)

**⚠️ Important:** Make sure there's no file extension (like .txt) - the file should be named exactly `Dockerfile`

```dockerfile
FROM alpine:latest
RUN apk add --no-cache curl
WORKDIR /app
COPY . .
CMD ["echo", "Hello from Custom Docker Image!"]
```

Create a sample file:

**For Mac/Linux:**
```bash
echo "This is a sample file" > sample.txt
```

**For Windows (Command Prompt):**
```cmd
echo This is a sample file > sample.txt
```

**For Windows (PowerShell):**
```powershell
"This is a sample file" | Out-File -FilePath sample.txt -Encoding UTF8
```











### Step 10: 🔨 Build the Image
*Compile your Dockerfile into a reusable Docker image*

```bash
docker build -t my-custom-app .
```

Verify the image was created:
```bash
docker images | grep my-custom-app
```











### Step 11: 🚀 Run the Custom Image
*Test your newly created custom image*

```bash
docker run my-custom-app
```

Run interactively to explore:
```bash
docker run -it my-custom-app sh
```

Inside container:
```bash
ls -la
cat sample.txt
exit
```











---

## 🎼 Part 4: Docker Compose Fundamentals (25 minutes)

### Step 12: 🎵 Introduction to Docker Compose
*Learn to orchestrate multiple containers with ease*

**For Mac/Linux:**
```bash
cd ../
mkdir compose-basics
cd compose-basics
```

**For Windows:**
```cmd
cd ..
mkdir compose-basics
cd compose-basics
```











### Step 13: 📄 Basic Docker Compose File
*Create your first multi-container configuration*

Create `docker-compose.yml`:

**💡 File Creation Tip:** 
- Make sure to save the file as `docker-compose.yml` (with .yml extension)
- Use a text editor that preserves indentation (YAML is sensitive to spacing)
- Visual Studio Code with YAML extension is recommended

```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
```

**What this does:**
- `version: '3.8'`: Specifies Docker Compose file format version
- `services:`: Defines the containers to be created
- `web:`: Name of our service
- `image: nginx:alpine`: Uses the nginx alpine image
- `ports:`: Maps host port 8080 to container port 80











### Step 14: ▶️ Run with Docker Compose
*Launch your first orchestrated service*

```bash
docker-compose up -d
```

Check running services:
```bash
docker-compose ps
```

Test the service:
```bash
curl http://localhost:8080
```

Stop the services:
```bash
docker-compose down
```











### Step 15: 🔗 Multi-Service Docker Compose
*Connect multiple services together*

Update `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    depends_on:
      - redis
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

**New components explained:**
- `redis:`: Second service definition
- `depends_on:`: Ensures redis starts before web
- `6379:6379`: Redis default port mapping











### Step 16: 🚀 Advanced Compose Features
*Add volumes, networks, and environment variables*

Create enhanced `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    environment:
      - ENV=development
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - redis
    networks:
      - app-network
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data
    networks:
      - app-network

volumes:
  redis-data:

networks:
  app-network:
    driver: bridge
```

**New features explained:**
- `environment:`: Sets environment variables
- `volumes:`: Mounts local directory to container
- `networks:`: Creates custom network for service communication
- `volumes:` (top-level): Defines named volumes for data persistence











### Step 17: Test Volume Mounting

Create HTML directory and file:

**For Mac/Linux:**
```bash
mkdir html
echo "<h1>Hello from Docker Compose!</h1>" > html/index.html
```

**For Windows (Command Prompt):**
```cmd
mkdir html
echo ^<h1^>Hello from Docker Compose!^</h1^> > html\index.html
```

**For Windows (PowerShell):**
```powershell
mkdir html
"<h1>Hello from Docker Compose!</h1>" | Out-File -FilePath html\index.html -Encoding UTF8
```

Start services:
```bash
docker-compose up -d
```

Test the custom HTML:
```bash
curl http://localhost:8080
```

Clean up:
```bash
docker-compose down
```











---

## 🎯 Part 5: Advanced Docker Concepts (20 minutes)

### Step 18: 🌐 Docker Networking
*Create custom networks for container communication*

Create custom network:
```bash
docker network create my-network
```

List networks:
```bash
docker network ls
```

Run containers on custom network:
```bash
docker run -d --name app1 --network my-network nginx:alpine
docker run -d --name app2 --network my-network redis:alpine
```

Test network connectivity:
```bash
docker exec app1 ping app2
```











### Step 19: 💾 Docker Volumes
*Manage persistent data storage for containers*

Create named volume:
```bash
docker volume create my-data
```

List volumes:
```bash
docker volume ls
```

Use volume in container:
```bash
docker run -d -v my-data:/data --name data-container alpine sleep 1000
```

Add data to volume:
```bash
docker exec data-container sh -c "echo 'Persistent data' > /data/test.txt"
```

Verify data persistence:
```bash
docker rm -f data-container
docker run -v my-data:/data alpine cat /data/test.txt
```











### Step 20: ⚡ Docker Resource Management
*Control CPU and memory usage of containers*

Run container with resource limits:
```bash
docker run -d --name limited-nginx --memory="100m" --cpus="0.5" nginx:alpine
```

**Note:** If the above command fails, try the alternative syntax:
```bash
# Alternative for older Docker versions
docker run -d --name limited-nginx -m 100m --cpu-shares=512 nginx:alpine
```

Check resource usage:
```bash
docker stats limited-nginx --no-stream
```

View continuous monitoring (stop with Ctrl+C):
```bash
docker stats limited-nginx
```

Clean up:
```bash
docker rm -f limited-nginx
```











---

## 📦 Part 6: Local Image Management & Distribution (15 minutes)

### Step 21: 🏷️ Local Image Tagging and Versioning
*Learn to version and organize your custom images locally*

Tag your custom image with multiple versions:
```bash
cd ../simple-app
docker tag my-custom-app:latest my-custom-app:v1.0
docker tag my-custom-app:latest my-custom-app:stable
```

View all tags:
```bash
docker images | grep my-custom-app
```

**Tagging Best Practices:**
- Use semantic versioning: `v1.0.0`, `v1.1.0`, `v2.0.0`
- Include environment tags: `dev`, `staging`, `production`
- Always maintain a `latest` tag for the current stable version
- Use descriptive tags: `stable`, `beta`, `experimental`











### Step 22: 🌐 Docker Hub Integration (Optional)
*Share your images with the global community*

**For sharing images with others, complete the Docker Hub guide:**

👉 **[Docker Hub Setup & Publishing Guide](docker-hub.md)**

This comprehensive guide covers:
- ✅ Creating a Docker Hub account
- ✅ Publishing images to the community
- ✅ Best practices for documentation
- ✅ Security and tagging strategies
- ✅ Community engagement

**Quick Docker Hub Commands (after setup):**
```bash
# Login to Docker Hub
docker login

# Tag for Docker Hub (replace YOUR-USERNAME)
docker tag my-custom-app:latest YOUR-USERNAME/my-custom-app:latest

# Push to Docker Hub
docker push YOUR-USERNAME/my-custom-app:latest
```

**Skip this step if you prefer to continue with local development only.**

**Skip this step if you prefer to continue with local development only.**











### Step 23: 💿 Offline Image Distribution
*Export and import Docker images for offline distribution*

**When to use:** Sharing images without internet access or private networks

Save image to file:

**For Mac/Linux:**
```bash
docker save my-custom-app:v1.0 > my-app.tar
```

**For Windows:**
```cmd
docker save my-custom-app:v1.0 -o my-app.tar
```

**Check file size:**
```bash
ls -lh my-app.tar  # Mac/Linux
dir my-app.tar     # Windows
```

Remove image to test loading:
```bash
docker rmi my-custom-app:v1.0
```

Load image back:

**For Mac/Linux:**
```bash
docker load < my-app.tar
```

**For Windows:**
```cmd
docker load -i my-app.tar
```

Verify:
```bash
docker images | grep my-custom-app
```

**💡 Use Cases for Image Files:**
- Offline environments without internet access
- Air-gapped networks for security
- Sharing images via physical media
- Backup and archival purposes











---

## 🎯 Part 7: Practical Examples

### 📚 Example Applications

The following practical examples are available as separate exercises. Complete them in order for the best learning experience:

1. **🐍 Flask Application** 
   - **File:** `flask.md` (in this repository)
   - **What you'll learn:** Simple "Hello World" Flask web application, Dockerfile creation and image building, Container deployment and testing
   - **Duration:** ~20 minutes
   - **Prerequisites:** Complete Parts 1-3 of this workshop

2. **🅰️ Angular Application** 
   - **File:** `angular.md` (in this repository)  
   - **What you'll learn:** Modern Angular single-page application, Multi-stage Docker build, Nginx serving static files
   - **Duration:** ~30 minutes
   - **Prerequisites:** Complete Flask example first

3. **🚀 Full-Stack Integration** 
   - **File:** `angular-flask.md` (in this repository)
   - **What you'll learn:** Complete application with Angular frontend and Flask backend, Docker Compose orchestration, Inter-service communication, Database integration
   - **Duration:** ~45 minutes
   - **Prerequisites:** Complete both Flask and Angular examples

4. **🌐 Docker Hub Publishing** 
   - **File:** `docker-hub.md` (in this repository)
   - **What you'll learn:** Create Docker Hub account, publish images, share with community, professional workflows
   - **Duration:** ~30 minutes
   - **Prerequisites:** Complete at least one application example above

**How to use these examples:**
1. Open the respective `.md` file in your text editor
2. Follow the step-by-step instructions
3. Run the commands in your terminal from the workshop directory
4. Test each step before proceeding to the next

---

## 🧹 Workshop Cleanup

### 🗑️ Remove All Workshop Resources
*Clean up your system after the workshop*

```bash
# Stop all running containers (ignore errors if none running)
docker stop $(docker ps -q) 2>/dev/null || true

# Remove all containers (ignore errors if none exist)
docker rm $(docker ps -aq) 2>/dev/null || true

# Remove custom images (ignore errors if images don't exist)
docker rmi my-custom-app:latest 2>/dev/null || true
docker rmi my-custom-app:v1.0 2>/dev/null || true

# Remove volumes (ignore errors if volumes don't exist)
docker volume rm my-data 2>/dev/null || true

# Remove networks (ignore errors if networks don't exist)
docker network rm my-network 2>/dev/null || true

# Clean up unused resources
docker system prune -f

# Remove any remaining workshop files:

**For Mac/Linux:**
```bash
rm -f my-app.tar
```

**For Windows:**
```cmd
del my-app.tar
```

---

## 🔧 Troubleshooting Common Issues

### **Problem: "docker: command not found"**
**Solution:** 
- Ensure Docker Desktop is installed and running
- Restart your terminal after installation
- On Linux, add your user to the docker group: `sudo usermod -aG docker $USER`

### **Problem: "Cannot connect to the Docker daemon"**
**Solution:**
- Start Docker Desktop application
- Check if Docker service is running: `docker version`
- On Linux: `sudo systemctl start docker`

### **Problem: "Port already in use"**
**Solution:**

**For Mac/Linux:**
- Check what's using the port: `lsof -i :8080`
- Use a different port: `-p 8081:80` instead of `-p 8080:80`
- Stop conflicting containers: `docker ps` then `docker stop <container-name>`

**For Windows:**
- Check what's using the port: `netstat -ano | findstr :8080`
- Use a different port: `-p 8081:80` instead of `-p 8080:80`
- Stop conflicting containers: `docker ps` then `docker stop <container-name>`

### **Problem: Container exits immediately**
**Solution:**
- Check container logs: `docker logs <container-name>`
- Run interactively to debug: `docker run -it <image-name> sh`
- Verify Dockerfile syntax and commands

### **Problem: "No space left on device"**
**Solution:**
- Clean up Docker resources: `docker system prune -a`
- Remove unused volumes: `docker volume prune`
- Remove unused images: `docker image prune -a`

### **Need Help?**
- Check Docker logs: `docker logs <container-name>`
- Inspect container details: `docker inspect <container-name>`
- View resource usage: `docker stats`
- Get help for commands: `docker <command> --help`

---

## 🚀 Next Steps

1. 🌐 **Complete the Docker Hub Guide** ([docker-hub.md](docker-hub.md)) to learn image sharing
2. 🐝 **Learn about Docker Swarm** for orchestration
3. ☸️ **Investigate Kubernetes** for production deployments
4. 💻 **Practice with more complex applications**
5. 🔄 **Implement CI/CD pipelines** with Docker
6. 🏢 **Set up private registries** for enterprise use
7. 🛡️ **Learn Docker security** best practices
8. 📊 **Monitor containerized applications** with tools like Prometheus and Grafana

---

**🎉 Workshop Complete!** 

You now have hands-on experience with:
- 🐳 Docker fundamentals
- 🎛️ Container management
- 🏗️ Image building
- 🎼 Docker Compose
- 🌐 Networking and volumes
- Real-world applications