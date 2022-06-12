from tkinter import *

class View(Tk):

    def __init__(self, model, controller):
        self._model = model
        self._controller = controller
