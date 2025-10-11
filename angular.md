# 🅰️ Angular Application Example

## 🎯 Objective
Create a modern Angular single-page application, containerize it using multi-stage Docker build, and serve it with Nginx.

---

## Step 1: 📁 Project Setup
*Create a dedicated directory for the Angular application*

**For Mac/Linux:**
```bash
cd workshop
mkdir angular-app
cd angular-app
```

**For Windows:**
```cmd
cd workshop
mkdir angular-app
cd angular-app
```











## Step 2: 🏗️ Create Angular Project Structure
*Set up the basic Angular application folder structure*

**For Mac/Linux:**
```bash
mkdir src
mkdir src/app
```

**For Windows:**
```cmd
mkdir src
mkdir src\app
```











## Step 3: 📦 Create Package.json
*Define Node.js dependencies and build scripts*

Create `package.json`:

**💡 Note:** You can use any text editor to create these files:
- **Visual Studio Code** (recommended): `code package.json`
- **Notepad++ (Windows)**: Open Notepad++ and save as `package.json`
- **TextEdit (Mac)**: Make sure to save as plain text, not RTF
- **Command line text editors**: `nano package.json` or `vim package.json`

```json
{
  "name": "angular-docker-app",
  "version": "1.0.0",
  "scripts": {
    "ng": "ng",
    "start": "ng serve",
    "build": "ng build",
    "build:prod": "ng build --configuration production"
  },
  "dependencies": {
    "@angular/animations": "^16.0.0",
    "@angular/common": "^16.0.0",
    "@angular/compiler": "^16.0.0",
    "@angular/core": "^16.0.0",
    "@angular/platform-browser": "^16.0.0",
    "@angular/platform-browser-dynamic": "^16.0.0",
    "@angular/router": "^16.0.0",
    "rxjs": "~7.8.0",
    "tslib": "^2.3.0",
    "zone.js": "~0.13.0"
  },
  "devDependencies": {
    "@angular-devkit/build-angular": "^16.0.0",
    "@angular/cli": "^16.0.0",
    "@angular/compiler-cli": "^16.0.0",
    "typescript": "~5.0.2"
  }
}
```











## Step 4: ⚙️ Create Angular Configuration
*Configure Angular CLI build settings and project structure*

Create `angular.json`:
```json
{
  "$schema": "./node_modules/@angular/cli/lib/config/schema.json",
  "version": 1,
  "newProjectRoot": "projects",
  "projects": {
    "angular-docker-app": {
      "projectType": "application",
      "schematics": {},
      "root": "",
      "sourceRoot": "src",
      "prefix": "app",
      "architect": {
        "build": {
          "builder": "@angular-devkit/build-angular:browser",
          "options": {
            "outputPath": "dist/angular-docker-app",
            "index": "src/index.html",
            "main": "src/main.ts",
            "polyfills": "src/polyfills.ts",
            "tsConfig": "tsconfig.app.json",
            "assets": [
              "src/favicon.ico",
              "src/assets"
            ],
            "styles": [
              "src/styles.css"
            ],
            "scripts": []
          },
          "configurations": {
            "production": {
              "budgets": [
                {
                  "type": "initial",
                  "maximumWarning": "500kb",
                  "maximumError": "1mb"
                }
              ],
              "outputHashing": "all"
            }
          }
        },
        "serve": {
          "builder": "@angular-devkit/build-angular:dev-server",
          "configurations": {
            "production": {
              "buildTarget": "angular-docker-app:build:production"
            }
          }
        }
      }
    }
  }
}
```











## Step 5: Create TypeScript Configuration

Create `tsconfig.json`:
```json
{
  "compileOnSave": false,
  "compilerOptions": {
    "baseUrl": "./",
    "outDir": "./dist/out-tsc",
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "sourceMap": true,
    "declaration": false,
    "downlevelIteration": true,
    "experimentalDecorators": true,
    "moduleResolution": "node",
    "importHelpers": true,
    "target": "ES2022",
    "module": "ES2022",
    "useDefineForClassFields": false,
    "lib": [
      "ES2022",
      "dom"
    ]
  },
  "angularCompilerOptions": {
    "enableI18nLegacyMessageIdFormat": false,
    "strictInjectionParameters": true,
    "strictInputAccessModifiers": true,
    "strictTemplates": true
  }
}
```

Create `tsconfig.app.json`:
```json
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "outDir": "./out-tsc/app",
    "types": []
  },
  "files": [
    "src/main.ts",
    "src/polyfills.ts"
  ],
  "include": [
    "src/**/*.d.ts"
  ]
}
```











## Step 6: Create Angular Application Files

Create `src/index.html`:
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Angular Docker App</title>
  <base href="/">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/x-icon" href="favicon.ico">
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      margin: 0;
      padding: 0;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      min-height: 100vh;
    }
  </style>
</head>
<body>
  <app-root></app-root>
</body>
</html>
```

Create `src/main.ts`:
```typescript
import { platformBrowserDynamic } from '@angular/platform-browser-dynamic';
import { AppModule } from './app/app.module';

