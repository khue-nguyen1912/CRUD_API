# Flyrank Week 1 - Task Management API

A lightweight RESTful API built with FastAPI to manage a simple task list with full CRUD (Create, Read, Update, Delete) capabilities.

---

## Features

* Create Tasks: Add new tasks with titles.
* Read Tasks: Retrieve a list of all tasks or specific task details.
* Update Tasks: Modify task titles or mark tasks as completed (done).
* Delete Tasks: Remove tasks by ID.
* Validation: Input validation and error handling (400 Bad Request, 404 Not Found).
* Stats: Get how many tasks, how many done and how many open
* Filter: Get task by status or name
* Reset: Reset the task list to intial 3

---

## Prerequisites & Setup

### 1. Clone the Repository
git clone <your-repository-url>
cd flyrank-week1

### 2. Set Up Virtual Environment
python3 -m venv venv
source venv/bin/activate

### 3. Install Dependencies
pip install fastapi uvicorn

---

## Running the Application

Start the FastAPI development server using uvicorn:

uvicorn main:app --reload

The server will start at: http://127.0.0.1:8000

---

## API Documentation & Testing

FastAPI automatically generates interactive API documentation:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## Endpoint Summary

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /tasks | Get all tasks |
| POST | /tasks | Create a new task |
| PUT | /tasks/{id} | Update an existing task |
| DELETE | /tasks/{id} | Delete a task |

---

## Git Commands to Save README

git add README.md
git commit -m "docs: add README.md"
git push
