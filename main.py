from fastapi import FastAPI

# Initialize the FastAPI app
app = FastAPI(
    name="Task API",
    version="1.0",
    description="A simple CRUD API built for Week 2 assignment."
)

@app.get("/")
async def read_root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"] } 

@app.get("/health")
async def health_check():
    return {"status": "ok"}
