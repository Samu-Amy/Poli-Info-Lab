from tkinter import *
from tkinter import ttk
from gui.model import Model


class View(Tk):

    def __init__(self, model, controller):

        # Variabili
        super().__init__()
        self._model = model
        self._controller = controller
        self._buttons = []

        # Grafica
        self.title("Campo minato")

        menubar = Menu(self)
        self["menu"] = menubar
        menu_file = Menu(menubar, tearoff=0)
        game_menu = Menu(menu_file, tearoff=0)
        menubar.add_cascade(menu=menu_file, label="Options")
        menu_file.add_cascade(menu=game_menu, label="New game")
        game_menu.add_command(label="Easy", command=lambda dim=Model.SMALL: self.initialization(dim))
        game_menu.add_command(label="Medium", command=lambda dim=Model.MEDIUM: self.initialization(dim))
        game_menu.add_command(label="Hard", command=lambda dim=Model.LARGE: self.initialization(dim))

        # Primo avvio
        dim = Model.SMALL
        self.initialization(Model.SMALL)

    def initialization(self, dim):
        x = dim[0]
        y = dim[1]

        # Rimozione elementi
        print("\nRimozione:")
        for i in range(len(self._buttons)):
            for j in range(len(self._buttons[i])):
                self._buttons[i][j].destroy()

        self.stampa()

        # Creazione tabella
        print("\nCreazione:")
        self._buttons = []
        for i in range(x):
            self._buttons.append([None]*y)

        self.stampa()

        # Disposizione elementi
        print("\nDisposizione:")
        for i in range(x):
            for j in range(y):
                b = Button(self, width=2, height=1, command=lambda r=i, c=j: self.pressed(r, c))
                self._buttons[i][j] = b
                b.grid(row=i, column=j)

        self.stampa()

    def pressed(self, i, j):
        print(i, j)

    def stampa(self):
        for i in range(len(self._buttons)):
            for j in range(len(self._buttons[i])):
                print(self._buttons[i][j], end=" ")
            print()