platformBrowserDynamic().bootstrapModule(AppModule)
  .catch(err => console.error(err));
```

Create `src/polyfills.ts`:
```typescript
import 'zone.js/dist/zone';
```











Create `src/styles.css`:
```css
/* Global Styles */
* {
  box-sizing: border-box;
}

body {
  margin: 0;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

.card {
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin: 20px 0;
}

.btn {
  background: #667eea;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s;
}
```











## Step 7: Create Angular Components
}

.btn:hover {
  background: #5a6fd8;
}

.btn:disabled {
  background: #ccc;
  cursor: not-allowed;
}
```

## Step 8: Create Angular Module

Create `src/app/app.module.ts`:
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











Create `src/app/app.component.ts`:
```typescript
import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div class="container">
      <h1>🐳 Angular Docker Application</h1>
      <app-home></app-home>
    </div>
  `,
  styles: [`
    .container {
      min-height: 100vh;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      color: white;
      padding: 40px 20px;
    }
    h1 {
      text-align: center;
      font-size: 2.5rem;
      margin-bottom: 40px;
      text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
  `]
})
export class AppComponent {
  title = 'Angular Docker App';
}
```











Create directory and component:
```bash
mkdir src/app/home
```











Create `src/app/home/home.component.ts`:
```typescript
import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-home',
  template: `
    <div class="home-container">
      <div class="card">
        <h2>Welcome to Angular + Docker! 🚀</h2>
        <p>This Angular application is running inside a Docker container.</p>
        
        <div class="features">
          <h3>Features Demonstrated:</h3>
          <ul>
            <li>Angular 16 Application</li>
            <li>Multi-stage Docker build</li>
            <li>Nginx web server</li>
            <li>Optimized production build</li>
            <li>Container orchestration ready</li>
          </ul>
        </div>

        <div class="actions">
          <button class="btn" (click)="loadData()" [disabled]="loading">
            {{ loading ? 'Loading...' : 'Test API Connection' }}
          </button>
          <button class="btn" (click)="containerInfo()">
            Show Container Info
          </button>
        </div>

        <div class="info" *ngIf="data">
          <h3>API Response:</h3>
          <pre>{{ data | json }}</pre>
        </div>

        <div class="info" *ngIf="error">
          <h3>Error:</h3>
          <p class="error">{{ error }}</p>
        </div>
      </div>
    </div>
  `,
  styles: [`
    .home-container {
      max-width: 800px;
      margin: 0 auto;
    }
    .card {
      background: rgba(255, 255, 255, 0.95);
      color: #333;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    .features ul {
      list-style-type: none;
      padding: 0;
    }
    .features li {
      padding: 8px 0;
      border-bottom: 1px solid #eee;
    }
    .features li::before {
      content: "✓ ";
      color: #4CAF50;
      font-weight: bold;
    }
    .actions {
      margin: 20px 0;
    }
    .btn {
      margin-right: 10px;
      margin-bottom: 10px;
    }
    .info {
      margin-top: 20px;
      padding: 15px;
      background: #f5f5f5;
      border-radius: 4px;
    }
    .error {
      color: #d32f2f;
    }
    pre {
      background: #333;
      color: #fff;
      padding: 10px;
      border-radius: 4px;
      overflow-x: auto;
    }
  `]
})
export class HomeComponent implements OnInit {
  data: any = null;
  error: string = '';
  loading: boolean = false;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.containerInfo();
  }

  loadData() {
    this.loading = true;
    this.error = '';
    this.apiService.getData().subscribe({
      next: (response) => {
        this.data = response;
        this.loading = false;
      },
      error: (err) => {
        this.error = 'Failed to connect to API. Make sure Flask backend is running.';
        this.loading = false;
      }
    });
  }

  containerInfo() {
    this.data = {
      message: 'Angular app running in Docker container',
      timestamp: new Date(),
      environment: 'production',
      container: 'nginx-alpine'
    };
  }
}
```











## Step 9: Create API Service

**For Mac/Linux:**
```bash
mkdir src/app/services
```

**For Windows:**
```cmd
mkdir src\app\services
```











Create `src/app/services/api.service.ts`:
```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  getData(): Observable<any> {
    return this.http.get(`${this.apiUrl}/api/data`);
  }

  getHealth(): Observable<any> {
    return this.http.get(`${this.apiUrl}/health`);
  }
}
```











## Step 10: Create Favicon and Assets

**For Mac/Linux:**
```bash
mkdir src/assets
```

**For Windows:**
```cmd
mkdir src\assets
```

Create a simple favicon or download one:

**For Mac/Linux:**
```bash
# Create a simple favicon.ico file
# You can create one at https://favicon.io/ or use any existing favicon
# For now, create an empty file as placeholder
touch src/favicon.ico
```

**For Windows:**
```cmd
REM Create a simple favicon.ico file
REM You can create one at https://favicon.io/ or use any existing favicon
REM For now, create an empty file as placeholder
copy NUL src\favicon.ico
```

Alternatively, you can create a simple SVG favicon:

**For Mac/Linux:**
```bash
cat > src/favicon.ico << 'EOF'
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="8" fill="#667eea"/>
  <text x="8" y="12" text-anchor="middle" fill="white" font-size="10">A</text>
