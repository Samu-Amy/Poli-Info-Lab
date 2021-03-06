from tkinter import *


class File:

    _id = 0

    def __init__(self, name="", format=None):
        self._name = name
        self._name_var = None
        self._format = format
        self._image = "file"
        self._data = ""
        self._path = []  #TODO: implementa (se serve)
        self._id = "fi" + str(File._id)
        File._id += 1
        # Argomento
        # Crea file veri (open e read)

    #TODO: aggiungi formati (sottoclassi apposta)

    #TODO: aggiungi blocco file con password

    #TODO: controllo nomi per elementi nella stessa cartella

    def set_name(self, name):
        self._name = name
        return self

    def set_name_var(self, name_var):
        self._name_var = name_var
        return self

    def set_data(self, data):
        self._data = data
        return self

    @property
    def name(self):
        return self._name

    @property
    def name_var(self):
        return self._name_var

    @name_var.setter
    def name_var(self, name):
        self._name_var.set(str(name))

    @property
    def format(self):
        return self._format

    @property
    def data(self):
        return self._data


class Folder:

    _id = 0

    def __init__(self, name):
        self._name = name
        self._name_var = None
        self._format = "folder"
        self._items = []
        self._path = []  # TODO: implementa (se serve)
        self._id = "fo" + str(Folder._id)
        Folder._id += 1

    #TODO: aggiungi ordinamento alfabetico e altri tipi di file

    def set_name(self, name):
        self._name = name
        return self

    def set_name_var(self, name_var):
        self._name_var = name_var
        return self

    def add(self, *folders):
        for folder in folders:
            self._items.append(folder)
        return self

    @property
    def name(self):
        return self._name

    @property
    def name_var(self):
        return self._name_var

    @name_var.setter
    def name_var(self, name):
        self._name_var.set(str(name))

    @property
    def format(self):
        return self._format

    def get_items(self):
        return self._items

    def __getitem__(self, index):
        return self._items[index]


class Desktop(Folder):

    def __init__(self):
        super().__init__(name="Desktop")
