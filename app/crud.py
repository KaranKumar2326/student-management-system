# from flask import logging
import logging

from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import Optional, List
from app.models import StudentCreate, StudentUpdate
from app.schemas import StudentOut
import os

# Initialize MongoDB client
MONGO_URI = os.getenv("MONGO_URI")
print(MONGO_URI)
client = AsyncIOMotorClient(MONGO_URI)


db = client.student_management  
students_collection = db.students  
 
# Helper to convert ObjectId to string
def student_helper(student) -> dict:
    return {
        "id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"]
    }

# Create a student
async def create_student(student: StudentCreate):
    student_dict = student.dict()
    result = await students_collection.insert_one(student_dict)
    return str(result.inserted_id)

# List all students
async def list_students(country: Optional[str] = None, age: Optional[int] = None) -> List[dict]:
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    
    students = []
    async for student in students_collection.find(query):
        # Return only 'name' and 'age' in the student object
        students.append({
            "name": student["name"],
            "age": student["age"]
        })
    return students

# Get student by ID
async def get_student_by_id(student_id: str) -> Optional[dict]:
    student = await students_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)
    return None

# Update student
async def update_student(student_id: str, student_data: StudentUpdate) -> bool:
    try:
        current_student = await students_collection.find_one({"_id": ObjectId(student_id)})
        
        print(f"Fetching student with ID {student_id}...")  # Debugging print statement
        if not current_student:
            print(f"Student with ID {student_id} not found.")  # Debugging print statement
            return False  # Student not found
        
        print(f"Current student data: {current_student}")  # Debugging print statement

    except Exception as e:
        print(f"Error fetching student with ID {student_id}: {e}")  # Debugging print statement
        return False

    # Step 2: Prepare the update data based on the provided fields
    update_data = {}

    print(f"Incoming student data to update: {student_data.dict()}")  # Debugging print statement

    # Only update the fields that are provided (i.e., not None)
    if student_data.name is not None:
        update_data["name"] = student_data.name
    else:
        update_data["name"] = current_student["name"]  # Keep the existing name if not updated

    if student_data.age is not None:
        update_data["age"] = student_data.age
    else:
        update_data["age"] = current_student["age"]  # Keep the existing age if not updated

    if student_data.address is not None:
        update_data["address"] = student_data.address.dict()  # Convert Address object to dict
    else:
        update_data["address"] = current_student["address"]  # Keep the existing address if not updated

    if not update_data:
        print("No data to update (all fields are None).")  # Debugging print statement
        return False  # No data to update (if all fields are None)

    print(f"Final update data: {update_data}")  # Debugging print statement

    # Step 3: Update the student in the database with the new data
    try:
        result = await students_collection.update_one(
            {"_id": ObjectId(student_id)}, {"$set": update_data}
        )

        print(f"Update result: {result}")  # Debugging print statement
        return result.modified_count > 0
    except Exception as e:
        print(f"Error updating student with ID {student_id}: {e}")  # Debugging print statement
        return False

    

# Delete student
async def delete_student(student_id: str) -> bool:
    result = await students_collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0
