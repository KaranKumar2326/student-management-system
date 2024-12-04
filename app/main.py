from fastapi import FastAPI
from app.routers.student_router import router as student_router
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Include the student router
app.include_router(student_router)

@app.get("/", tags=["Health Check"])
async def root():
    return {"message": "Student Management System is running!"}
