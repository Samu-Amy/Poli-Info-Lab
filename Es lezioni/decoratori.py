def decor_name(funct):

    def inner(*args):
        print("Lo studente si chiama: ", end="")
        funct(*args)
        print()

    return inner

def decor_age(funct):

    def inner(*args):
        print("Lo studente ha: ", end="")
        funct(*args)
        print(" anni.\n")

    return inner

def decor(funct):

    def inner(*args):
        name, age = funct(*args)
        print(f"Lo studente si chiama {name} ed ha {age} anni.")

    return inner


class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @decor_name
    def get_name(self):
        print(self._name, end="")

    @decor_age
    def get_age(self):
        print(self._age, end="")

    @decor
    def get(self):
        return self._name, self._age


student = Student("Joe", 21)
# student.get_name()
# student.get_age()
# print()
student.get()


# def greet():
#     print("Hello")
#
#
# def repeat_ten_times(func):
#
#     def inner():
#         print("Esecuzione della funzione 10 volte:")
#         for i in range(10):
#             func()
#
#     return inner
#
# @repeat_ten_times
# def saluta():
#     print("Ciao")
#
#
# greet()
#
# repeat = repeat_ten_times(greet)
# repeat()
#
# saluta()