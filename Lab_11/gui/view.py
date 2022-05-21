from tkinter import *
from tkinter import ttk


# Gestisce la parte grafica

class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller

        self.title("Raw material")

        self._name = StringVar()
        self._calories = StringVar()
        self._proteins = StringVar()
        self._carbs = StringVar()
        self._fats = StringVar()
        self._errorMessage = StringVar()
        self._materialList = []
        self._rawMaterialList = StringVar(value=self._materialList)

        # Grafica

        # Parte di input
        self._frame1 = ttk.Frame(self)
        self._frame1.grid(row=0, column=0)

        ttk.Label(self._frame1, text="Raw material", anchor="center", font=("", 12)).grid(row=0, column=0, columnspan=2, sticky="ew", pady=10)

        ttk.Label(self._frame1, text="Name:").grid(row=1, column=0, sticky="e", padx=(20, 0))
        ttk.Entry(self._frame1, textvariable=self._name).grid(row=1, column=1, padx=(10, 20), pady=10)

        ttk.Label(self._frame1, text="Calories:").grid(row=2, column=0, sticky="e", padx=(20, 0))
        ttk.Entry(self._frame1, textvariable=self._calories).grid(row=2, column=1, padx=(10, 20), pady=10)

        ttk.Label(self._frame1, text="Proteins:").grid(row=3, column=0, sticky="e", padx=(20, 0))
        ttk.Entry(self._frame1, textvariable=self._proteins).grid(row=3, column=1, padx=(10, 20), pady=10)

        ttk.Label(self._frame1, text="Carbs:").grid(row=4, column=0, sticky="e", padx=(20, 0))
        ttk.Entry(self._frame1, textvariable=self._carbs).grid(row=4, column=1, padx=(10, 20), pady=10)

        ttk.Label(self._frame1, text="Fats:").grid(row=5, column=0, sticky="e", padx=(20, 0))
        ttk.Entry(self._frame1, textvariable=self._fats).grid(row=5, column=1, padx=(10, 20), pady=10)

        self._errorMessageEntry = ttk.Label(self._frame1, textvariable=self._errorMessage)
        self._errorMessageEntry.grid(row=6, column=0, columnspan=2, sticky="e", padx=(20, 0))
        ttk.Button(self._frame1, text="Submit").grid(row=7, column=1, padx=(10, 20), pady=(10, 20))

        # Parte di output
        self._frame2 = ttk.Frame(self)
        self._frame2.grid(row=0, column=2)

        ttk.Label(self._frame2, text="Raw material", anchor="center", font=("", 12)).grid(row=0, column=0, sticky="new", pady=10)
        Listbox(self._frame2, listvariable=self._rawMaterialList).grid(row=1, column=0, padx=20, pady=20)

        # Divisore
        ttk.Separator(self, orient="vertical").grid(row=0, column=1, sticky="ns")


    def create_material(self):
        pass

    def setMessage(self, message, color):
        self._errorMessageEntry.config(foreground=color)
        self._errorMessage.set(message)
        self.after(800, lambda: self._errorMessage.set(""))
