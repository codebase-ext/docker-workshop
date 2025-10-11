# 🌐 Docker Hub Setup & Image Sharing Guide

## 📋 Overview
**Duration:** 30 minutes  
**Prerequisites:** Docker installed and working  
**Goal:** Learn to create, publish, and share Docker images with the community

---

## 🎯 What You'll Learn
- Create a Docker Hub account
- Build and tag images for sharing
- Publish images to Docker Hub
- Share images with the community
- Best practices for image documentation
- Pull and use community images

---

## 📝 Step 1: Create Your Docker Hub Account

Docker Hub is the world's largest repository of container images. Having an account allows you to:
- **Pull public images** from the community
- **Push your own images** to share with others
- **Create private repositories** for your projects
- **Collaborate** with teams and organizations

### **Create Account:**
1. **Visit Docker Hub**: [https://hub.docker.com/](https://hub.docker.com/)
2. **Click "Sign Up"** in the top right corner
3. **Choose your plan**:
   - **Free Plan**: Includes 1 private repository + unlimited public repositories
   - **Pro/Team Plans**: More private repositories and advanced features
4. **Fill in your details**:
   - Username (this will be your Docker Hub namespace)
   - Email address
   - Password
5. **Verify your email** by clicking the link sent to your inbox
6. **Complete your profile** (optional but recommended)

**💡 Username Tips:**
- Choose a professional username (you might use this for work projects)
- Use lowercase letters, numbers, and hyphens only
- Make it memorable and related to your name or organization











## 🔐 Step 2: Login to Docker Hub via Command Line

Open your terminal and login:

**For all platforms:**
```bash
docker login
```

Enter your Docker Hub credentials when prompted:
```
Username: your-dockerhub-username
Password: your-dockerhub-password
```

**Success message:**
```
Login Succeeded
```

**🔐 Security Tip:** For better security, consider using Personal Access Tokens instead of passwords:
1. Go to [Docker Hub Account Settings](https://hub.docker.com/settings/security)
2. Create a new Access Token
3. Use the token as your password when logging in











## 🚀 Step 3: Create a Sample Application

Let's create a simple web application to demonstrate the publishing process.

**For Mac/Linux:**
```bash
mkdir my-first-image
cd my-first-image
```

**For Windows:**
```cmd
mkdir my-first-image
cd my-first-image
```

Create a simple `index.html`:

**For Mac/Linux:**
```bash
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My First Docker Image</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            text-align: center; 
            margin-top: 50px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container { 
            background: rgba(255, 255, 255, 0.9); 
            color: #333;
            padding: 50px; 
            border-radius: 15px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 600px;
        }
        h1 { color: #667eea; margin-bottom: 20px; }
        .info { background: #f0f0f0; padding: 15px; border-radius: 8px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Hello from My Docker Image!</h1>
        <div class="info">
            <strong>Created by:</strong> YOUR-NAME
        </div>
        <div class="info">
            <strong>Image:</strong> Running in Docker container
        </div>
        <div class="info">
            <strong>Purpose:</strong> Learning Docker Hub publishing
        </div>
        <p>This application demonstrates how to build, publish, and share Docker images with the community!</p>
    </div>
</body>
</html>
EOF
```

**For Windows (PowerShell):**
```powershell
@"
<!DOCTYPE html>
<html>
<head>
    <title>My First Docker Image</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            text-align: center; 
            margin-top: 50px; 
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container { 
            background: rgba(255, 255, 255, 0.9); 
            color: #333;
            padding: 50px; 
            border-radius: 15px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            max-width: 600px;
        }
        h1 { color: #667eea; margin-bottom: 20px; }
        .info { background: #f0f0f0; padding: 15px; border-radius: 8px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐳 Hello from My Docker Image!</h1>
        <div class="info">
            <strong>Created by:</strong> YOUR-NAME
        </div>
        <div class="info">
            <strong>Image:</strong> Running in Docker container
        </div>
        <div class="info">
            <strong>Purpose:</strong> Learning Docker Hub publishing
        </div>
        <p>This application demonstrates how to build, publish, and share Docker images with the community!</p>
    </div>
</body>
</html>
"@ | Out-File -FilePath index.html -Encoding UTF8
```

Create a `Dockerfile`:

**💡 File Creation Tip:** 
- Make sure to save the file as exactly `Dockerfile` (no extension)
- Use a text editor that preserves plain text format

```dockerfile
FROM nginx:alpine

# Copy our HTML file to nginx web root
COPY index.html /usr/share/nginx/html/

# Add a custom nginx configuration for better performance
RUN echo 'server { \
    listen 80; \
    server_name localhost; \
    location / { \
        root /usr/share/nginx/html; \
        index index.html; \
        try_files $uri $uri/ =404; \
    } \
    # Enable gzip compression \
    gzip on; \
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript; \
}' > /etc/nginx/conf.d/default.conf

# Expose port 80
EXPOSE 80

# Add labels for better image metadata
LABEL maintainer="your-email@example.com"
LABEL description="My first Docker image - a simple web app for Docker Hub"
LABEL version="1.0"
LABEL source="Docker Workshop"

# Health check to ensure the service is running
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
```











## 🏗️ Step 4: Build Your Image with Proper Tagging

Build the image with your Docker Hub username:

**Replace `YOUR-USERNAME` with your actual Docker Hub username:**
```bash
docker build -t YOUR-USERNAME/my-first-app:1.0 .
```

**Example:**
```bash
docker build -t johnsmith/my-first-app:1.0 .
```

**Tag Explanation:**
- `YOUR-USERNAME`: Your Docker Hub username (required for pushing)
- `my-first-app`: Repository name (choose any descriptive name)
- `1.0`: Version tag (helps with versioning your releases)

**Create additional tags:**
```bash
# Create a 'latest' tag (conventional for most recent version)
docker tag YOUR-USERNAME/my-first-app:1.0 YOUR-USERNAME/my-first-app:latest

# Create environment-specific tags
docker tag YOUR-USERNAME/my-first-app:1.0 YOUR-USERNAME/my-first-app:stable
```

View your tagged images:
```bash
docker images | grep YOUR-USERNAME/my-first-app
```











## 🧪 Step 5: Test Your Image Locally

Always test your image before publishing:

```bash
docker run -d -p 8080:80 --name my-app-test YOUR-USERNAME/my-first-app:1.0
```

Test it:

**For Mac/Linux:**
```bash
curl http://localhost:8080
```

**For Windows:**
```cmd
curl http://localhost:8080
```

Or open `http://localhost:8080` in your browser to see your application.

**Verify the health check:**
```bash
docker ps
```

You should see the health status in the STATUS column.

Clean up the test container:
```bash
docker stop my-app-test
docker rm my-app-test
```











## 📤 Step 6: Push Your Image to Docker Hub

Push your image to Docker Hub:

```bash
# Push the specific version
docker push YOUR-USERNAME/my-first-app:1.0

# Push the latest tag
docker push YOUR-USERNAME/my-first-app:latest

# Push the stable tag
docker push YOUR-USERNAME/my-first-app:stable
```

**You should see output like:**
```
The push refers to repository [docker.io/johnsmith/my-first-app]
a1b2c3d4e5f6: Pushed
7g8h9i0j1k2l: Layer already exists
m3n4o5p6q7r8: Layer already exists
...
1.0: digest: sha256:abc123... size: 1234
latest: digest: sha256:abc123... size: 1234
stable: digest: sha256:abc123... size: 1234
```

**💡 Push Tips:**
- The first push takes longer as it uploads all layers
- Subsequent pushes only upload changed layers
- Multiple tags pointing to the same image share layers











## 🌐 Step 7: Verify and Document on Docker Hub

### **Verify Your Image:**
1. Go to [https://hub.docker.com/](https://hub.docker.com/)
2. Login to your account
3. You should see your new repository: `YOUR-USERNAME/my-first-app`
4. Click on it to see details, tags, and usage instructions

### **Add Documentation:**
1. **Click "Edit"** on your repository page
2. **Add a Description**: Brief summary of what your image does
3. **Write a README**: Detailed usage instructions (see template below)
4. **Add Tags**: Keywords to help others find your image

### **README Template:**
```markdown
# My First App

A simple web application demonstrating Docker containerization and Docker Hub publishing.

## 🚀 Quick Start

```bash
docker run -d -p 8080:80 YOUR-USERNAME/my-first-app:latest
```

Visit http://localhost:8080 to see the application.

## 📋 Available Tags

- `latest`: Most recent stable version
- `1.0`: Initial release version  
- `stable`: Production-ready version

## 🔧 Configuration

- **Port**: 80 (internal), map to any external port
- **No environment variables required**
- **No volumes needed**
- **Health check included**

## 💻 Usage Examples

### Basic Usage
```bash
docker run -p 8080:80 YOUR-USERNAME/my-first-app:latest
```

### With Custom Port
```bash
docker run -p 3000:80 YOUR-USERNAME/my-first-app:latest
```

### Background Mode
```bash
docker run -d --name my-app -p 8080:80 YOUR-USERNAME/my-first-app:latest
```

## 🏗️ Building from Source

```bash
git clone [your-repo-url]
cd my-first-app
docker build -t YOUR-USERNAME/my-first-app:latest .
```

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! Please feel free to submit issues and enhancement requests.
```











## 👥 Step 8: Test Community Sharing

**Simulate being another user to verify sharing works:**

Remove your local images:
```bash
docker rmi YOUR-USERNAME/my-first-app:latest
docker rmi YOUR-USERNAME/my-first-app:1.0
docker rmi YOUR-USERNAME/my-first-app:stable
```

Pull your image from Docker Hub (as if you were someone else):
```bash
docker pull YOUR-USERNAME/my-first-app:latest
```

Run the pulled image:
```bash
docker run -d -p 8080:80 --name community-test YOUR-USERNAME/my-first-app:latest
```

Test it:
```bash
curl http://localhost:8080
```

Clean up:
```bash
docker stop community-test
docker rm community-test
```

**🎉 Congratulations!** You've successfully:
- ✅ Built a custom Docker image
- ✅ Published it to Docker Hub  
- ✅ Made it available to the global community
- ✅ Verified others can access and use it
- ✅ Added proper documentation











## 🏷️ Step 9: Advanced Tagging Strategies

Learn professional tagging practices:

### **Semantic Versioning:**
```bash
# Major.Minor.Patch versioning
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:1.0.0
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:1.0
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:1

# Push all versions
docker push YOUR-USERNAME/my-first-app:1.0.0
docker push YOUR-USERNAME/my-first-app:1.0  
docker push YOUR-USERNAME/my-first-app:1
```

### **Environment Tags:**
```bash
# Environment-specific tags
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:production
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:staging
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:development

# Push environment tags
docker push YOUR-USERNAME/my-first-app:production
docker push YOUR-USERNAME/my-first-app:staging
docker push YOUR-USERNAME/my-first-app:development
```

### **Date-based Tags:**
```bash
# Date-based tags for tracking
DATE=$(date +%Y%m%d)
docker tag YOUR-USERNAME/my-first-app:latest YOUR-USERNAME/my-first-app:$DATE
docker push YOUR-USERNAME/my-first-app:$DATE
```











## 🔍 Step 10: Explore Community Images

Practice pulling and using popular community images:

### **Official Images:**
```bash
# Official language runtimes
docker pull python:3.9-slim
docker pull node:18-alpine
docker pull openjdk:11-jre-slim

# Official databases
docker pull postgres:15-alpine
docker pull redis:alpine
docker pull mongo:latest

# Official web servers
docker pull nginx:alpine
docker pull httpd:alpine
```

### **Popular Community Images:**
```bash
# Development tools
docker pull portainer/portainer-ce
docker pull jenkins/jenkins:lts
docker pull sonarqube:community

# Monitoring and analytics
docker pull grafana/grafana
docker pull prom/prometheus
docker pull elasticsearch:8.5.0
```

### **Search for Images:**
```bash
# Search Docker Hub from command line
docker search python
docker search nginx
docker search YOUR-USERNAME
```

**Web Search:**
- Visit [https://hub.docker.com/search](https://hub.docker.com/search)
- Use filters: Official Images, Verified Publisher, etc.
- Check download counts and star ratings
- Read documentation and reviews











## 📖 Step 11: Best Practices for Docker Hub

### **Repository Naming:**
- ✅ Use lowercase letters, numbers, and hyphens
- ✅ Make names descriptive: `web-app`, `data-processor`, `api-server`
- ✅ Include purpose: `nginx-custom`, `python-ml-model`
- ❌ Avoid: `myapp`, `test`, `temp`

### **Image Documentation:**
1. **Add a detailed README** to your Docker Hub repository
2. **Include usage examples** and configuration options
3. **Document environment variables** and ports
4. **Provide troubleshooting tips**
5. **Add build instructions** if building from source

### **Security Considerations:**
- 🔒 **Never include secrets** in your images
- 🏷️ **Use specific base image tags** instead of `latest` in production
- 🔄 **Regularly update base images** for security patches
- 🛡️ **Scan images for vulnerabilities** using Docker Scout
- 🔑 **Use multi-stage builds** to reduce attack surface

### **Performance Optimization:**
- 📦 **Use alpine-based images** when possible (smaller size)
- 🗂️ **Order Dockerfile commands** for better layer caching
- 🧹 **Clean up package caches** in the same RUN command
- 📋 **Use .dockerignore** to exclude unnecessary files

### **Maintenance:**
- 🏷️ **Tag releases consistently** using semantic versioning
- 📝 **Maintain changelog** in your repository description
- 🔄 **Automate builds** using CI/CD pipelines
- 📊 **Monitor download statistics** and user feedback











## 🔄 Step 12: Automated Builds (Optional Advanced Topic)

Set up automated builds that trigger when you push code changes:

### **GitHub Integration:**
1. **Connect GitHub**: In Docker Hub, go to Account Settings → Linked Accounts
2. **Create Repository**: Link your GitHub repository to Docker Hub
3. **Configure Build Rules**: Set up automatic builds on git push
4. **Build Hooks**: Trigger builds on tags or branch changes

### **Example Build Configuration:**
```yaml
# docker-compose.yml for automated builds
version: '3.8'
services:
  app:
    build: .
    image: YOUR-USERNAME/my-first-app:latest
    ports:
      - "80:80"
```

### **CI/CD Integration:**
```yaml
# .github/workflows/docker-publish.yml
name: Docker Publish
on:
  push:
    tags: ['v*']
jobs:
  push:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build and push
        uses: docker/build-push-action@v3
        with:
          push: true
          tags: YOUR-USERNAME/my-first-app:latest
```











## 🧹 Step 13: Cleanup

Remove local test images and containers:

```bash
# Remove test containers
docker rm -f $(docker ps -aq --filter "ancestor=YOUR-USERNAME/my-first-app") 2>/dev/null || true

# Remove local images
docker rmi YOUR-USERNAME/my-first-app:latest 2>/dev/null || true
docker rmi YOUR-USERNAME/my-first-app:1.0 2>/dev/null || true
docker rmi YOUR-USERNAME/my-first-app:stable 2>/dev/null || true

# Clean up system
docker system prune -f
```

**For Mac/Linux:**
```bash
# Remove project directory
cd ..
rm -rf my-first-image
```

**For Windows:**
```cmd
cd ..
rmdir /s my-first-image
```

**🌐 Your Docker Hub Repository:** 
Your published images will remain on Docker Hub and continue to be available to the community unless you delete them from the web interface.











## 🎯 Key Takeaways

**You now know how to:**
- ✅ Create and configure a Docker Hub account
- ✅ Build images with proper tagging conventions
- ✅ Publish images to the global Docker community
- ✅ Document images for easy community adoption
- ✅ Use advanced tagging strategies for professional workflows
- ✅ Discover and use community images effectively
- ✅ Follow security and performance best practices

**Professional Skills Gained:**
- 🚀 **DevOps Workflow**: Complete CI/CD image publishing pipeline
- 🤝 **Community Contribution**: Sharing work with the global developer community  
- 📚 **Documentation**: Creating user-friendly technical documentation
- 🔒 **Security Awareness**: Safe practices for container image distribution
- 🏗️ **Software Distribution**: Modern approaches to software packaging and delivery

---

## 🚀 Next Steps

1. **🏗️ Practice with Real Projects**: Containerize your own applications and publish them
2. **🔄 Set up CI/CD**: Automate your build and publish process
3. **🏢 Explore Private Registries**: Learn about enterprise Docker registries
4. **🛡️ Security Scanning**: Use Docker Scout and other security tools
5. **📊 Monitoring**: Track usage statistics and user feedback
6. **🤝 Community Engagement**: Contribute to open source Docker projects
7. **📖 Advanced Topics**: Multi-architecture builds, image signing, and more

**Return to the main workshop:** [workshop_guide.md](workshop_guide.md)

---

**🎉 Docker Hub Mastery Complete!** You're now ready to share your containerized applications with the world! 🌍