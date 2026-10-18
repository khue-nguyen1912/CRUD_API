from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

# Define the Pydantic model for the task
class TaskCreate(BaseModel):
    title: str
    done: bool = False

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

@app.get("/tasks/{id}")
def get_task_by_id(id: int):
    result = next((task for task in tasks if task["id"] == id), None)
    if not result:
        return JSONResponse(status_code=404, content={"error": f"Task {id} not found"})
    return result

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

    

    

