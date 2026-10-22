# API Monitoring Tool

A backend-focused project for monitoring API availability, response times, and HTTP status codes. The goal is to build a service that allows developers to register API endpoints, trigger health checks, and inspect historical monitoring results.

## Overview

APIs are essential components of modern applications, but endpoints may become unavailable, return unexpected HTTP status codes, or respond more slowly than expected.

This project aims to provide a centralized service to monitor registered API endpoints and record their results. Development is incremental, starting with a database foundation and progressing toward a reliable monitoring backend.

## Planned Features

- Register, view, and manage API endpoints
- Trigger manual health checks
- Record HTTP status codes and response times
- Track successful and failed checks
- Maintain historical monitoring results
- Calculate uptime and performance metrics
- Introduce scheduled monitoring and alerts in future versions

## Technology Stack

- **Language:** Python
- **Backend:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Driver:** Psycopg
- **Configuration:** python-dotenv
- **Testing:** Automated tests and Postman
- **Version Control:** Git and GitHub

## Current Project Status

**In progress — database foundation established.**

Completed:
- Defined the initial REST API routes
- Designed the `users`, `endpoints`, and `checks` tables
- Created the tables in PostgreSQL
- Configured and tested the Python–PostgreSQL connection
- Added SQLAlchemy models for the three tables
- Added initial checks for table existence and column names

In progress:
- Database repository and service layers
- Persistent endpoint management
- Manual health-check execution

Not implemented yet:
- Complete CRUD API routes
- Authentication and authorization
- Scheduled monitoring and alerts
- Uptime metrics and deployment

## Getting Started

### Prerequisites

- Python
- PostgreSQL
- Git

### 1. Clone the repository

```bash
git clone https://github.com/edlynjessica/API-Monitoring-Tool.git
cd API-Monitoring-Tool
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=api_monitoring
DB_USER=postgres
DB_PASSWORD=your_local_postgres_password
```

Replace the example password with your local PostgreSQL password. Create the database and tables before running the current database checks.

**Security:** Never commit `.env`, passwords, or other secrets to GitHub. Ensure `.env` and `.venv/` are listed in `.gitignore`.

### 5. Run the database checks

From the repository root, with the virtual environment activated:

```powershell
python -m tests.test_db_connection
python -m tests.test_models
```

The connection check requires PostgreSQL to be running and the `.env` credentials to be correct.

## Git Workflow

This project uses small, meaningful commits to document development progress.

Before committing:

```powershell
git status
git diff
```

Stage only the files related to the milestone:

```powershell
git add <relevant-files>
git diff --cached
git commit -m "type: short description"
git push
```

Replace `<relevant-files>` with the actual paths you intend to commit. Review the staged changes before committing and never stage `.env`, `.venv/`, or secrets.

### Commit Message Convention

Follow the Conventional Commits format:

`<type>: <short description>`

Common types:

- `feat:` — add a feature
- `fix:` — fix a bug
- `test:` — add or update tests
- `refactor:` — restructure code without changing intended behavior
- `docs:` — documentation changes
- `chore:` — maintenance and tooling
- `build:` — build configuration or dependency changes

Examples:

```text
docs: document project setup and Git workflow
chore: configure Python project dependencies
feat: add PostgreSQL connection and SQLAlchemy models
test: verify database schema and model mappings
feat: register monitored endpoints
feat: execute manual endpoint health checks
fix: handle endpoint connection timeouts
```

Choose the commit type that reflects the actual changes. Don't describe a planned feature as implemented.

### Recommended Development Cycle

1. Implement one coherent change.
2. Run relevant tests and verify behavior.
3. Review `git diff` and `git status`.
4. Stage only related files.
5. Commit with a descriptive message.
6. Push to GitHub.

Prefer one focused commit per meaningful milestone rather than one commit per line of code.

## Development Roadmap

### Phase 1 — MVP and Backend Fundamentals
- Finalize requirements and REST API design
- Implement endpoint management
- Implement manual health checks

### Phase 2 — Database Integration
- Persist endpoints and check results
- Add repository and service layers
- Maintain monitoring history

### Phase 3 — Authentication and Security
- Add user registration and authentication
- Implement authorization and ownership
- Validate inputs and handle errors securely

### Phase 4 — Automated Monitoring
- Schedule recurring checks
- Handle timeouts and connection failures
- Record results automatically

### Phase 5 — Metrics and Optimization
- Calculate uptime and failure rates
- Analyze response-time trends
- Explore caching and background processing

### Phase 6 — Deployment and Observability
- Containerize and deploy the application
- Add structured logging and operational metrics

## Project Goals

- Develop strong backend engineering fundamentals
- Apply REST API design principles
- Understand relational database design and persistence
- Learn asynchronous processing and background jobs
- Build reliable, testable, maintainable software

## Future Scope

Potential extensions include configurable monitoring intervals, response validation, uptime reports, alert notifications, and a dashboard for visualizing monitoring history.
