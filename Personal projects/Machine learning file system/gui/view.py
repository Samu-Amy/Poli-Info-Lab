from tkinter import *
from tkinter import ttk


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._controller.set_view(self)

        self._folder_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\folder.png")
        self._file_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\file.png")

        self.title("File System")

        self._main = ttk.Frame(self)
        self._main.grid(row=0, column=0, padx=10, pady=10)

        # b = ttk.Button(self._main, text="Folder", image=self._folder_image, width=10, compound=TOP)
        # b.grid(row=0, column=0, padx=10, pady=10)

        self.initialize()

    def initialize(self):
        self._controller.update()

    def create(self, name, file_format, index):
        if file_format == "folder":
            image = self._folder_image
        else:
            image = self._file_image

        b = ttk.Button(self._main, text=name, image=image, width=10, compound=TOP)
        b.grid(row=0, column=index, padx=10, pady=10)
