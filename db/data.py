from pydantic import BaseModel, Field
from typing import Optional, List
import sqlite3



class Student(BaseModel):
    id: int = Field(..., description="The unique identifier for the student")
    name: str = Field(..., description="The name of the student")
    age: Optional[int] = Field(None, description="The age of the student")


class StudentDatabase:

    def __init__(self):
        self.connection = sqlite3.connect('students.db')
        self.create_table()
    
    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )
            ''')
    
    def create_student(self, student: Student):
        with self.connection:
            self.connection.execute('''
                INSERT INTO students (id, name, age) VALUES (?, ?, ?)
            ''', (student.id, student.name, student.age))
    
    def get_student(self, student_id: int) -> Optional[Student]:
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, name, age FROM students WHERE id = ?', (student_id,))
        row = cursor.fetchone()
        if row:
            return Student(id=row[0], name=row[1], age=row[2])
        return None
    
    def get_all_students(self) -> List[Student]:
        cursor = self.connection.cursor()
        cursor.execute('SELECT id, name, age FROM students')
        rows = cursor.fetchall()
        return [Student(id=row[0], name=row[1], age=row[2]) for row in rows]
    
    def update_student(self, student: Student):
        with self.connection:
            self.connection.execute('''
                UPDATE students SET name = ?, age = ? WHERE id = ?
            ''', (student.name, student.age, student.id))
    
    def delete_student(self, student_id: int):
        with self.connection:
            self.connection.execute('DELETE FROM students WHERE id = ?', (student_id,))
            
    def close(self):
        self.connection.close()
