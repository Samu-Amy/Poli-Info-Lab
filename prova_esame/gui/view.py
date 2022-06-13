from tkinter import *
from tkinter import ttk


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller

        # Grafica
        self.title("Chess")

        l = ttk.Label(self, text="Scacchi")
        l.grid(row=0, column=0)
