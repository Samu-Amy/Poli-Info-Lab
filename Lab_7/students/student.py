class Student:

    def __init__(self, name: str, surname: str) -> None:
        self._name = name
        self._surname = surname
        self._studentId = None
        self._coursesList = []
        self._courseInfo = None
        self._string = ""
        self._list = []

    def set_student_id(self, studentId: int) -> None:
        self._studentId = studentId

    def get_student_info(self) -> tuple:
        return self._studentId, self._name, self._surname

    def add_course(self, course: object) -> None:
        self._coursesList.append(course)

    def get_courses(self) -> list:
        for index in range(len(self._coursesList)):
            self._string = ""
            self._courseInfo = self._coursesList[index].get_course_info()
            self._string += f"{self._courseInfo[0]},{self._courseInfo[1]},{self._courseInfo[2]}"
            self._list.append(self._string)

        return self._list
