# 🐍 Flask Application Example

## 🎯 Objective
Create a simple Flask "Hello World" application, containerize it, and deploy using Docker.

---

## Step 1: 📁 Project Setup
*Create a dedicated directory for the Flask application*

**For Mac/Linux:**
```bash
cd workshop
mkdir flask-app
cd flask-app
```

**For Windows:**
```cmd
cd workshop
mkdir flask-app
cd flask-app
```











## Step 2: 🐍 Create Flask Application
*Build a simple REST API with multiple endpoints*

Create `app.py`:

**💡 Note:** You can use any text editor to create these files:
- **Visual Studio Code** (recommended): `code app.py`
- **Notepad++ (Windows)**: Open Notepad++ and save as `app.py`
- **TextEdit (Mac)**: Make sure to save as plain text
- **Nano/Vim (Linux/Mac terminal)**: `nano app.py` or `vim app.py`

```python
from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello World from Flask!',
        'container_id': socket.gethostname(),
        'environment': os.getenv('ENV', 'production')
    })

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/api/data')
def get_data():
    return jsonify({
        'data': [
            {'id': 1, 'name': 'Docker'},
            {'id': 2, 'name': 'Containers'},
            {'id': 3, 'name': 'Flask'}
        ]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```











## Step 3: 📋 Create Requirements File
*Define Python dependencies for the application*

Create `requirements.txt`:
```
Flask==2.3.3
```











## Step 4: 🐳 Create Dockerfile
*Define how to build the Flask application container*

Create `Dockerfile`:
```dockerfile
# Use Python 3.9 slim image as base
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port 5000
EXPOSE 5000

# Set environment variable
ENV FLASK_APP=app.py
ENV ENV=development

# Run the application
CMD ["python", "app.py"]
```

**Dockerfile Explanation:**
- `FROM python:3.9-slim`: Lightweight Python base image
- `WORKDIR /app`: Sets working directory inside container
- `COPY requirements.txt .`: Copies requirements file first for Docker layer caching
- `RUN pip install`: Installs Python dependencies
- `COPY app.py .`: Copies application code
- `EXPOSE 5000`: Documents which port the app uses
- `ENV`: Sets environment variables
- `CMD`: Specifies the command to run when container starts











## Step 5: 🔨 Build Docker Image
*Compile the Dockerfile into a runnable Docker image*

```bash
docker build -t flask-hello-world .
```

Check if image was created:
```bash
docker images | grep flask-hello-world
```











## Step 6: 🚀 Run Flask Container
*Launch the Flask application in a Docker container*

```bash
docker run -d -p 5000:5000 --name flask-app flask-hello-world
```

Verify container is running:
```bash
docker ps
```











## Step 7: 🧪 Test the Application
*Verify all API endpoints are working correctly*

Test main endpoint:
```bash
curl http://localhost:5000/
```

Test health endpoint:
```bash
curl http://localhost:5000/health
```

Test data endpoint:
```bash
curl http://localhost:5000/api/data
```

Open browser to `http://localhost:5000` to see JSON response.











## Step 8: 📊 Check Container Logs
*Monitor application output and debug issues*

```bash
docker logs flask-app
```

Follow logs in real-time:
```bash
docker logs -f flask-app
```

Stop following with `Ctrl+C`.











## Step 9: 🔍 Access Container Shell
*Explore the container's internal file system*

```bash
docker exec -it flask-app bash
```

Inside container:
```bash
ps aux
ls -la
cat app.py
exit
```











## Step 10: 🌍 Environment Variables
*Configure application behavior with environment variables*

Stop current container:
```bash
docker stop flask-app
docker rm flask-app
```

Run with custom environment:
```bash
docker run -d -p 5000:5000 -e ENV=production --name flask-app flask-hello-world
```

Test to see environment change:
```bash
curl http://localhost:5000/
```











## Step 11: 📂 Volume Mounting for Development
*Enable live code changes without rebuilding the image*

Stop container:
```bash
docker stop flask-app
docker rm flask-app
```

Run with volume mount for live development:

**For Mac/Linux:**
```bash
docker run -d -p 5000:5000 -v $(pwd):/app --name flask-app flask-hello-world
```

**For Windows (Command Prompt):**
```cmd
docker run -d -p 5000:5000 -v %cd%:/app --name flask-app flask-hello-world
```

**For Windows (PowerShell):**
```powershell
docker run -d -p 5000:5000 -v ${PWD}:/app --name flask-app flask-hello-world
```

Modify `app.py` (add new route):
```python
@app.route('/version')
def version():
    return jsonify({'version': '1.0.0'})
```

**Note:** With Flask's debug mode enabled (`debug=True` in `app.py`), the application will automatically reload when you save changes to the mounted files. Test the new endpoint:
```bash
curl http://localhost:5000/version
```

If auto-reload doesn't work, restart the container:
```bash
docker restart flask-app
```











## Step 12: Docker Compose for Flask

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  flask-app:
    build: .
    ports:
      - "5000:5000"
    environment:
      - ENV=development
      - FLASK_ENV=development
    volumes:
      # Works for both Mac/Linux and Windows
      - .:/app
    command: python app.py
```

Stop existing container:
```bash
docker stop flask-app
docker rm flask-app
```

Run with Docker Compose:

**For Mac/Linux:**
```bash
docker-compose up -d
```

**For Windows:**
```cmd
docker-compose up -d
```

**Alternative (newer Docker versions):**
```bash
docker compose up -d
```

Test the application:
```bash
curl http://localhost:5000/
```

View logs:
```bash
docker-compose logs flask-app
```











## Step 13: Multi-Stage Build (Optional)

Create `Dockerfile.multi`:
```dockerfile
# Build stage - Use full Python image for dependencies
FROM python:3.9 as builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Production stage - Use slim image for smaller final size
FROM python:3.9-slim

WORKDIR /app

# Copy dependencies from builder stage
COPY --from=builder /root/.local /root/.local
COPY app.py .

# Add local binaries to PATH
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000
CMD ["python", "app.py"]
```

**Multi-stage build benefits:**
- **Builder stage**: Uses full Python image with build tools for installing dependencies
- **Production stage**: Uses slim image without build tools for smaller final size
- **Result**: Smaller production image with all necessary dependencies

Build multi-stage image:
```bash
docker build -f Dockerfile.multi -t flask-hello-world:multi .
```

Compare image sizes:
```bash
docker images | grep flask-hello-world
```











## Step 14: Cleanup

Stop and remove containers:
```bash
docker-compose down
```

Or manually:
```bash
docker stop flask-app
docker rm flask-app
```

Remove images:
```bash
docker rmi flask-hello-world flask-hello-world:multi
```

---

## Key Learning Points

1. **Flask Application Structure**: Simple REST API with multiple endpoints
2. **Dockerfile Best Practices**: Layer caching, slim images, proper WORKDIR
3. **Container Management**: Building, running, logging, accessing containers
4. **Environment Configuration**: Using environment variables
5. **Development Workflow**: Volume mounting for live development
6. **Docker Compose**: Simplified container orchestration
7. **Multi-Stage Builds**: Optimizing image size for production

---

**Flask Example Complete!** ✅