</svg>
EOF
```

**For Windows (PowerShell):**
```powershell
@"
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="8" fill="#667eea"/>
  <text x="8" y="12" text-anchor="middle" fill="white" font-size="10">A</text>
</svg>
"@ | Out-File -FilePath src\favicon.ico -Encoding UTF8
```











## Step 11: 🐳 Create Multi-Stage Dockerfile
*Build an optimized production image using multi-stage Docker build*

Create `Dockerfile`:
```dockerfile
# Stage 1: Build the Angular application
FROM node:18-alpine as build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the Angular application for production
RUN npm run build:prod

# Stage 2: Serve the application with Nginx
FROM nginx:alpine

# Copy the built Angular app from the previous stage
COPY --from=build /app/dist/angular-docker-app /usr/share/nginx/html

# Copy custom nginx configuration (optional)
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
```

**🔍 Dockerfile Explanation:**
- **Stage 1 (build)**: Uses Node.js to build the Angular application
- **Stage 2 (nginx)**: Uses lightweight Nginx to serve the built static files
- **Multi-stage benefit**: Final image only contains Nginx and built files, not Node.js or source code











## Step 12: Create Nginx Configuration

Create `nginx.conf`:
```nginx
events {
    worker_connections 1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;

        root   /usr/share/nginx/html;
        index  index.html index.htm;

        # Handle Angular routing
        location / {
            try_files $uri $uri/ /index.html;
        }

        # Enable gzip compression
        gzip on;
        gzip_vary on;
        gzip_min_length 1024;
        gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        # Security headers
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header X-Content-Type-Options "nosniff" always;

        # Error pages
        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }
}
```











## Step 13: 🔨 Build Docker Image
*Compile the multi-stage Dockerfile into an optimized image*

```bash
docker build -t angular-docker-app .
```

Check image size:
```bash
docker images | grep angular-docker-app
```











## Step 14: 🚀 Run Angular Container
*Launch the Angular application with Nginx web server*

```bash
docker run -d -p 8080:80 --name angular-app angular-docker-app
```

Verify container is running:
```bash
docker ps
```











## Step 15: 🧪 Test the Application
*Verify the Angular application is working correctly*

Open browser to `http://localhost:8080`

Test with curl:
```bash
curl http://localhost:8080
```











## Step 16: Check Container Logs

```bash
docker logs angular-app
```











## Step 17: Create Docker Compose

Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  angular-app:
    build: .
    ports:
      - "8080:80"
    environment:
      - NODE_ENV=production
    restart: unless-stopped

  # Optional: Add a reverse proxy
  nginx-proxy:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      # Works for both Mac/Linux and Windows
      - ./proxy.conf:/etc/nginx/nginx.conf
    depends_on:
      - angular-app
```











## Step 18: Development with Docker Compose

Create `docker-compose.dev.yml`:
```yaml
version: '3.8'
services:
  angular-dev:
    image: node:18-alpine
    working_dir: /app
    ports:
      - "4200:4200"
    volumes:
      # Works for both Mac/Linux and Windows
      - .:/app
      - /app/node_modules
    command: sh -c "npm install && npm start -- --host 0.0.0.0"
    environment:
      - NODE_ENV=development
```

Run development environment:

**For Mac/Linux:**
```bash
docker-compose -f docker-compose.dev.yml up
```

**For Windows:**
```cmd
docker-compose -f docker-compose.dev.yml up
```

**Alternative (newer Docker versions):**
```bash
docker compose -f docker-compose.dev.yml up
```











## Step 19: Optimize Docker Image

Create `.dockerignore`:
```
node_modules
npm-debug.log
.git
.gitignore
README.md
.env
.nyc_output
coverage
.nyc_output
.vscode
```

Rebuild optimized image:
```bash
docker build -t angular-docker-app:optimized .
```

Compare sizes:
```bash
docker images | grep angular-docker-app
```











## Step 20: Health Check

Add health check to Dockerfile:
```dockerfile
# Add this to the nginx stage
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```

Rebuild and run:
```bash
docker build -t angular-docker-app:health .
docker run -d -p 8080:80 --name angular-app-health angular-docker-app:health
```

Check health status:
```bash
docker ps
```











## Step 21: Cleanup

Stop and remove containers:
```bash
docker stop angular-app angular-app-health
docker rm angular-app angular-app-health
```

Remove images:
```bash
docker rmi angular-docker-app angular-docker-app:optimized angular-docker-app:health
```

---

## Key Learning Points

1. **Multi-Stage Builds**: Optimize final image size by separating build and runtime environments
2. **Nginx Configuration**: Serve Single Page Applications with proper routing support
3. **Development vs Production**: Different Docker setups for different environments
4. **Static Asset Optimization**: Gzip compression and security headers
5. **Health Checks**: Monitor container health status
6. **Docker Compose**: Orchestrate both development and production environments
7. **Image Optimization**: Use .dockerignore to reduce build context

---

**Angular Example Complete!** ✅