# Student CRUD API

A simple Student CRUD Application built using FastAPI. This project demonstrates CRUD (Create, Read, Update, Delete) operations without using a database. Student data is stored temporarily in memory using a Python list.

---

## Features

✅ Create Student

✅ Get All Students

✅ Get Student By ID

✅ Update Student

✅ Delete Student

---

## Project Structure

```text
student_curd/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   └── studentModel.py
│
├── controllers/
│   └── studentController.py
│
└── routers/
    └── studentRouter.py
```

---

## Requirements

Install required packages:

```bash
pip install fastapi uvicorn pydantic
```

Or install from requirements file:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Open terminal inside the project folder and run:

```bash
uvicorn main:app --reload
```

If the server starts successfully, you will see:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

## Swagger API Documentation

Open your browser and visit:

```text
http://127.0.0.1:8000/docs
```

Swagger UI provides an interface to test all API endpoints.

---

## API Endpoints

| Method | Endpoint |
|----------|----------|
| POST | `/students/poststudents` |
| GET | `/students/getstudents` |
| GET | `/students/getstudent/{studentid}` |
| PUT | `/students/updatestudent/{studentid}` |
| DELETE | `/students/deletestudent/{studentid}` |

---

## How Student CRUD Works

### Create Student

Creates a new student and automatically assigns a unique ID.

Example:

```json
{
  "name": "Dev",
  "email": "dev@gmail.com",
  "course": "MSC_IT",
  "semester": 7
}
```

### Get All Students

Returns all student records stored in memory.

### Get Student By ID

Returns a specific student using the Student ID.

Example:

```text
/students/getstudent/1
```

### Update Student

Updates the information of an existing student.

### Delete Student

Deletes a student record using the Student ID.

### Storage

This project uses:

```python
students = []
```

to store data temporarily in memory.

**Note:** Since no database is used, all data is lost when the server stops.

---

## Git Commands Used

Initialize Git Repository:

```bash
git init
```

Add Project Files:

```bash
git add .
```

Create Commit:

```bash
git commit -m "Initial Student CRUD Project"
```

Set Main Branch:

```bash
git branch -M main
```

Connect GitHub Repository:

```bash
git remote add origin <repository-url>
```

Push Project to GitHub:

```bash
git push -u origin main
```

---

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git
- GitHub

---

## Author

**Dev Rijwani**

MSc IT Student