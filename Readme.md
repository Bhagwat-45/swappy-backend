# Swappy

## Project Overview

Swappy is a centralized platform designed to facilitate academic collaboration, resource sharing, and real-time technical engagement for students. This repository contains the core backend services for the first phase of the Minimum Viable Product (MVP).

## MVP Phase 1 Scope

The initial release focuses on four primary pillars:

- **Profile Creation and Identity Management**: Establishing the foundation for student skill profiling.
- **Assignment Exchange**: A repository for sharing and collaborating on academic projects.
- **Real-Time War Room**: A collaborative environment for live coding and performance monitoring.
- **Student Tech News**: Curated updates regarding emerging technologies and industry trends.

## Technology Stack

- **Primary Framework**: FastAPI (Python)
- **Database**: PostgreSQL
- **Real-Time Communication**: WebSockets
- **Containerization**: Docker / Docker Compose
- **Environment Management**: Python Virtual Environment (venv)

## Installation and Setup

### Prerequisites

- Python 3.9 or higher
- Git

### Automated Installation

To ensure consistency across the development team, an automated setup script is provided. This script creates a virtual environment, upgrades the package manager, and installs all dependencies listed in `requirements.txt`.

1. **Clone the repository:**

```bash
git clone https://github.com/[USERNAME]/swappy-backend.git
cd swappy-backend
```

2. **Run the installation script:**

```bash
python install.py
```

3. **Activate the virtual environment:**

   **Windows:**
   ```bash
   .\venv\Scripts\activate
   ```

   **MacOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

## Running the Application

Once the virtual environment is activated, the server can be started using Uvicorn. The `--reload` flag is recommended for local development to enable automatic restarts upon code changes.

```bash
uvicorn app.main:app --reload
```

The API documentation (Swagger UI) will be available at:

**http://127.0.0.1:8000/docs**

## Project Structure

```
swappy-backend/
├── app/
│   ├── api/          # Feature-specific endpoints (Auth, Assignments, War Room, News)
│   ├── core/         # Configuration and global security settings
│   ├── models/       # Database schemas and ORM definitions
│   ├── schemas/      # Pydantic data validation models
│   └── main.py       # Application entry point
├── install.py        # Automated environment setup script
├── docker-compose.yml # Container orchestration
├── requirements.txt  # Python dependencies
└── .gitignore        # Version control exclusion rules
```

## Collaboration Guidelines

### Branching Strategy

Direct commits to the `main` branch are restricted. All contributors must follow the feature-branch workflow:

1. Pull the latest changes from `main`.
2. Create a new branch for the specific feature (e.g., `feature/assignment-logic`).
3. Commit changes with clear, descriptive messages.
4. Push the branch to the remote repository and open a Pull Request (PR).

### Pull Requests

- All code must be reviewed and approved by **one required reviewer** before being merged into the `main` branch.
- Ensure that the application starts successfully and passes basic validation before submitting a PR.