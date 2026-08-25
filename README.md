# Assignment API

A simple assignment API built with **Python and FastAPI** for creating and managing assignments. This project demonstrates fundamental backend development concepts, including API routing, HTTP methods, data validation, and temporary data storage.

## Project Overview

The Assignment API provides a simple way to manage assignment records through RESTful API endpoints.

The API allows users to create assignments, view all assignments, retrieve a specific assignment by its ID, and delete assignments. **Pydantic** is used to validate the information submitted to the API.

## Features

* Create new assignments
* Retrieve all assignments
* Retrieve a specific assignment by ID
* Delete assignments by ID
* Validate input data using Pydantic
* Interactive API documentation using Swagger UI
* In-memory data storage

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* Git
* GitHub

## Project Structure

```text
Assignment-API/
│
├── main.py
├── assignments.py
├── README.md
├── requirements.txt
└── .venv/
```

## Installation

### 1. Clone the Repository

Clone the project from GitHub and move into the project directory:

```bash
git clone https://github.com/Jo-p-ops/Week-2-Assignment-API.git
cd Week-2-Assignment-API
```

### 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

Install the required packages:

```bash
pip install fastapi uvicorn pydantic
```

## Running the Application

Start the FastAPI development server using:

```bash
fastapi dev main.py
```

You can also run the application with Uvicorn:

```bash
uvicorn main:app --reload
```

After starting the server, the API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive documentation.

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

The Swagger UI allows you to view and test the available API endpoints.

## API Endpoints

| Method | Endpoint            | Description                  |
| ------ | ------------------- | ---------------------------- |
| GET    | `/assignments`      | Retrieve all assignments     |
| GET    | `/assignments/{id}` | Retrieve an assignment by ID |
| POST   | `/assignments`      | Create a new assignment      |
| DELETE | `/assignments/{id}` | Delete an assignment by ID   |

## Creating an Assignment

To create a new assignment, send a `POST` request to:

```text
/assignments
```

### Request Body

```json
{
  "title": "Complete FastAPI exercise",
  "due_date": "2026-08-30",
  "done": false
}
```

### Example Response

```json
{
  "id": 1,
  "title": "Complete FastAPI exercise",
  "due_date": "2026-08-30",
  "done": false
}
```

## Retrieving All Assignments

Use the following endpoint:

```text
GET /assignments
```

### Example Response

```json
[
  {
    "id": 1,
    "title": "Complete FastAPI exercise",
    "due_date": "2026-08-30",
    "done": false
  }
]
```

## Retrieving a Single Assignment

To retrieve one assignment, provide its ID:

```text
GET /assignments/1
```

### Example Response

```json
{
  "id": 1,
  "title": "Complete FastAPI exercise",
  "due_date": "2026-08-30",
  "done": false
}
```

## Deleting an Assignment

To remove an assignment, use the DELETE endpoint:

```text
DELETE /assignments/1
```

### Example Response

```json
{
  "message": "Assignment deleted successfully"
}
```

## Data Validation

The API uses **Pydantic** to validate incoming data.

For example, the assignment title must contain at least **3 characters**.

### Invalid Request

```json
{
  "title": "Do",
  "due_date": "2026-08-30",
  "done": false
}
```

Because `"Do"` contains fewer than three characters, the API rejects the request.

### Validation Response

The API returns a `422 Unprocessable Entity` response similar to:

```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": [
        "body",
        "title"
      ],
      "msg": "String should have at least 3 characters",
      "input": "Do",
      "ctx": {
        "min_length": 3
      }
    }
  ]
}
```

## Data Storage

The current application uses **in-memory storage**.

## Author

**Joshua Kwasi Nyamekye**

DataBloom Africa — Future Code Project, Cohort 2

**Project:** Assignment API
