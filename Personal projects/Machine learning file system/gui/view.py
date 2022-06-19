from tkinter import *
from tkinter import ttk


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._controller.set_view(self)
        self._buttons = []
        # self._datas = []
        self._path = StringVar()
        self._data = StringVar()

        # Assets
        self._folder_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\folder.png")
        self._file_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\file.png")
        self._back_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\back.png")

        # Impostazioni finestra
        self.title("File System")
        self["background"] = "#efefef"
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Frame
        self._toolbar = Frame(self)
        self._toolbar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="we")

        self._main = Frame(self, background="#efefef")
        self._main.grid(row=1, column=0, padx=10, pady=10, sticky="news")
        # self._main.rowconfigure(0, weight=1)
        # self._main.columnconfigure(0, weight=1)

        # Menu
        self._main_menu = Menu(self, tearoff=0)
        self._menu_new = Menu(self._main_menu, tearoff=0)
        self._main_menu.add_cascade(menu=self._menu_new, label="New")
        self._menu_new.add_command(label="Folder")
        self._menu_new.add_command(label="File")

        # Grafica toolbar
        self._back = Button(self._toolbar, image=self._back_image, command=self._controller.return_back)
        self._back.grid(row=0, column=0)
        ttk.Label(self._toolbar, textvariable=self._path).grid(row=0, column=1, padx=10)

        # Eventi
        self._main.bind("<Button-3>", self.do_popup)

        # Inizializzazione
        self.initialize()

    def initialize(self):
        self._controller.update()

    # Crea i tasti
    def create(self, name, file_format, index):

        if file_format == "folder":
            image = self._folder_image
        else:
            image = self._file_image

        button = Button(self._main, text=name, image=image, width=60, height=60, compound=TOP, background="#efefef", borderwidth=0, command=lambda: self._controller.open(index))
        self.changeOnHover(button, "#D6EAF8", "#efefef")
        self._buttons.append(button)
        button.bind("<Button-3>", lambda event, i=index: self.do_popup(i))
        button.grid(row=0, column=index, padx=5, pady=5, sticky="nw")

    # Mostra il contenuto del file
    def show(self, data, title):
        # self._data.set(data)
        data_var = StringVar()
        data_var.set("ghrer")
        window = Toplevel(self)
        window.title(title)
        data_label = ttk.Label(window, textvariable=data_var, anchor="center")
        data_label.grid(row=0, column=0, padx=5, pady=5, sticky="news")
        # self._datas.append(data)

    # Abilita o disabilita il tasto "indietro"
    def set_return_back(self, state):
        self._back["state"] = state

    # Aggiorna il percorso nella grafica
    def update_path(self, path):
        string = ""
        for index in range(len(path)):
            string += path[index].name
            if index < len(path) - 1:
                string += " > "
        self._path.set(string)

    # Elimina tutti gli elementi
    def clear(self):
        for button in self._buttons:
            button.destroy()
        # for data in self._datas:
        #     data.destroy()

    # Apre il menu (tasto destro)
    def do_popup(self, event, index=None):
        try:
            self._main_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self._main_menu.grab_release()

    # Cambio colore tasto se il mouse è in hover
    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))
