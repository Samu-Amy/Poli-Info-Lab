from tkinter import *
from tkinter import ttk, messagebox
from elements import Desktop, Folder, File


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._controller.set_view(self)
        self._buttons = []
        self._path = StringVar()
        self._path_mod = StringVar()

        # Colori
        self._back_color = "#fff"
        self._light_blue = "#d0f0ff"

        # Layout
        self._rows = 0
        self._max = 10
        self._current_multiple = 0
        self._multiples = []
        for i in range(50):
            self._multiples.append(self._max * i)

        # Asset

        # Percorsi desktop
        # self._window_icon = r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\deep_learning.ico"
        # self._folder_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\folder.png")
        # self._add_folder_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\add_folder.png")
        # self._file_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\file.png")
        # self._add_file_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\add_file.png")
        # self._back_image = PhotoImage(file=r"D:\Download\Lezioni\Materiale studio\Secondo anno\Secondo semestre\Algoritmi e programmazione a oggetti\Repository info lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\back.png")

        # Percorsi laptop
        self._window_icon = r"C:\Users\LENOVO\Desktop\Studio\Secondo anno - secondo semestre\Algoritmi e programmazione a oggetti\Repository lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\deep_learning.ico"
        self._folder_image = PhotoImage(file=r"C:\Users\LENOVO\Desktop\Studio\Secondo anno - secondo semestre\Algoritmi e programmazione a oggetti\Repository lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\folder.png")
        self._add_folder_image = PhotoImage(file=r"C:\Users\LENOVO\Desktop\Studio\Secondo anno - secondo semestre\Algoritmi e programmazione a oggetti\Repository lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\add_folder.png")
        self._file_image = PhotoImage(file=r"C:\Users\LENOVO\Desktop\Studio\Secondo anno - secondo semestre\Algoritmi e programmazione a oggetti\Repository lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\file.png")
        self._add_file_image = PhotoImage(file=r"C:\Users\LENOVO\Desktop\Studio\Secondo anno - secondo semestre\Algoritmi e programmazione a oggetti\Repository lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\add_file.png")
        self._back_image = PhotoImage(file=r"C:\Users\LENOVO\Desktop\Studio\Secondo anno - secondo semestre\Algoritmi e programmazione a oggetti\Repository lab\Poli-Info-Lab\Personal projects\Machine learning file system\assets\back.png")

        # Impostazioni finestra
        self.title("File System")
        self.iconbitmap(default=self._window_icon)
        self["background"] = self._back_color
        self.geometry("+750+300")
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Frame
        self._toolbar = Frame(self, background=self._back_color)
        self._toolbar.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="we")
        self._toolbar.rowconfigure(0, weight=1)
        self._toolbar.columnconfigure(1, weight=1)

        self._main = Frame(self, background=self._back_color)
        self._main.grid(row=1, column=0, padx=10, pady=10, sticky="news")

        # Menu pop up
        self._main_menu = Menu(self, tearoff=0)
        self._menu_new = Menu(self._main_menu, tearoff=0)
        self._main_menu.add_cascade(menu=self._menu_new, label="New")
        self._menu_new.add_command(label="Folder", command=self._controller.create_folder)
        self._menu_new.add_command(label="File", command= self._controller.create_file)

        # Menu
        menubar = Menu(self)
        self["menu"] = menubar

        menu_options = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=menu_options, label="Options")

        menu_options.add_command(label="Info", command=self.show_info)

        # Grafica toolbar
        self._back = Button(self._toolbar, image=self._back_image, width=20, height=20, background=self._back_color, borderwidth=0, command=self._controller.return_back)
        self._back.grid(row=0, column=0)
        self.change_on_hover(self._back, self._light_blue, self._back_color)

        path_label = ttk.Label(self._toolbar, textvariable=self._path, background=self._back_color)
        path_label.grid(row=0, column=1, padx=10, sticky="we")
        path_label.bind("<Button-1>", lambda event: self.modify_path(path_label))

        button = Button(self._toolbar, image=self._add_folder_image, width=20, height=20, background=self._back_color, borderwidth=0, command=self._controller.create_folder)
        button.grid(row=0, column=2, sticky="e")
        self.change_on_hover(button, self._light_blue, self._back_color)

        button = Button(self._toolbar, image=self._add_file_image, width=20, height=20, background=self._back_color, borderwidth=0, command=self._controller.create_file)
        button.grid(row=0, column=3, padx=(10, 0), sticky="e")
        self.change_on_hover(button, self._light_blue, self._back_color)

        # Eventi
        self._main.bind("<Button-3>", self.do_popup)  # Menu azioni

        # Inizializzazione
        self.initialize()

    def initialize(self):
        self._controller.update()

    # Crea i tasti
    def create(self, name, item, index):

        # Gestisce il layout
        if index in self._multiples:
            i = self._multiples.index(index)
            if self._multiples[i] != self._current_multiple:
                self._current_multiple = self._multiples[i]
                self._rows += 1

        col = index - self._current_multiple

        #TODO: crea funzione per restituire l'immagine giusta a seconda del file e formato

        # Gestisce le immagini
        if isinstance(item, Folder):
            image = self._folder_image
        else:
            image = self._file_image

        # Grafica tasti

        # button_frame = Frame(self._main, background=self._back_color)
        # button = Button(button_frame, image=image, width=60, height=50, borderwidth=0)
        # label = ttk.Label(button_frame, text=name)
        #
        # self.change_on_hover_multiples(button_frame, self._light_blue, self._back_color, button_frame, button, label)
        #
        # button_frame.bind("<Button-1>", lambda event: self._controller.open(index))
        # button.bind("<Button-1>", lambda event: self._controller.open(index))
        # label.bind("<Button-1>", lambda event: self._controller.open(index))
        #
        # button_frame.bind("<Button-3>", lambda event: self.do_popup(index))  #TODO: da sistemare
        #
        # button_frame.grid(row=self._rows, column=col, padx=8, pady=8, sticky="nw")
        # button.grid(row=0, column=0, sticky="s")
        # label.grid(row=1, column=0, sticky="n")
        #
        # self._buttons.append(button_frame)


        button = Button(self._main, text=name, image=image, width=60, height=60, compound=TOP, background=self._back_color, borderwidth=0, command=lambda: self._controller.open(index))
        self.change_on_hover(button, self._light_blue, self._back_color)
        self._buttons.append(button)
        button.bind("<Button-3>", lambda event, i=index: self.do_popup(i))
        button.grid(row=self._rows, column=col, padx=5, pady=5, sticky="nw")

    #TODO: crea rinomiazione file e cartelle e aggiunta formato e contenuto testo
    # (aggiornamento label durante la digitazione, con entry nascosta e bind "enter" per il submit)

    # Mostra il contenuto del file
    def show(self, data, title):
        data_var = StringVar()
        data_var.set(data)
        window = Toplevel(self)
        window.title(title)
        window.geometry("+800+350")
        window.protocol("WM_DELETE_WINDOW", lambda: self.close_file(window))
        data_label = Label(window, textvariable=data_var, anchor="center")
        data_label.grid(row=0, column=0, padx=5, pady=5, sticky="news")

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

        string = ""
        for index in range(len(path)):
            string += path[index].name
            if index < len(path) - 1:
                string += "/"
        self._path_mod.set(string)

    # Elimina tutti gli elementi
    def clear(self):
        self._rows = 0
        for button in self._buttons:
            button.destroy()

    # Chiude il file
    def close_file(self, window):
        window.destroy()
        self._controller.close_file()

    # Apre il menu (tasto destro)
    def do_popup(self, event, index=None):
        try:
            self._main_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self._main_menu.grab_release()

    # Selezione e modifica percorso
    def modify_path(self, path_label, open=False):
        if isinstance(path_label, ttk.Label):
            path_label = Entry(self._toolbar, textvariable=self._path_mod, background=self._back_color, highlightthickness=0)
            path_label.grid(row=0, column=1, padx=10, sticky="we")
            path_label.focus_set()
            path_label.bind("<Return>", lambda event: self.modify_path(path_label, True))  # Aggiorna il percorso
            path_label.bind("<Button-3>", lambda event: self.modify_path(path_label))  # Non aggiorna il percorso
            self._toolbar.bind("<Button-1>", lambda event: self.modify_path(path_label))  # Non aggiorna il percorso
            self._main.bind("<Button-1>", lambda event: self.modify_path(path_label))  # Non aggiorna il percorso
        else:
            if open:
                self._controller.open_path(self._path_mod.get())  # Modifica il percorso
                path_label = ttk.Label(self._toolbar, textvariable=self._path, background=self._back_color)
                path_label.grid(row=0, column=1, padx=10, sticky="we")
                path_label.bind("<Button-1>", lambda event: self.modify_path(path_label))
            else:
                self._controller.update_view_path()
                path_label = ttk.Label(self._toolbar, textvariable=self._path, background=self._back_color)
                path_label.grid(row=0, column=1, padx=10, sticky="we")
                path_label.bind("<Button-1>", lambda event: self.modify_path(path_label))

    # Mostra messaggio di errore
    def show_error_box(self, title, message):
        messagebox.showerror(title=title, message=message)

    # Mostra la finestra con le informazioni sul funzionamento
    def show_info(self):
        text = ["CREAZIONE FILE E CARTELLE: tasto destro in un punto vuoto o pulsanti in alto a destra", "RICERCA PERCORSO: tasto sinistro sul percorso > inserimento percorso > invio", "ANNULLAMENTO RICERCA PERCORSO: tasto destro sul percorso o tasto sinistro in un punto vuoto"]
        window = Toplevel(self)
        window.title("Informazioni sul software")
        window.geometry("+800+350")

        for i in range(len(text)):
            if i == 0:
                pad = (20, 5)
            elif i == len(text) - 1:
                pad = (5, 20)
            else:
                pad = 5

            label = ttk.Label(window, text=text[i], font=("", 10), justify="left")
            label.grid(row=i, column=0, padx=20, pady=pad, sticky="news")

    # Cambio colore tasto se il mouse è in hover
    def change_on_hover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(
            background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(
            background=colorOnLeave))

    # Cambio colore a più elementi se il mouse è in hover
    def change_on_hover_multiples(self, button, colorOnHover, colorOnLeave, *elements):
        button.bind("<Enter>", func=lambda e: self.color_change(colorOnHover, *elements))
        button.bind("<Leave>", func=lambda e: self.color_change(colorOnLeave, *elements))

    def color_change(self, color, *elements):
        for el in elements:
            el["background"] = color
