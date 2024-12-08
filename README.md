Student Management System - Backend API
Overview
This is a Student Management System Backend API built using FastAPI and MongoDB. It provides endpoints to manage student records, including creating, retrieving, updating, and deleting students. The API follows RESTful principles and includes features like filtering and partial updates.

Features
Create Students: Add new student records with mandatory fields.
List Students: Retrieve a list of students with optional filters.
Fetch Student by ID: Get detailed information about a specific student.
Update Students: Update specific fields of a student record.
Delete Students: Remove a student record from the database.
API Endpoints
1. Create a Student
Endpoint: POST /students

Request Body:

json
Copy code
{
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
Response:

Status: 201 Created
Body:
json
Copy code
{
  "id": "unique_student_id"
}
2. List Students
Endpoint: GET /students

Query Parameters:

country: (optional) Filter by country.
age: (optional) Filter by age greater than or equal to the provided value.
Response:

Status: 200 OK
Body:
json
Copy code
{
  "data": [
    {
      "name": "Alice",
      "age": 22
    },
    {
      "name": "Bob",
      "age": 25
    }
  ]
}
3. Fetch Student by ID
Endpoint: GET /students/{id}

Response:

Status: 200 OK
Body:
json
Copy code
{
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
4. Update Student
Endpoint: PATCH /students/{id}

Request Body (partial update allowed):

json
Copy code
{
  "name": "Jane Doe",
  "age": 21
}
Response:

Status: 204 No Content
5. Delete Student
Endpoint: DELETE /students/{id}

Response:

Status: 200 OK
Body:
json
Copy code
{
  "message": "Student deleted successfully"
}
Requirements
Prerequisites
Python 3.10+
MongoDB Atlas Cluster (or local MongoDB)
Python Dependencies
Install the required Python dependencies using:

bash
Copy code
pip install -r requirements.txt
Environment Variables
Set the following environment variables:

MONGO_URI: MongoDB connection string.
Example .env file:

php
Copy code
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<database>?retryWrites=true&w=majority
Run the Application
Locally
Start the server:
bash
Copy code
uvicorn app.main:app --reload
Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
Deployment
Render or any cloud platform supporting FastAPI.
Ensure MONGO_URI is set in environment variables during deployment.
Project Structure
graphql
Copy code
student-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application entry point
│   ├── crud.py          # Contains database CRUD operations
│   ├── models.py        # Pydantic models for request validation
│   ├── schemas.py       # Pydantic schemas for API response models
│   └── routers/
│       └── student_router.py  # API endpoints
│
├── .env                # Environment variables (MONGO_URI, etc.)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
Testing the API
Using Swagger UI
Navigate to http://127.0.0.1:8000/docs to interact with the API.
Using cURL
Example for creating a student:

bash
Copy code
curl -X 'POST' \
  'http://127.0.0.1:8000/students' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "John Doe",
    "age": 22,
    "address": {
      "city": "New York",
      "country": "USA"
    }
  }'
