from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Define the Pydantic model for the task
class TaskCreate(BaseModel):
    title: str
    done: bool = False

class TaskUpdate(BaseModel):
    title: str | None = None
    done: bool | None = None

# Initialize the FastAPI app
app = FastAPI(
    name="Task API",
    version="1.0",
    description="A simple CRUD API built for Week 2 assignment."
)

# STAGE 2: In-memory Database
tasks = [
    {"id": 1, "title": "Learn FastAPI basics", "done": True},
    {"id": 2, "title": "Build a CRUD API", "done": False},
    {"id": 3, "title": "Master status codes", "done": False}
]

# STAGE 0 & 1: Root & Health Endpoints
@app.get("/")
async def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"] } 

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# STAGE 2: Read Endpoints
@app.get("/tasks")
def get_task():
    return tasks

# 1. STATIC ROUTE FIRST (Must be above {id})
@app.get("/tasks/filter")
def get_tasks(done: bool | None = None, search: str | None = None):
    task_copy = tasks 
    if done is not None:
        task_copy = [task for task in task_copy if task["done"] == done]
    if search is not None:
        task_copy = [task for task in task_copy if search.lower() in task["title"].lower()]
    return task_copy

# STAGE 3: Create: POST a new task
@app.post("/tasks", status_code=201)
def create_task(task_data: TaskCreate):
    if not task_data.title or not task_data.title.strip():
        return JSONResponse(status_code=400, content={"Bad Request": "Title is required and cannot be empty"})
    new_task = {
        "id": tasks[-1]['id'] + 1 if tasks else 1,
        "title": task_data.title,
        "done": False
    }
    tasks.append(new_task)
    return new_task

# STAGE 4: Update a Task
@app.put("/tasks/{id}")
def update_task(id: int, task_data: TaskUpdate):
    task = next((task for task in tasks if task["id"] == id), None)
    if not task:
        return JSONResponse(status_code=404, content={"error": f"Unknown ID"})
    if task_data.title is None and task_data.done is None:
        return JSONResponse(status_code=400, content={"error": "Empty body"})

    if task_data.title is not None:
        if not task_data.title.strip():
            return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})
        task["title"] = task_data.title.strip()

    if task_data.done is not None:
        task["done"] = task_data.done

    return task

# 2. DYNAMIC ROUTE SECOND
@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    task = next((task for task in tasks if task["id"] == id), None)
    if task is None:
        return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})
    return task

# Extra Endpoints
@app.get("/stats")
def get_stats():
    total_task = len(tasks)
    done_task = len([task for task in tasks if task["done"]== True])
    open_task = len([task for task in tasks if task["done"]== False])
    return {"total": total_task, "done": done_task, "open": open_task}

@app.post("/reset")
def reset_tasks():
    tasks.clear()
    tasks.extend([
        {"id": 1, "title": "Learn FastAPI basics", "done": True},
        {"id": 2, "title": "Build a CRUD API", "done": False},
        {"id": 3, "title": "Master status codes", "done": False}
    ])
    return {"message": "Database reset successfully", "tasks": tasks}