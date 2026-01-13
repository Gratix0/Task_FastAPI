# Task FastAPI

Task Management API built with **FastAPI**.  
This project is a pet project focused on applying backend best practices and common production patterns.

## Tech Stack
- Python
- FastAPI
- Pydantic
- SQLAlchemy (async)
- PostgreSQL
- Alembic
- Docker / docker-compose
- Pytest

## Getting Started

### 1. Clone the repository
Clone the project and navigate to the project directory.

```bash
git clone https://github.com/Gratix0/Task_FastAPI.git
cd Task_FastAPI
```
### 2. Configure environment variables
Create a .env file based on the provided example.

```bash
cp .env.example .env
```

### 3. Build and run the application
Start the application using Docker and docker-compose.
```bash
docker-compose up --build
```

### 4. Apply database migrations
Apply all Alembic migrations to the database.
```bash
alembic upgrade head
```

### 5. Run tests
Run the test suite to verify that everything works correctly.
```bash
pytest
```
