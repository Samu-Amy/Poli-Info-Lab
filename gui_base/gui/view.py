from tkinter import *
from tkinter import ttk


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._variable = StringVar()
        self._variable_2 = 10

        self.title("Interfaccia")

        label = ttk.Label(self, text="Label")
        label.grid(row=0, column=0)

        entry = ttk.Entry(self, textvariable=self._variable)
        entry.grid(row=1, column=0)

        button = ttk.Button(self, text="Submit", command=lambda i=self._variable_2: self._controller.function(i))
        button.grid(row=3, column=0, pady=(20, 0), sticky="w")

    def reset_var(self):
        self._variable.set("")
