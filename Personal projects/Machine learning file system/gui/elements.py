class File:

    def __init__(self, name, format="txt"):
        self._name = name
        self._format = format
        self._image = "file"
        # Argomento

    @property
    def name(self):
        return self._name

    @property
    def format(self):
        return self._format


class Folder:

    def __init__(self, name):
        self._name = name
        self._format = "folder"
        self._items = []

    @property
    def name(self):
        return self._name

    @property
    def format(self):
        return self._format

    def add(self, *folders):
        for folder in folders:
            self._items.append(folder)
        return self

    def get_items(self):
        return self._items

    def __getitem__(self, index):
        return self._items[index]


class Desktop(Folder):

    def __init__(self):
        super().__init__(name="Desktop")
