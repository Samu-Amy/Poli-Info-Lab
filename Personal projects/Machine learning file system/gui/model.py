from elements import Desktop, Folder, File


class Model:

    def __init__(self):
        self._desktop = Desktop()
        self._path = [self._desktop]
        self._current_item = self._desktop

        if not isinstance(self._current_item, File):
            self._items = self._current_item.get_items()
        else:
            self._items = []

        print(self._path)
        print(self._current_item.name)
        print(self._items)

        # Prova
        folder = Folder("Files").add(File("Text 1")).add(File("Text 2"))
        self._desktop.add(folder).add(File("Text"))
        folder = Folder("Images").add(File("Image 1")).add(File("Image 2"))
        self._desktop.add(folder)

    @property
    def path(self):
        return self._path

    @property
    def current_item(self):
        return self._current_item

    @current_item.setter
    def current_item(self, index):
        self._current_item = self._items[index]

    @property
    def items(self):
        return self._items

    def add_path(self, item):
        self._path.append(item)

    def pop_path(self):
        self._path.pop()
