from .data import Student, StudentDatabase

class Manager:
    def __init__(self):
        self.db = StudentDatabase()

    def create_student(self, student: Student):
        self.db.create_student(student)

    def get_student(self, student_id: int) -> Student:
        return self.db.get_student(student_id)

    def get_all_students(self) -> list[Student]:
        return self.db.get_all_students()

    def update_student(self, student: Student):
        self.db.update_student(student)

    def delete_student(self, student_id: int):
        self.db.delete_student(student_id)

    def close(self):
        self.db.close()