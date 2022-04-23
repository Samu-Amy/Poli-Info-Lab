from typing import List
from students import *
from courses import *


class University:

    # R1
    def __init__(self, name: str) -> None:
        self._name = name
        self._rectorName = ""
        self._rectorSurname = ""
        self._studentsNumber = 10000
        self._studentsList = []
        self._coursesNumber = 10
        self._coursesList = []

        # Variabili "secondarie"
        self._student = None
        self._course = None
        self._temp = None
        self._studentInfo = None
        self._courseInfo = None

    def get_name(self) -> str:
        return self._name

    def set_rector(self, name: str, surname: str) -> None:
        self._rectorName = name
        self._rectorSurname = surname

    def get_rector(self) -> str:
        return self._rectorName + " " + self._rectorSurname

    # R2
    def add_student(self, name: str, surname: str) -> int:
        self._student = Student(name, surname)
        self._temp = self._studentsNumber
        self._student.set_student_id(self._temp)
        self._studentsList.append(self._student)
        self._studentsNumber += 1
        return self._temp

    def get_student_info(self, student_id: int) -> str:
        for student in self._studentsList:
            self._studentInfo = student.get_student_info()
            if self._studentInfo[0] == student_id:
                return f"{self._studentInfo[0]} {self._studentInfo[1]} {self._studentInfo[2]}"

    # R3
    def add_course(self, title: str, teacher: str) -> int:
        self._course = Course(title, teacher)
        self._temp = self._coursesNumber
        self._course.set_course_code(self._temp)
        self._coursesList.append(self._course)
        self._coursesNumber += 1
        return self._temp

    def get_course_info(self, course_id: int) -> str:
        for course in self._coursesList:
            self._courseInfo = course.get_course_info()
            if self._courseInfo[0] == course_id:
                return f"{self._courseInfo[0]},{self._courseInfo[1]},{self._courseInfo[2]}"

    # R4
    def register_to_course(self, student_id: int, course_id: int) -> None:
        for student in self._studentsList:
            self._studentInfo = student.get_student_info()
            if self._studentInfo[0] == student_id:
                for course in self._coursesList:
                    self._courseInfo = course.get_course_info()
                    if self._courseInfo[0] == course_id:
                        course.register(student)
                        student.add_course(course)

    def get_attendees(self, course_id: int) -> str:
        for course in self._coursesList:
            self._courseInfo = course.get_course_info()
            if self._courseInfo[0] == course_id:
                return course.get_students()

    def get_study_plan(self, student_id: int) -> List[str]:
        for student in self._studentsList:
            self._studentInfo = student.get_student_info()
            if self._studentInfo[0] == student_id:
                return student.get_courses()
