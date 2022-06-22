class File:

    def __init__(self, name="", format="txt"):
        self._name = name
        self._format = format
        self._image = "file"
        self._data = ""
        # Argomento
        # Crea file veri (open e read)

    #TODO: aggiungi formati e immagini corrispondenti

    def set_name(self, name):
        self._name = name
        return self

    def set_data(self, data):
        self._data = data
        return self

    @property
    def name(self):
        return self._name

    @property
    def format(self):
        return self._format

    @property
    def data(self):
        return self._data


class Folder:

    def __init__(self, name):
        self._name = name
        self._format = "folder"
        self._items = []

    #TODO: aggiungi ordinamento alfabetico e altri tipi di file

    def set_name(self, name):
        self._name = name
        return self

    def add(self, *folders):
        for folder in folders:
            self._items.append(folder)
        return self

    @property
    def name(self):
        return self._name

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
