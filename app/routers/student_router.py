# from venv import logger
from fastapi import APIRouter, HTTPException, status
from typing import Optional
# import logger
from app.schemas import StudentOut
from app.models import StudentCreate, StudentUpdate
from app.crud import create_student, list_students, get_student_by_id, update_student, delete_student

router = APIRouter()

@router.post("/students", status_code=status.HTTP_201_CREATED, response_model=dict)
async def create_student_api(student: StudentCreate):
    student_id = await create_student(student)
    return {"id": student_id}

@router.get("/students", response_model=dict)
async def list_students_api(country: Optional[str] = None, age: Optional[int] = None):
    students = await list_students(country, age)
    return {"data": students}

@router.get("/students/{student_id}", response_model=StudentOut)
async def get_student_api(student_id: str):
    student = await get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return student

@router.patch("/students/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_student_api(student_id: str, student_data: StudentUpdate):
    print(f"Received PATCH request to update student with ID: {student_id}")  # Debugging print statement
    updated = await update_student(student_id, student_data)
    
    if not updated:
        print(f"Failed to update student with ID: {student_id}")  # Debugging print statement
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    
    print(f"Successfully updated student with ID: {student_id}")  # Debugging print statement
    return None
@router.delete("/students/{student_id}", status_code=status.HTTP_200_OK)
async def delete_student_api(student_id: str):
    deleted = await delete_student(student_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    return {"message": "Student deleted successfully"}
