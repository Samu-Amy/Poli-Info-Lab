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
        self._score = 0
        self._score_var = StringVar()
        self._window = None
        self._dim_var = StringVar()

        # Grafica
        self.title("Minesweeper")
        self.geometry("+750+350")

        self._game_frame = ttk.Frame(self)
        self._game_frame.grid(row=1, column=0, columnspan=2)

        menubar = Menu(self)
        self["menu"] = menubar
        menu_file = Menu(menubar, tearoff=0)
        game_menu = Menu(menu_file, tearoff=0)
        menubar.add_cascade(menu=menu_file, label="Options")
        menu_file.add_cascade(menu=game_menu, label="New game")
        game_menu.add_command(label="Easy", command=lambda d=Model.SMALL: self.initialization(d))
        game_menu.add_command(label="Medium", command=lambda d=Model.MEDIUM: self.initialization(d))
        game_menu.add_command(label="Hard", command=lambda d=Model.LARGE: self.initialization(d))

        score = ttk.Label(self, textvariable=self._score_var)
        score.grid(row=0, column=0, padx=30, pady=5, sticky="w")
        self._button_flag = Button(self, text=chr(128681), foreground="#f23b2c", command=self.flag)
        self._button_flag.grid(row=0, column=1, padx=25, pady=5, sticky="e")
        self._default_b_color = self._button_flag.cget("background")

        # Primo avvio
        self._dim = Model.SMALL
        self.initialization(self._dim)

    def initialization(self, dim):
        x = dim[0]
        y = dim[1]
        self._dim = dim
        self._pressed = set()
        self._score = 0
        self._update_score()
        self._controller.initialization(dim)

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
            if not self._flag and self._buttons[i][j]["text"] != chr(128681):
                self._controller.pressed(i, j)
                self.check()
            elif self._flag and self._buttons[i][j]["text"] == chr(128681):
                self._buttons[i][j]["text"] = ""
                self._buttons[i][j]["foreground"] = "#000"
            else:
                self._buttons[i][j]["text"] = chr(128681)
                self._buttons[i][j]["foreground"] = "#f23b2c"

    def expose(self, i, j, value):
        self._pressed.add((i, j))
        if value == "x":
            self._buttons[i][j]["text"] = chr(128163)
            self._buttons[i][j]["background"] = "#f23b2c"
        else:
            self._score += 1
            self._update_score()
            self._buttons[i][j]["text"] = value
            self._buttons[i][j]["background"] = "#bbb"
        self._buttons[i][j]["relief"] = "sunken"
        self._buttons[i][j]["foreground"] = "#000"
        # self._buttons[i][j]["state"] = "disabled"

    def flag(self):
        self._flag = not self._flag
        if self._flag:
            self._button_flag["relief"] = "sunken"
            self._button_flag["background"] = "#f23b2c"
            self._button_flag["foreground"] = "#000"
        else:
            self._button_flag["relief"] = "raised"
            self._button_flag["background"] = self._default_b_color
            self._button_flag["foreground"] = "#f23b2c"

    def check(self):
        dim = self._dim
        total = dim[0]*dim[1]
        total_pressed = len(self._pressed)
        if total-total_pressed == dim[2]:
            self.show_message("Hai vinto", "green", True)

    def _update_score(self):
        self._score_var.set(str(self._score))

    def show_message(self, message, color, win):
        self._window = Toplevel(self)
        self._window.geometry("+840+480")
        ttk.Label(self._window, text=message, foreground=color).grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 5))
        if win:
            combobox = ttk.Combobox(self._window, textvariable=self._dim_var)
            combobox["values"] = ("Easy", "Medium", "Hard")
            combobox.set("Easy")
            combobox.state(["readonly"])
            combobox.grid(row=1, column=0, sticky="w", padx=20, pady=(5, 20))
            ttk.Button(self._window, text="New game", command=lambda dim=self._dim_var: self.new_game(dim, True)).grid(row=1, column=1, sticky="e", padx=20, pady=(5, 20))
        else:
            ttk.Button(self._window, text="Retry", command=lambda dim=self._dim: self.new_game(dim, False)).grid(row=1, column=1, sticky="e", padx=50, pady=(5, 20))

    def new_game(self, dim, get):
        if get:
            if dim.get() == "Easy":
                dim = Model.SMALL
            elif dim.get() == "Medium":
                dim = Model.MEDIUM
            elif dim.get() == "Hard":
                dim = Model.LARGE
        self._window.destroy()
        self.initialization(dim)

    def stampa(self):
        for i in range(len(self._buttons)):
            for j in range(len(self._buttons[i])):
                print(self._buttons[i][j], end=" ")
            print()
