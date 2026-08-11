from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Student Details Management API")

#1. In-Memoery Database
students_db = {
    1:{"name": "Sruthi", :age:21, "course": "Data Science"},
    2:{"name": "Mahek",  :age:22, "course": "Web Development"}
    3:{"name": "payal", :age:23, "course": "AI & ML"} 
}

==========================================
READ (GET) - View All or Filter by Course
==========================================

#2. Data Validation Model
class Student(BaseModel):
    name: str
    age: int
    course: str

@app.get("/students/")
def get_students(course: str = None):
    if course:
        filtered = {
            s_id: s
            for s_id, s in students_db.items()
            if s["course"].lower() == course.lower()
        }
        return filtered

    return students_db
