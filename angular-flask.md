# 🚀 Full-Stack Angular + Flask Integration

## 🎯 Objective
Create a complete full-stack application with Angular frontend, Flask backend, and database integration using Docker Compose for orchestration.

---

## Step 1: 📁 Project Setup
*Create organized directories for the full-stack application*

**For Mac/Linux:**
```bash
cd workshop
mkdir full-stack-app
cd full-stack-app
mkdir frontend backend database
```

**For Windows:**
```cmd
cd workshop
mkdir full-stack-app
cd full-stack-app
mkdir frontend backend database
```











## Step 2: 🐍 Backend API Enhancement
*Build a robust Flask API with database integration*

**For Mac/Linux:**
```bash
cd backend
```

**For Windows:**
```cmd
cd backend
```

Create enhanced `app.py`:
```python
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import json
import time
from datetime import datetime
import sqlite3

app = Flask(__name__)
CORS(app)  # Enable CORS for Angular frontend

# Database initialization
def init_db():
    conn = sqlite3.connect('/data/app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN DEFAULT FALSE,
            user_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')
    
    # Insert sample data if tables are empty
    cursor.execute('SELECT COUNT(*) FROM users')
    if cursor.fetchone()[0] == 0:
        sample_users = [
            ('John Doe', 'john@example.com'),
            ('Jane Smith', 'jane@example.com'),
            ('Bob Johnson', 'bob@example.com')
        ]
        cursor.executemany('INSERT INTO users (name, email) VALUES (?, ?)', sample_users)
        
        sample_tasks = [
            ('Learn Docker', 'Complete Docker workshop', False, 1),
            ('Build Angular App', 'Create frontend application', True, 1),
            ('Setup Flask API', 'Create backend API', True, 2),
            ('Deploy to Production', 'Deploy full stack app', False, 2)
        ]
        cursor.executemany('INSERT INTO tasks (title, description, completed, user_id) VALUES (?, ?, ?, ?)', sample_tasks)
    
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def home():
    return jsonify({
        'message': 'Full-Stack Flask API',
        'version': '2.0.0',
        'timestamp': datetime.now().isoformat(),
        'endpoints': [
            '/users',
            '/tasks',
            '/health',
            '/stats'
        ]
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'database': 'connected',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/users', methods=['GET', 'POST'])
def users():
    conn = sqlite3.connect('/data/app.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute('SELECT * FROM users ORDER BY created_at DESC')
        users = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return jsonify(users)
    
    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data:
            return jsonify({'error': 'Name and email are required'}), 400
        
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', 
                      (data['name'], data['email']))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({'id': user_id, 'message': 'User created successfully'}), 201

@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    conn = sqlite3.connect('/data/app.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if request.method == 'GET':
        cursor.execute('''
            SELECT t.*, u.name as user_name 
            FROM tasks t 
            LEFT JOIN users u ON t.user_id = u.id 
            ORDER BY t.created_at DESC
        ''')
        tasks = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return jsonify(tasks)
    
    elif request.method == 'POST':
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({'error': 'Title is required'}), 400
        
        cursor.execute('INSERT INTO tasks (title, description, user_id) VALUES (?, ?, ?)', 
                      (data['title'], data.get('description', ''), data.get('user_id', 1)))
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return jsonify({'id': task_id, 'message': 'Task created successfully'}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT', 'DELETE'])
def task_detail(task_id):
    conn = sqlite3.connect('/data/app.db')
    cursor = conn.cursor()
    
    if request.method == 'PUT':
        data = request.get_json()
        cursor.execute('UPDATE tasks SET completed = ? WHERE id = ?', 
                      (data.get('completed', False), task_id))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task updated successfully'})
    
    elif request.method == 'DELETE':
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Task deleted successfully'})

@app.route('/stats')
def stats():
    conn = sqlite3.connect('/data/app.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT COUNT(*) FROM users')
    user_count = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE completed = 1')
    completed_tasks = cursor.fetchone()[0]
    
    cursor.execute('SELECT COUNT(*) FROM tasks WHERE completed = 0')
    pending_tasks = cursor.fetchone()[0]
    
    conn.close()
    
    return jsonify({
        'users': user_count,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'total_tasks': completed_tasks + pending_tasks
    })

if __name__ == '__main__':
    # Initialize database
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
```

Create `requirements.txt`:
```
Flask==2.3.3
Flask-CORS==4.0.0
```

Create `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY app.py .

# Create data directory
RUN mkdir -p /data

EXPOSE 5000

CMD ["python", "app.py"]
```











