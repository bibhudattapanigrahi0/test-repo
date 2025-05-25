from typing import Union

from fastapi import FastAPI
from db import Manager, Student

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/students/", response_model=Student)
def create_student(student: Student):
    manager = Manager()
    manager.create_student(student)
    return student

@app.get("/students/{student_id}", response_model=Student)
def read_student(student_id: int):
    manager = Manager()
    student = manager.get_student(student_id)
    if student is None:
        return {"error": "Student not found"}
    return student

@app.get("/students/", response_model=list[Student])
def read_students():
    manager = Manager()
    students = manager.get_all_students()
    return students

@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: Student):
    manager = Manager()
    existing_student = manager.get_student(student_id)
    if existing_student is None:
        return {"error": "Student not found"}
    student.id = student_id
    manager.update_student(student)
    return student

@app.delete("/students/{student_id}", response_model=Union[Student, dict])
def delete_student(student_id: int):
    manager = Manager()
    existing_student = manager.get_student(student_id)
    if existing_student is None:
        return {"error": "Student not found"}
    manager.delete_student(student_id)
    return existing_student