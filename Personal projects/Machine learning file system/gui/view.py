from tkinter import *
from tkinter import ttk


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._controller.set_view(self)

        # Stile
        # style = ttk.Style(self)
        # style.configure("TButton", padding=6, relief="flat", background="#efefef")
        # style.map('TButton', background=[('active', 'red')])

        # Assets
        self._folder_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\folder.png")
        self._file_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\file.png")

        # Impostazioni finestra
        self.title("File System")
        self["background"] = "#efefef"

        # Grafica
        self._toolbar = Frame(self)
        self._toolbar.grid(row=0, column=0, padx=10, pady=10)

        self._main = Frame(self, background="#efefef")
        self._main.grid(row=1, column=0, padx=10, pady=10)

        # Inizializzazione
        self.initialize()

    def initialize(self):
        self._controller.update()

    def create(self, name, file_format, index):
        if file_format == "folder":
            image = self._folder_image
        else:
            image = self._file_image

        b = Button(self._main, text=name, image=image, width=60, height=60, compound=TOP, background="#efefef", borderwidth=0, command= lambda item=index: self._controller.update(index))
        self.changeOnHover(b, "#D6EAF8", "#efefef")
        b.grid(row=0, column=index, padx=5, pady=5)

        # b = ttk.Button(self._main, text=name, image=image, width=10, compound=TOP)
        # b.grid(row=0, column=index, padx=10, pady=10)

    def changeOnHover(self, button, colorOnHover, colorOnLeave):

        # adjusting backgroung of the widget
        # background on entering widget
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))

        # background color on leving widget
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))