## Step 3: Enhanced Frontend

**For Mac/Linux:**
```bash
cd ../frontend
```

**For Windows:**
```cmd
cd ..\frontend
```

Update the Angular API service to work with the enhanced backend:

Create `src/app/services/api.service.ts`:
```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface User {
  id: number;
  name: string;
  email: string;
  created_at: string;
}

export interface Task {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  user_id: number;
  user_name?: string;
  created_at: string;
}

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  // Health check
  getHealth(): Observable<any> {
    return this.http.get(`${this.apiUrl}/health`);
  }

  // Users
  getUsers(): Observable<User[]> {
    return this.http.get<User[]>(`${this.apiUrl}/users`);
  }

  createUser(user: {name: string, email: string}): Observable<any> {
    return this.http.post(`${this.apiUrl}/users`, user);
  }

  // Tasks
  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.apiUrl}/tasks`);
  }

  createTask(task: {title: string, description: string, user_id: number}): Observable<any> {
    return this.http.post(`${this.apiUrl}/tasks`, task);
  }

  updateTask(taskId: number, task: {completed: boolean}): Observable<any> {
    return this.http.put(`${this.apiUrl}/tasks/${taskId}`, task);
  }

  deleteTask(taskId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/tasks/${taskId}`);
  }

  // Stats
  getStats(): Observable<any> {
    return this.http.get(`${this.apiUrl}/stats`);
  }
}
```

Create directory and component:

**For Mac/Linux:**
```bash
mkdir -p src/app/home
mkdir -p src/app/services
```

**For Windows:**
```cmd
mkdir src\app\home
mkdir src\app\services
```

Create `src/app/home/home.component.ts`:
```typescript
import { Component, OnInit } from '@angular/core';
import { ApiService, User, Task } from '../services/api.service';

@Component({
  selector: 'app-home',
  template: `
    <div class="dashboard">
      <!-- Stats Section -->
      <div class="stats-grid" *ngIf="stats">
        <div class="stat-card">
          <h3>{{ stats.users }}</h3>
          <p>Total Users</p>
        </div>
        <div class="stat-card">
          <h3>{{ stats.total_tasks }}</h3>
          <p>Total Tasks</p>
        </div>
        <div class="stat-card">
          <h3>{{ stats.completed_tasks }}</h3>
          <p>Completed</p>
        </div>
        <div class="stat-card">
          <h3>{{ stats.pending_tasks }}</h3>
          <p>Pending</p>
        </div>
      </div>

      <!-- Connection Status -->
      <div class="connection-status">
        <button class="btn" (click)="checkConnection()" [disabled]="checking">
          {{ checking ? 'Checking...' : 'Test Backend Connection' }}
        </button>
        <span class="status" [class.connected]="connected" [class.disconnected]="!connected">
          {{ connectionStatus }}
        </span>
      </div>

      <!-- Users Section -->
      <div class="section">
        <h2>Users</h2>
        <div class="user-form">
          <input [(ngModel)]="newUser.name" placeholder="Name" class="input">
          <input [(ngModel)]="newUser.email" placeholder="Email" class="input">
          <button class="btn" (click)="addUser()">Add User</button>
        </div>
        <div class="users-list">
          <div *ngFor="let user of users" class="user-card">
            <h4>{{ user.name }}</h4>
            <p>{{ user.email }}</p>
            <small>{{ user.created_at | date:'medium' }}</small>
          </div>
        </div>
      </div>

      <!-- Tasks Section -->
      <div class="section">
        <h2>Tasks</h2>
        <div class="task-form">
          <input [(ngModel)]="newTask.title" placeholder="Task Title" class="input">
          <input [(ngModel)]="newTask.description" placeholder="Description" class="input">
          <select [(ngModel)]="newTask.user_id" class="input">
            <option value="">Select User</option>
            <option *ngFor="let user of users" [value]="user.id">{{ user.name }}</option>
          </select>
          <button class="btn" (click)="addTask()">Add Task</button>
        </div>
        <div class="tasks-list">
          <div *ngFor="let task of tasks" class="task-card" [class.completed]="task.completed">
            <div class="task-content">
              <h4>{{ task.title }}</h4>
              <p>{{ task.description }}</p>
              <small>Assigned to: {{ task.user_name }} | {{ task.created_at | date:'medium' }}</small>
            </div>
            <div class="task-actions">
              <button class="btn-small" (click)="toggleTask(task)" 
                      [class.btn-complete]="!task.completed" 
                      [class.btn-undo]="task.completed">
                {{ task.completed ? 'Undo' : 'Complete' }}
              </button>
              <button class="btn-small btn-delete" (click)="deleteTask(task.id)">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .dashboard {
      padding: 20px;
      max-width: 1200px;
      margin: 0 auto;
    }
    .stats-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 20px;
      margin-bottom: 30px;
    }
    .stat-card {
      background: white;
      padding: 20px;
      border-radius: 8px;
      text-align: center;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .stat-card h3 {
      font-size: 2rem;
      margin: 0;
      color: #667eea;
    }
    .connection-status {
      text-align: center;
      margin: 20px 0;
    }
    .status {
      margin-left: 10px;
      padding: 5px 10px;
      border-radius: 4px;
    }
    .connected {
      background: #4CAF50;
      color: white;
    }
    .disconnected {
      background: #f44336;
      color: white;
    }
    .section {
      background: white;
      margin: 20px 0;
      padding: 25px;
      border-radius: 8px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .user-form, .task-form {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }
    .input {
      padding: 10px;
      border: 1px solid #ddd;
      border-radius: 4px;
      flex: 1;
      min-width: 200px;
    }
    .users-list {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
      gap: 15px;
    }
    .user-card {
      padding: 15px;
      border: 1px solid #eee;
      border-radius: 6px;
      background: #f9f9f9;
    }
    .user-card h4 {
      margin: 0 0 5px 0;
      color: #333;
    }
    .tasks-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .task-card {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 15px;
      border: 1px solid #eee;
      border-radius: 6px;
      background: #f9f9f9;
    }
    .task-card.completed {
      background: #e8f5e8;
      opacity: 0.8;
    }
    .task-card.completed .task-content {
      text-decoration: line-through;
    }
    .task-actions {
      display: flex;
      gap: 5px;
    }
    .btn-small {
      padding: 5px 10px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      font-size: 12px;
    }
    .btn-complete {
      background: #4CAF50;
      color: white;
    }
    .btn-undo {
      background: #ff9800;
      color: white;
    }
    .btn-delete {
      background: #f44336;
      color: white;
    }
  `]
})
export class HomeComponent implements OnInit {
  users: User[] = [];
  tasks: Task[] = [];
  stats: any = null;
  connected: boolean = false;
  checking: boolean = false;
  connectionStatus: string = 'Not checked';

  newUser = { name: '', email: '' };
  newTask = { title: '', description: '', user_id: 0 };

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadData();
  }

  loadData() {
    this.loadUsers();
    this.loadTasks();
    this.loadStats();
    this.checkConnection();
  }

  checkConnection() {
    this.checking = true;
    this.apiService.getHealth().subscribe({
      next: (response) => {
        this.connected = true;
        this.connectionStatus = 'Connected to Flask API';
        this.checking = false;
      },
      error: (error) => {
        this.connected = false;
        this.connectionStatus = 'Cannot connect to Flask API';
        this.checking = false;
      }
    });
  }

  loadUsers() {
    this.apiService.getUsers().subscribe({
      next: (users) => this.users = users,
      error: (error) => console.error('Error loading users:', error)
    });
  }

  loadTasks() {
    this.apiService.getTasks().subscribe({
      next: (tasks) => this.tasks = tasks,
      error: (error) => console.error('Error loading tasks:', error)
    });
  }

  loadStats() {
    this.apiService.getStats().subscribe({
      next: (stats) => this.stats = stats,
      error: (error) => console.error('Error loading stats:', error)
    });
  }

  addUser() {
    if (this.newUser.name && this.newUser.email) {
      this.apiService.createUser(this.newUser).subscribe({
        next: (response) => {
          this.newUser = { name: '', email: '' };
          this.loadUsers();
          this.loadStats();
        },
        error: (error) => console.error('Error creating user:', error)
      });
    }
  }

  addTask() {
    if (this.newTask.title && this.newTask.user_id) {
      this.apiService.createTask(this.newTask).subscribe({
        next: (response) => {
          this.newTask = { title: '', description: '', user_id: 0 };
          this.loadTasks();
          this.loadStats();
        },
        error: (error) => console.error('Error creating task:', error)
      });
    }
  }

  toggleTask(task: Task) {
    this.apiService.updateTask(task.id, { completed: !task.completed }).subscribe({
      next: (response) => {
        this.loadTasks();
        this.loadStats();
      },
      error: (error) => console.error('Error updating task:', error)
    });
  }

  deleteTask(taskId: number) {
    this.apiService.deleteTask(taskId).subscribe({
      next: (response) => {
        this.loadTasks();
        this.loadStats();
      },
      error: (error) => console.error('Error deleting task:', error)
    });
  }
}
```

Update `src/app/app.module.ts` to include FormsModule:
```typescript
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { ApiService } from './services/api.service';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

Create frontend `Dockerfile`:
```dockerfile
# Multi-stage build for Angular
FROM node:18-alpine as build

WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build:prod

# Serve with nginx
FROM nginx:alpine
COPY --from=build /app/dist/angular-docker-app /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```











## Step 4: 🎼 Create Docker Compose Configuration
*Orchestrate multiple services with Docker Compose*

**For Mac/Linux:**
```bash
cd ../
```

**For Windows:**
```cmd
cd ..
```

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  # Backend API (SQLite database included)
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
    volumes:
      - api_data:/data
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    environment:
      - NODE_ENV=production

  # Redis for caching (optional)
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
    command: redis-server --appendonly yes

  # Nginx reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf
    depends_on:
      - frontend
      - backend

volumes:
  api_data:
  redis_data:

networks:
  default:
    driver: bridge
```

**Docker Compose Components Explained:**

- **database**: PostgreSQL database with persistent storage
- **backend**: Flask API server with health checks
- **frontend**: Angular application served by Nginx
- **redis**: Optional caching layer
- **nginx**: Reverse proxy for routing requests
- **volumes**: Named volumes for data persistence
- **networks**: Custom network for service communication











## Step 6: Create Nginx Reverse Proxy Configuration

**For Mac/Linux:**
```bash
mkdir nginx
```

**For Windows:**
```cmd
mkdir nginx
```

Create `nginx/nginx.conf`:
```nginx
events {
    worker_connections 1024;
}

http {
    upstream frontend {
        server frontend:80;
    }

    upstream backend {
        server backend:5000;
    }

    server {
        listen 80;
        server_name localhost;

        # Frontend routes
        location / {
            proxy_pass http://frontend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Backend API routes
        location /api/ {
            rewrite ^/api/(.*)$ /$1 break;
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            
            # CORS headers
            add_header Access-Control-Allow-Origin *;
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE, OPTIONS";
            add_header Access-Control-Allow-Headers "DNT,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range";
        }

        # Direct backend routes (without /api prefix)
        location ~ ^/(health|users|tasks|stats)(/.*)?$ {
            proxy_pass http://backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }
}
```











## Step 6: Development Docker Compose

Create `docker-compose.dev.yml`:
```yaml
version: '3.8'

services:
  # Development backend with live reload
  backend:
    build: ./backend
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=development
      - FLASK_DEBUG=1
    volumes:
      # For Mac/Linux
      - ./backend:/app
      # For Windows, use the same syntax
      - ./backend:/app
      - dev_data:/data
    command: python app.py

  # Development frontend with live reload
  frontend:
    image: node:18-alpine
    working_dir: /app
    ports:
      - "4200:4200"
    volumes:
      # For Mac/Linux
      - ./frontend:/app
      # For Windows, use the same syntax
      - ./frontend:/app
      - /app/node_modules
    command: sh -c "npm install && npm start -- --host 0.0.0.0"
    depends_on:
      - backend

volumes:
  dev_data:
```











## Step 7: 🏗️ Build and Run the Full Stack
*Launch the complete multi-service application*

Build all services:
```bash
docker-compose build
```

Start all services:
```bash
docker-compose up -d
```

Check service status:
```bash
docker-compose ps
```

View logs:
```bash
docker-compose logs -f
```











## Step 8: 🧪 Test the Complete Application
*Verify all services are working together correctly*

Test database connection:
```bash
docker-compose exec backend sqlite3 /data/app.db "SELECT * FROM users;"
```

Test backend API:
```bash
curl http://localhost:5000/health
curl http://localhost:5000/users
curl http://localhost:5000/tasks
```

Test frontend:
Open browser to `http://localhost:80`

Test reverse proxy:
```bash
curl http://localhost:8080/api/health
```











## Step 9: Application Monitoring

Create monitoring docker-compose:

Create `docker-compose.monitoring.yml`:
```yaml
version: '3.8'

services:
  # Extend the main docker-compose.yml
  prometheus:
    image: prom/prometheus:latest
    ports:
      - "9090:9090"
    volumes:
      - ./monitoring/prometheus.yml:/etc/prometheus/prometheus.yml

  grafana:
    image: grafana/grafana:latest
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana_data:/var/lib/grafana

  portainer:
    image: portainer/portainer-ce:latest
    ports:
      - "9000:9000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - portainer_data:/data

volumes:
  grafana_data:
  portainer_data:
```

Run with monitoring:
```bash
docker-compose -f docker-compose.yml -f docker-compose.monitoring.yml up -d
```

## Step 11: Production Deployment

Create `docker-compose.prod.yml`:
```yaml
version: '3.8'

services:
  database:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: fullstack_prod
      POSTGRES_USER: produser
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    secrets:
      - db_password
    volumes:
      - postgres_prod_data:/var/lib/postgresql/data
    restart: unless-stopped

  backend:
    build: 
      context: ./backend
      dockerfile: Dockerfile.prod
    environment:
      - FLASK_ENV=production
      - SECRET_KEY_FILE=/run/secrets/flask_secret
    secrets:
      - flask_secret
    depends_on:
      - database
    restart: unless-stopped

  frontend:
    build:
      context: ./frontend
      dockerfile: Dockerfile.prod
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "443:443"
      - "80:80"
    volumes:
      - ./nginx/prod.conf:/etc/nginx/nginx.conf
      - ./ssl:/etc/nginx/ssl
    depends_on:
      - frontend
      - backend
    restart: unless-stopped

secrets:
  db_password:
    file: ./secrets/db_password.txt
  flask_secret:
    file: ./secrets/flask_secret.txt

volumes:
  postgres_prod_data:
```

## Step 12: Scaling the Application

Scale specific services:
```bash
# Scale backend to 3 instances
docker-compose up -d --scale backend=3

# Scale frontend to 2 instances
docker-compose up -d --scale frontend=2
```

Check scaled services:
```bash
docker-compose ps
```

## Step 13: Backup and Restore

Create backup script `backup.sh`:
```bash
#!/bin/bash
# Backup database
docker-compose exec -T database pg_dump -U admin fullstack_db > backup_$(date +%Y%m%d_%H%M%S).sql

# Backup volumes
docker run --rm -v full-stack-app_postgres_data:/data -v $(pwd):/backup alpine tar czf /backup/postgres_backup_$(date +%Y%m%d_%H%M%S).tar.gz /data
```

Create restore script `restore.sh`:
```bash
#!/bin/bash
# Restore database
docker-compose exec -T database psql -U admin fullstack_db < $1
```

## Step 14: Health Checks and Monitoring

Check health status:
```bash
docker-compose ps
```

View resource usage:
```bash
docker stats
```

Check logs for errors:
```bash
docker-compose logs --tail=100 backend
docker-compose logs --tail=100 frontend
```

## Step 15: Cleanup and Maintenance

Stop all services:
```bash
docker-compose down
```

Remove volumes (careful - this deletes data):
```bash
docker-compose down -v
```

Clean up unused resources:
```bash
docker system prune -f
docker volume prune -f
```

Complete cleanup:
```bash
docker-compose down --rmi all --volumes --remove-orphans
```

---

## 🎓 Key Learning Points

1. **🏗️ Multi-Service Architecture**: Frontend, backend, database, and proxy services
2. **🌐 Service Communication**: How containers communicate through Docker networks
3. **💾 Data Persistence**: Using volumes for database and application data
4. **🌍 Environment Management**: Different configurations for dev/prod environments
5. **❤️ Health Checks**: Monitoring service health and dependencies
6. **🔄 Reverse Proxy**: Using Nginx to route requests to appropriate services
7. **📈 Scaling**: Horizontal scaling of individual services
8. **🔐 Secrets Management**: Secure handling of passwords and keys
9. **📊 Monitoring**: Application and infrastructure monitoring
10. **🚀 Production Deployment**: Best practices for production environments

---

## ✨ Application Features Demonstrated

✅ **📝 Full CRUD Operations**: Create, Read, Update, Delete users and tasks  
✅ **🗄️ Database Integration**: PostgreSQL with data persistence  
✅ **🔌 API Communication**: REST API between Angular and Flask  
✅ **🎼 Container Orchestration**: Multi-service Docker Compose setup  
✅ **🔄 Development Workflow**: Live reload for both frontend and backend  
✅ **🏭 Production Ready**: Health checks, monitoring, and scaling  
✅ **🔒 Security**: CORS handling, secrets management  
✅ **⚡ Performance**: Multi-stage builds, optimized images  

---

**Full-Stack Integration Complete!** 🚀