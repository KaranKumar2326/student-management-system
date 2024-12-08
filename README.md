
```markdown
# Student Management System API

This is a **Student Management System API** built with **FastAPI** and **MongoDB**. It provides endpoints to manage student records, including creating, retrieving, updating, and deleting operations.

---

## Features

- **Add Students**: Create new student records with mandatory details.
- **View Students**: Fetch a list of all students or filter them by country and age.
- **Retrieve Specific Student**: Get detailed information for a particular student by ID.
- **Update Student**: Partially update student details.
- **Remove Students**: Delete a student record from the system.

---

## Prerequisites

- **Python 3.10+**
- **MongoDB Atlas** or a local MongoDB instance.

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd student-management-system
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory with the following:
```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<database>?retryWrites=true&w=majority
```

---

## Running the Application

1. Start the FastAPI server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Open the API documentation in your browser:
   - **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## API Endpoints

### 1. Create a Student

**Endpoint**: `POST /students`

#### Request Body:
```json
{
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

#### Response:
- **Status Code**: `201 Created`
- **Body**:
```json
{
  "id": "unique_student_id"
}
```

---

### 2. List Students

**Endpoint**: `GET /students`

#### Query Parameters:
- `country` (optional): Filter students by their country.
- `age` (optional): Return students whose age is greater than or equal to the provided value.

#### Response:
- **Status Code**: `200 OK`
- **Body**:
```json
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
```

---

### 3. Fetch Student by ID

**Endpoint**: `GET /students/{id}`

#### Response:
- **Status Code**: `200 OK`
- **Body**:
```json
{
  "name": "John Doe",
  "age": 20,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}
```

---

### 4. Update a Student

**Endpoint**: `PATCH /students/{id}`

#### Request Body:
```json
{
  "name": "Jane Doe",
  "age": 21
}
```

#### Response:
- **Status Code**: `204 No Content`

---

### 5. Delete a Student

**Endpoint**: `DELETE /students/{id}`

#### Response:
- **Status Code**: `200 OK`
- **Body**:
```json
{
  "message": "Student deleted successfully"
}
```

---

## Project Structure

```
student-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point for the application
│   ├── crud.py          # Database operations logic
│   ├── models.py        # Pydantic models for validation
│   ├── schemas.py       # Response schemas for the API
│   └── routers/
│       └── student_router.py  # API routes for student operations
│
├── .env                # Environment variables (e.g., MONGO_URI)
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
```

---

## Deployment

This application can be deployed on platforms such as **Render**, **Heroku**, or **AWS**.

### Deployment Steps:
1. Push your code to a GitHub repository.
2. Set up the deployment service (e.g., Render).
3. Add the `MONGO_URI` environment variable in the deployment settings.
4. Start the application and verify using the API documentation.

---

## Testing the API

### Using Swagger UI
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to interact with the API documentation.

### Using cURL
Example for creating a student:
```bash
curl -X POST "http://127.0.0.1:8000/students" \
-H "Content-Type: application/json" \
-d '{
  "name": "John Doe",
  "age": 22,
  "address": {
    "city": "New York",
    "country": "USA"
  }
}'
```

---


