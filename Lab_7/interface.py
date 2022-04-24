from university import *
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("University")
root.minsize(400, 200)
root.columnconfigure(0, weight=1)


# -- Variabili --
title = StringVar()
universityName = StringVar()
rectorName = StringVar()
rectorSurname = StringVar()
studentName = StringVar()
studentSurname = StringVar()
studentId = StringVar()
studentId2 = StringVar()  #Per evitare che si veda la modifica nell'interfaccia
courseTitle = StringVar()
courseTeacher = StringVar()
courseId = StringVar()
courseId2 = StringVar()  #Per evitare che si veda la modifica nell'interfaccia
width1 = 15
label1 = StringVar()
label2 = StringVar()
label3 = StringVar()
labelOut1 = StringVar()
labelOut2 = StringVar()
labelOut3 = StringVar()

label1.set("Prova")
label2.set("Prova")
label3.set("Prova")
labelOut1.set("Prova")
labelOut2.set("Prova")
labelOut3.set("Prova")


uni = University("PoliTo")
universityName.set(uni.get_name())

# -- Funzioni --

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

    button = ttk.Button(frame, text="Set name", command=lambda: submit_rector_name(window))
    button.grid(row=4, column=0, pady=(20, 0))


    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()


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

    button = ttk.Button(frame, text="Get students", command=lambda: get_students_list(window))
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

    button = ttk.Button(frame, text="Get courses", command=lambda: get_courses_list(window))
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

    button = ttk.Button(frame, text="Get info", command=lambda: get_student_info(window))
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

    button = ttk.Button(frame, text="Get info", command=lambda: get_course_info(window))
    button.grid(row=2, column=0, pady=(20, 0))

    # Centro la finestra
    window.update()
    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()
    windowWidth = window.winfo_width()
    windowHeight = window.winfo_height()
    window.geometry(f"+{int((screenWidth / 2) - (windowWidth / 2))}+{int((screenHeight / 2) - (windowHeight / 2))}")
    window.update()


def submit_rector_name(window):
    global uni
    uni.set_rector(rectorName.get(), rectorSurname.get())
    window.destroy()
    root.attributes('-topmost', True)


def get_rector():  # TODO: compila
    global uni
    print(uni.get_rector())


def get_student_info(window):
    global uni
    print(uni.get_student_info(int(studentId.get())))
    studentId.set("")
    window.destroy()
    root.attributes('-topmost', True)


def get_course_info(window):
    global uni
    print(uni.get_course_info(int(courseId.get())))
    courseId.set("")
    window.destroy()
    root.attributes('-topmost', True)


def get_students_list(window):
    global uni
    print(uni.get_attendees(int(courseId.get())).split("\n"))
    courseId.set("")
    window.destroy()
    root.attributes('-topmost', True)


def get_courses_list(window):
    global uni
    print(uni.get_study_plan(int(studentId.get())))
    studentId.set("")
    window.destroy()
    root.attributes('-topmost', True)


def add_student():
    global uni
    uni.add_student(studentName.get(), studentSurname.get())
    studentName.set("")
    studentSurname.set("")


def add_course():
    global uni
    uni.add_course(courseTitle.get(), courseTeacher.get())
    courseTitle.set("")
    courseTeacher.set("")


def register():
    global uni
    uni.register_to_course(int(studentId2.get()), int(courseId2.get()))
    studentId2.set("")
    courseId2.set(" ")


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


# Main
name = ttk.Label(root, textvariable=universityName, font=("", 14), anchor="center")
name.grid(row=0, column=0, sticky="we", pady=10)

frameMain = ttk.Frame(root)
frameMain.grid(row=1, column=0, padx=20, pady=(0, 20))
frameMain.columnconfigure(1, weight=1)


# Aggiungi studente
secondaryFrame = ttk.Frame(frameMain)
secondaryFrame.grid(row=1, column=1)
secondaryFrame.rowconfigure(0, weight=1)

label = ttk.Label(secondaryFrame, text="Add student", anchor="center", font=("", 12))
label.grid(row=0, column=0, columnspan=2, sticky="we", pady=(0, 15))

label = ttk.Label(secondaryFrame, text="Student name:", width=width1)
label.grid(row=1, column=0, sticky="w")
entry = ttk.Entry(secondaryFrame, textvariable=studentName)
entry.grid(row=1, column=1, padx=(20, 0))

label = ttk.Label(secondaryFrame, text="Student surname:")
label.grid(row=2, column=0, sticky="w")
entry = ttk.Entry(secondaryFrame, textvariable=studentSurname)
entry.grid(row=2, column=1, padx=(20, 0), pady=20)

button = ttk.Button(secondaryFrame, text="Add", command=add_student)
button.grid(row=3, column=1, sticky="e")


