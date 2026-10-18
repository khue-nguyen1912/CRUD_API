from fastapi import FastAPI
from fastapi.responses import JSONResponse

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

    

