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

        # Prova
        file1 = File("Text 1").set_data("Primo testo")
        file2 = File("Text 2").set_data("Altro testo")
        folder2 = Folder("Other files").add(file1).add(file2)
        folder = Folder("Files").add(folder2).add(file1).add(file2)
        file = File("Text").set_data("File")
        self._desktop.add(folder).add(file)
        folder = Folder("Images").add(File("Image 1")).add(File("Image 2"))
        self._desktop.add(folder)

    @property
    def path(self):
        return self._path

    @property
    def current_item(self):
        return self._current_item

    def set_current_item(self, index):
        to_update = False
        self._current_item = self._items[index]
        self.update_items()
        if self._path[-1] != self._current_item:
            self._path.append(self._current_item)
            to_update = True

    @property
    def items(self):
        return self._items

    def pop_path(self):
        self._path.pop()
        self.update_current_item()
        self.update_items()

    def update_current_item(self):
        self._current_item = self._path[-1]

    def update_items(self):
        if not isinstance(self._current_item, File):
            self._items = self._current_item.get_items()
