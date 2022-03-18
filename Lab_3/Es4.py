from tkinter import *
from tkinter import ttk


root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.title("Esercizio 4")
root.geometry("300x400+500+200")
root.rowconfigure(0, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

frame = ttk.Frame(root, width=300, height=300)
frame.grid(row=0, column=0, columnspan=4)


counter = 0
counterVar = StringVar(value=counter)

def increment(num):
    global counter
    if (counter + num) <= 100:
        counter += num
        canvas.itemconfig(progression, extent=-(counter*359/100)) # impostato a 359 perchè a 360 torna all'inizio
        counterVar.set(counter)

def decrement(num):
    global counter
    if (counter - num) >= 0:
        counter -= num
        canvas.itemconfig(progression, extent=-(counter*359/100)) # impostato a 359 perchè a 360 torna all'inizio
        counterVar.set(counter)


canvas = Canvas(frame)

backGround = canvas.create_oval(20,20,200,200, outline="white", fill="white")
progression = canvas.create_arc(20,20,200,200, start=180, extent=0, outline="orange", fill="orange")
canvas.place(x=40, y=40, anchor=NW)


textProgression = ttk.Label(root, textvariable=counterVar, font=("", 16))
textProgression.grid(row=1, column=1, columnspan=2, pady=15)


button1 = ttk.Button(root, text="+1", command= lambda: increment(1))
button1.grid(row=2, column=0, padx=(10, 5), pady=10)

button2 = ttk.Button(root, text="+2", command= lambda: increment(2))
button2.grid(row=2, column=1, padx=5, pady=10)

button3 = ttk.Button(root, text="+4", command= lambda: increment(4))
button3.grid(row=2, column=2, padx=5, pady=10)

button4 = ttk.Button(root, text="+8", command= lambda: increment(8))
button4.grid(row=2, column=3, padx=(5, 10), pady=10)


button_1 = ttk.Button(root, text="-1", command= lambda: decrement(1))
button_1.grid(row=3, column=0, padx=(10, 5), pady=10)

button_2 = ttk.Button(root, text="-2", command= lambda: decrement(2))
button_2.grid(row=3, column=1, padx=5, pady=10)

button_3 = ttk.Button(root, text="-4", command= lambda: decrement(4))
button_3.grid(row=3, column=2, padx=5, pady=10)

button_4 = ttk.Button(root, text="-8", command= lambda: decrement(8))
button_4.grid(row=3, column=3, padx=(5, 10), pady=10)


root.mainloop()
