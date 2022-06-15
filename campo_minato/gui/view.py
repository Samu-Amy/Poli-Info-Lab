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
        self._flag = False
        self._pressed = set()

        # Grafica
        self.title("Minesweeper")

        self._game_frame = ttk.Frame(self)
        self._game_frame.grid(row=1, column=0)

        menubar = Menu(self)
        self["menu"] = menubar
        menu_file = Menu(menubar, tearoff=0)
        game_menu = Menu(menu_file, tearoff=0)
        menubar.add_cascade(menu=menu_file, label="Options")
        menu_file.add_cascade(menu=game_menu, label="New game")
        game_menu.add_command(label="Easy", command=lambda d=Model.SMALL: self.initialization(d))
        game_menu.add_command(label="Medium", command=lambda d=Model.MEDIUM: self.initialization(d))
        game_menu.add_command(label="Hard", command=lambda d=Model.LARGE: self.initialization(d))

        self._button_flag = Button(self, text=chr(128681), command=self.flag)
        self._button_flag.grid(row=0, column=0, padx=25, pady=5, sticky="e")
        self._default_b_color = self._button_flag.cget("background")

        # Primo avvio
        dim = Model.SMALL
        self.initialization(Model.SMALL)

    def initialization(self, dim):
        x = dim[0]
        y = dim[1]
        self._pressed = set()
        self._model.initialization(dim)

        # Rimozione elementi
        for i in range(len(self._buttons)):
            for j in range(len(self._buttons[i])):
                self._buttons[i][j].destroy()

        # Creazione tabella
        self._buttons = []
        for i in range(x):
            self._buttons.append([None]*y)

        # Disposizione elementi
        for i in range(x):
            for j in range(y):
                b = Button(self._game_frame, width=2, height=1, command=lambda r=i, c=j: self.pressed(r, c))
                self._buttons[i][j] = b
                b.grid(row=i, column=j)

    def pressed(self, i, j):
        if (i, j) not in self._pressed:
            print(i, j)  # TODO: elimina
            self._controller.pressed(i, j)
            self._pressed.add((i, j))

    def expose(self, i, j, value):
        self._buttons[i][j]["text"] = value
        self._buttons[i][j]["relief"] = "sunken"
        self._buttons[i][j]["background"] = "#bbb"
        self._buttons[i][j]["foreground"] = "#000"
        # self._buttons[i][j]["state"] = "disabled"

    def flag(self):
        self._flag = not self._flag
        if self._flag:
            self._button_flag["relief"] = "sunken"
            self._button_flag["background"] = "#f23b2c"
        else:
            self._button_flag["relief"] = "raised"
            self._button_flag["background"] = self._default_b_color

    def stampa(self):
        for i in range(len(self._buttons)):
            for j in range(len(self._buttons[i])):
                print(self._buttons[i][j], end=" ")
            print()