# Aggiungi corso
secondaryFrame = ttk.Frame(frameMain)
secondaryFrame.grid(row=1, column=3)
secondaryFrame.rowconfigure(0, weight=1)

label = ttk.Label(secondaryFrame, text="Add course", anchor="center", font=("", 12))
label.grid(row=0, column=0, columnspan=2, sticky="we", pady=(0, 15))

label = ttk.Label(secondaryFrame, text="Course name:", width=width1)
label.grid(row=1, column=0, sticky="w")
entry = ttk.Entry(secondaryFrame, textvariable=courseTitle)
entry.grid(row=1, column=1, padx=(20, 0))

label = ttk.Label(secondaryFrame, text="Course teacher:")
label.grid(row=2, column=0, sticky="w")
entry = ttk.Entry(secondaryFrame, textvariable=courseTeacher)
entry.grid(row=2, column=1, padx=(20, 0), pady=20)

button = ttk.Button(secondaryFrame, text="Add", command=add_course)
button.grid(row=3, column=1, sticky="e")


# Stampa
width2 = 12
width3 = 25
secondaryFrame = ttk.Frame(frameMain)
secondaryFrame.grid(row=3, column=1)
for i in range(4):
    secondaryFrame.rowconfigure(i, weight=1)
secondaryFrame.columnconfigure(0, weight=1)
secondaryFrame.columnconfigure(1, weight=2)

label = ttk.Label(secondaryFrame, text="Informazioni", anchor="center", font=("", 12))
label.grid(row=0, column=0, columnspan=2, sticky="we", pady=(0, 15))

label = ttk.Label(secondaryFrame, textvariable=label1, width=width2, background="#374046", foreground="white")
label.grid(row=1, column=0, sticky="we", padx=(0, 20))
label = ttk.Label(secondaryFrame, textvariable=labelOut1, width=width3, background="white")
label.grid(row=1, column=1, sticky="we")

label = ttk.Label(secondaryFrame, textvariable=label2, width=width2, background="#374046", foreground="white")
label.grid(row=2, column=0, sticky="we", padx=(0, 20), pady=10)
label = ttk.Label(secondaryFrame, textvariable=labelOut2, width=width3, background="white")
label.grid(row=2, column=1, sticky="we")

label = ttk.Label(secondaryFrame, textvariable=label3, width=width2, background="#374046", foreground="white")
label.grid(row=3, column=0, sticky="we", padx=(0, 20))
label = ttk.Label(secondaryFrame, textvariable=labelOut3, width=width3, background="white")
label.grid(row=3, column=1, sticky="we")


# Registra studente
secondaryFrame = ttk.Frame(frameMain)
secondaryFrame.grid(row=3, column=3)
secondaryFrame.rowconfigure(0, weight=1)

label = ttk.Label(secondaryFrame, text="Register", anchor="center", font=("", 12))
label.grid(row=0, column=0, columnspan=2, sticky="we", pady=(0, 15))

label = ttk.Label(secondaryFrame, text="Student id:", width=width1)
label.grid(row=1, column=0, sticky="w")
entry = ttk.Entry(secondaryFrame, textvariable=studentId2)
entry.grid(row=1, column=1, padx=(20, 0))

label = ttk.Label(secondaryFrame, text="Course id:")
label.grid(row=2, column=0, sticky="w")
entry = ttk.Entry(secondaryFrame, textvariable=courseId2)
entry.grid(row=2, column=1, padx=(20, 0), pady=20)

button = ttk.Button(secondaryFrame, text="Add", command=register)
button.grid(row=3, column=1, sticky="e")



# Separatori
Frame(frameMain, height=1, background="#121212").grid(row=0, column=0, columnspan=5, sticky="we", padx=10, pady=10)
Frame(frameMain, height=1, background="#121212").grid(row=2, column=0, columnspan=5, sticky="we", padx=10, pady=10)
Frame(frameMain, height=1, background="#121212").grid(row=4, column=0, columnspan=5, sticky="we", padx=10, pady=10)
Frame(frameMain, width=1, background="#121212").grid(row=0, column=0, rowspan=5, sticky="ns", padx=10, pady=10)
Frame(frameMain, width=1, background="#121212").grid(row=0, column=2, rowspan=5, sticky="ns", padx=10, pady=10)
Frame(frameMain, width=1, background="#121212").grid(row=0, column=4, rowspan=5, sticky="ns", padx=10, pady=10)

#TODO: togli separatori, usa colori


# Centro la finestra
root.update()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
rootWidth = root.winfo_width()
rootHeight = root.winfo_height()
root.geometry(f"+{int((screenWidth/2)-(rootWidth/2))}+{int((screenHeight/2)-(rootHeight/2))}")
root.update()


root.mainloop()


# Comandi:
# register student (interfaccia)
# add/get course (interfaccia)
# get students/courses (menu)