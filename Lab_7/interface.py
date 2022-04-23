from university import *
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("University")
root.minsize(400, 200)

# Comandi:
# add/get/register student (interfaccia)
# add/get course (interfaccia)
# get students/courses (menu)


# -- Variabili --
title = StringVar()
universityName = StringVar()
rectorName = StringVar()
rectorSurname = StringVar()
studentName = StringVar()
studentSurname = StringVar()
studentId = StringVar()
courseTitle = StringVar()
courseTeacher = StringVar()
courseId = StringVar()


uni = University("PoliTo")
universityName.set(uni.get_name())

# -- Funzioni --
def submit_rector_name():
    global uni
    uni.set_rector(rectorName.get(), rectorSurname.get())
    window.destroy()
    root.attributes('-topmost', True)

def set_rector():
    window = Toplevel(root)
    window.title("Rector name")
    window.attributes('-topmost', True)

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    text = ttk.Label(frame, text="Insert rector name:")
    text.grid(row=0, column=0, sticky="w")

    textEntry = ttk.Entry(frame, textvariable=rectorName)
    textEntry.grid(row=1, column=0)
    textEntry.focus_set()

    text = ttk.Label(frame, text="Insert rector surname:")
    text.grid(row=2, column=0, sticky="w", pady=(20, 0))

    textEntry = ttk.Entry(frame, textvariable=rectorSurname)
    textEntry.grid(row=3, column=0)
    textEntry.focus_set()

    button = ttk.Button(frame, text="Set name", command=submit_rector_name)
    button.grid(row=4, column=0, pady=(20, 0))


    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()

def get_rector():  #TODO: compila
    global uni
    print(uni.get_rector())

def get_students():
    window = Toplevel(root)
    window.title("Students list")
    window.attributes('-topmost', True)

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    text = ttk.Label(frame, text="Insert course id:")
    text.grid(row=0, column=0, sticky="w")

    textEntry = ttk.Entry(frame, textvariable=courseId)
    textEntry.grid(row=1, column=0)
    textEntry.focus_set()

    button = ttk.Button(frame, text="Get students", command=get_students_list)
    button.grid(row=2, column=0, pady=(20, 0))

    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()

def get_courses():
    window = Toplevel(root)
    window.title("Courses list")
    window.attributes('-topmost', True)

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    text = ttk.Label(frame, text="Insert student id:")
    text.grid(row=0, column=0, sticky="w")

    textEntry = ttk.Entry(frame, textvariable=studentId)
    textEntry.grid(row=1, column=0)
    textEntry.focus_set()

    button = ttk.Button(frame, text="Get courses", command=get_courses_list)
    button.grid(row=2, column=0, pady=(20, 0))

    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()

def get_student():
    window = Toplevel(root)
    window.title("Student info")
    window.attributes('-topmost', True)

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    text = ttk.Label(frame, text="Insert student id:")
    text.grid(row=0, column=0, sticky="w")

    textEntry = ttk.Entry(frame, textvariable=studentId)
    textEntry.grid(row=1, column=0)
    textEntry.focus_set()

    button = ttk.Button(frame, text="Get info", command=get_student_info)
    button.grid(row=2, column=0, pady=(20, 0))

    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()

def get_course():
    window = Toplevel(root)
    window.title("Course info")
    window.attributes('-topmost', True)

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    text = ttk.Label(frame, text="Insert course id:")
    text.grid(row=0, column=0, sticky="w")

    textEntry = ttk.Entry(frame, textvariable=courseId)
    textEntry.grid(row=1, column=0)
    textEntry.focus_set()

    button = ttk.Button(frame, text="Get info", command=get_students_list)
    button.grid(row=2, column=0, pady=(20, 0))

    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()

def get_student_info():
    global uni
    print(uni.get_student_info(int(studentId.get())))

def get_course_info():
    global uni

def get_students_list():
    global uni
    students = uni.get_attendees(int(courseId.get())).split("\n")
    print(students)

def get_courses_list():
    global uni
    courses = uni.get_study_plan(int(studentId.get()))
    print(courses)

def add_student():
    global uni
    uni.add_student(studentName.get(), studentSurname.get())
    studentName.set("")
    studentSurname.set("")


# -- Grafica --

# - Finestra principale
menubar = Menu(root)
root['menu'] = menubar
menu_file = Menu(menubar, tearoff=0)
rector_menu = Menu(menu_file, tearoff=0)
info_menu = Menu(menu_file, tearoff=0)
menubar.add_cascade(menu=menu_file, label='Options')
menu_file.add_cascade(menu=rector_menu, label="Rector")
rector_menu.add_command(label='Set Rector', command=set_rector)
rector_menu.add_command(label='Get Rector', command=get_rector)
menu_file.add_separator()
menu_file.add_cascade(menu=info_menu, label="Get info")
info_menu.add_command(label="Student", command=get_student)
info_menu.add_command(label="Course", command=get_course)
menu_file.add_separator()
menu_file.add_command(label="Get students", command=get_students)
menu_file.add_command(label="Get courses", command=get_courses)

name = ttk.Label(root, textvariable=universityName, font=("", 14))
name.grid(row=0, column=0, sticky="we")

frameMain = ttk.Frame(root)
frameMain.grid(row=1, column=0, padx=20, pady=20)

studentFrame = ttk.Frame(frameMain)
studentFrame.grid(row=0, column=0)

label = ttk.Label(studentFrame, text="Student's name:")
label.grid(row=0, column=0, sticky="w")
entry = ttk.Entry(studentFrame, textvariable=studentName)
entry.grid(row=0, column=1, padx=(20, 0))

label = ttk.Label(studentFrame, text="Student's surname:")
label.grid(row=1, column=0, sticky="w")
entry = ttk.Entry(studentFrame, textvariable=studentSurname)
entry.grid(row=1, column=1, padx=(20, 0), pady=20)

button = ttk.Button(studentFrame, text="Add", command=add_student)
button.grid(row=2, column=1, sticky="e")


# Centro la finestra
root.update()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
rootWidth = root.winfo_width()
rootHeight = root.winfo_height()
root.geometry(f"+{int((screenWidth/2)-(rootWidth/2))}+{int((screenHeight/2)-(rootHeight/2))}")
root.update()


root.mainloop()
