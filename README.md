# 🚀 API Monitoring Tool

<p align="center">
  A backend-driven API monitoring system to track endpoint availability, HTTP status codes, and response times.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Pytest-Testing-0A9EDC?logo=pytest&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-In%20Development-orange" />
</p>

---

## 📌 Overview

APIs are critical components of modern applications. However, endpoints can become unavailable, return unexpected HTTP responses, or experience increased response times.

The **API Monitoring Tool** is a backend application designed to monitor registered API endpoints, execute health checks, and maintain a history of monitoring results.

The project follows a layered architecture, separating API routes, business logic, database operations, and data models to keep the application modular and maintainable.

## ✨ Features

- Register and manage API endpoints
- Retrieve registered endpoints
- Trigger manual HTTP health checks
- Measure API response times
- Capture HTTP status codes
- Identify successful and failed requests
- Store monitoring results in PostgreSQL
- Retrieve historical check records
- Handle connection failures and request timeouts

## 🛠️ Technology Stack

| Category | Technology |
|---|---|
| Language | Python |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Database Driver | Psycopg |
| HTTP Client | HTTPX |
| Validation | Pydantic |
| Configuration | python-dotenv |
| Testing | Pytest, Postman |
| Version Control | Git, GitHub |

## 🏗️ Architecture

The application follows a layered backend architecture:

```text
                 Client / Postman
                        |
                        v
                  FastAPI Routes
                        |
                        v
                   Repositories
                        |
             +----------+----------+
             |                     |
             v                     v
         PostgreSQL          Monitoring Service
                                   |
                                   v
                              HTTPX Client
                                   |
                                   v
                            External APIs
```

**Project Structure**

```text
API-Monitoring-Tool/
│
├── src/
│   ├── main.py
│   ├── database.py
│   ├── dependencies.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── endpoint.py
│   │   └── check.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── endpoint.py
│   │   └── check.py
│   │
│   ├── routes/
│   │   ├── endpoints.py
│   │   └── checks.py
│   │
│   ├── repositories/
│   │   ├── endpoint_repository.py
│   │   └── check_repository.py
│   │
│   └── services/
│       └── monitoring_service.py
│
├── tests/
│   ├── conftest.py
│   ├── test_models.py
│   ├── test_endpoint_repository.py
│   ├── test_check_repository.py
│   └── test_monitoring_service.py
│
├── .env
├── .gitignore
└── requirements.txt
```

## 🔌 API Endpoints

Base URL: `http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/endpoints/` | Register an endpoint |
| GET | `/endpoints/` | Retrieve all endpoints |
| GET | `/endpoints/{id}` | Retrieve an endpoint |
| DELETE | `/endpoints/{id}` | Delete an endpoint |
| POST | `/endpoints/{id}/checks` | Trigger a health check |
| GET | `/endpoints/{id}/checks` | Retrieve check history |
| GET | `/endpoints/{id}/checks/{check_id}` | Retrieve a specific check |

Interactive API documentation is available through Swagger UI:

`http://127.0.0.1:8000/docs`

## 🗄️ Database Design

The application currently uses three PostgreSQL tables:

- **users** — stores user information
- **endpoints** — stores registered API endpoints
- **checks** — stores individual monitoring results

Relationships:

```text
Users (1) ───────── (*) Endpoints
                            |
                            |
                            v
                       Checks (*)
```

Each user can register multiple endpoints, and each endpoint can have multiple monitoring records.

## ⚙️ Getting Started

### Prerequisites

- Python 3.13+
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/edlynjessica/API-Monitoring-Tool.git
cd API-Monitoring-Tool
```

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=api_monitoring
DB_USER=postgres
DB_PASSWORD=your_postgres_password
```

Create the PostgreSQL database and required tables before starting the application. The current setup uses a manually created database schema.

**Security:** Never commit `.env` or database credentials to GitHub.

### 5. Start the application

```powershell
python -m uvicorn src.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

### 6. Run automated tests

```powershell
python -m pytest -v
```

## 🧪 Testing

The project includes automated tests for:

- SQLAlchemy model mappings
- Endpoint repository operations
- Check repository operations
- Monitoring service behaviour
- Successful HTTP responses
- Server-side HTTP errors
- Network failures

API routes have also been manually verified using Postman.

## 📍 Development Progress

**Current milestone: V1 Backend — Core Functionality**

- [x] PostgreSQL database design and setup
- [x] SQLAlchemy models
- [x] Database connection and session management
- [x] Repository layer
- [x] Monitoring service using HTTPX
- [x] FastAPI application and routing
- [x] Endpoint management routes
- [x] Manual health-check execution
- [x] Monitoring history retrieval
- [x] Automated repository and service tests
- [x] Manual API testing using Postman

## 🗺️ Roadmap

### V1 — Backend Foundation
- [x] Database integration
- [x] Endpoint management
- [x] Manual monitoring
- [x] Monitoring history
- [x] Automated tests

### V2 — Application Expansion
- [ ] User registration and authentication
- [ ] JWT-based authorization
- [ ] Multi-user endpoint ownership
- [ ] Scheduled health checks
- [ ] Background monitoring
- [ ] Uptime and performance analytics
- [ ] Alert notifications

### V3 — Frontend and Deployment
- [ ] Interactive monitoring dashboard
- [ ] Endpoint management interface
- [ ] Monitoring history visualization
- [ ] Response-time and uptime charts
- [ ] Backend and frontend integration
- [ ] Dockerization and deployment
- [ ] Production logging and observability

## 🎯 Project Goals

- Apply backend engineering principles through a practical project.
- Build modular REST APIs using FastAPI.
- Understand relational database design and ORM integration.
- Implement reliable HTTP monitoring and error handling.
- Develop testable and maintainable backend systems.
- Explore authentication, background processing, and application deployment.

---

<p align="center">
  Built with Python, FastAPI, and PostgreSQL.
</p>