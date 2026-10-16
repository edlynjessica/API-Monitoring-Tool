# API Monitoring Tool

A backend-focused project for monitoring API availability, response times, and HTTP status codes. The goal is to build a service that allows developers to register API endpoints, trigger health checks, and inspect historical monitoring results.

## Overview

APIs are essential components of modern applications, but an endpoint may become unavailable, return unexpected HTTP status codes, or respond more slowly than expected.

This project aims to simplify API health monitoring by providing a centralized service to check registered endpoints and record their results.

The project will be developed incrementally, starting with a minimal working backend and gradually evolving into a more reliable monitoring system.

## Planned Features

- Register API endpoints for monitoring
- View and manage registered endpoints
- Trigger manual health checks
- Record HTTP status codes and response times
- Track successful and failed checks
- Maintain historical monitoring results
- Calculate uptime and performance metrics
- Introduce scheduled monitoring and alerts in future versions

## Planned Technology Stack

- **Language:** Python
- **Backend Framework:** FastAPI
- **Database:** PostgreSQL
- **API Testing:** Postman and automated tests
- **Version Control:** Git and GitHub

Additional technologies may be introduced as the project evolves.

## Development Roadmap

### Phase 1 — MVP Design and Backend Fundamentals
- Define requirements and scope
- Design REST API endpoints
- Plan request and response formats
- Implement core API management and manual health checks

### Phase 2 — Database Integration
- Design the database schema
- Store monitored endpoints and check results
- Implement persistent monitoring history

### Phase 3 — Authentication and Security
- Introduce user registration and authentication
- Implement authorization and ownership
- Handle errors and validate inputs securely

### Phase 4 — Automated Monitoring
- Schedule recurring health checks
- Handle timeouts and connection failures
- Record results automatically

### Phase 5 — Metrics and Optimization
- Calculate uptime and failure rates
- Analyze response-time trends
- Explore caching and background processing

### Phase 6 — Deployment and Observability
- Containerize the application
- Deploy the backend
- Add structured logging, metrics, and operational monitoring

## Project Goals

- Develop a strong understanding of backend engineering
- Apply REST API design principles
- Learn database modeling and SQL through a practical project
- Understand asynchronous processing and background jobs
- Build reliable, testable, and maintainable backend software

## Project Status

**Currently in planning and design.**

Features listed above represent the intended roadmap and are not necessarily implemented.

## Future Scope

Potential extensions include configurable monitoring intervals, response validation, uptime reports, alert notifications, and a dashboard for visualizing monitoring history.
