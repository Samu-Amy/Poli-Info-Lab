from tkinter import *
from tkinter import ttk
from hydraulics.hsystem import HSystem
from hydraulics.elements import Element, Source, Tap, Sink, Split

root = Tk()
root.title("Hydraulics")

# Variabili
system = HSystem()
itemsList = {}
nameVar = StringVar()
typeVar = StringVar()
outputVar = StringVar()


# Funzioni
def submit():
    global system
    if nameVar.get() != "":
        if typeVar.get() == "Source":
            object = Source(nameVar.get())
        elif typeVar.get() == "Tap":
            object = Tap(nameVar.get())
        elif typeVar.get() == "Split":
            object = Split(nameVar.get())
        else:
            object = Sink(nameVar.get())

        system.add_element(object)
        itemsList[nameVar.get()] = typeVar.get()
        nameVar.set("")

def showElements():
    global outputVar
    string = ""
    for item in system.get_elements():
        string += f"{(item.get_name() + ':') :>15} {itemsList[item.get_name()] :<15}\n" #TODO: da sistemare
    outputVar.set(string)
    print(string)


# Grafica Input
mainFrame = ttk.Frame(root)
mainFrame.grid(row=0, column=0, padx=20, pady=(20, 0))

label = ttk.Label(mainFrame, text="Name:")
label.grid(row=0, column=0, sticky="w")
label = ttk.Label(mainFrame, text="Type:")
label.grid(row=0, column=1, sticky="w")

entry = ttk.Entry(mainFrame, textvariable=nameVar)
entry.grid(row=1, column=0, padx=(0, 20))
comboBox = ttk.Combobox(mainFrame, textvariable=typeVar)
comboBox["values"] = ("Source", "Tap", "Split", "Sink")
comboBox.state(["readonly"])
comboBox.grid(row=1, column=1)

button = ttk.Button(mainFrame, text="Submit", command=submit)
button.grid(row=2, column=1, pady=(20, 0), sticky="e")

# Grafica Output
separator = Frame(mainFrame, height=1, background="#121212")
separator.grid(row=4, column=0, columnspan=2, sticky="we", pady=20)

button = ttk.Button(mainFrame, text="Show items", command=showElements)
button.grid(row=5, column=0, columnspan=2, sticky="we")

label = ttk.Label(mainFrame, textvariable=outputVar, background="white", anchor="center")
label.grid(row=6, column=0, columnspan=2)


root.mainloop()
