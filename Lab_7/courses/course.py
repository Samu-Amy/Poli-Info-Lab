class Course:

    def __init__(self, title: str, teacher: str) -> None:
        self._title = title
        self._teacher = teacher
        self._courseCode = None
        self._courseStudentsList = []
        self._studentInfo = None
        self._string = ""

    def set_course_code(self, code: int) -> None:
        self._courseCode = code

    def get_course_info(self) -> tuple:
        return self._courseCode, self._title, self._teacher

    def register(self, student: object) -> None:
        self._courseStudentsList.append(student)

    def get_students(self) -> str:
        self._string = ""
        for index in range(len(self._courseStudentsList)):
            self._studentInfo = self._courseStudentsList[index].get_student_info()
            self._string += f"{self._studentInfo[0]} {self._studentInfo[1]} {self._studentInfo[2]}"
            if index < len(self._courseStudentsList) - 1:
                self._string += "\n"

        return self._string
