from elements import Desktop, Folder, File


class Model:

    def __init__(self):
        self._desktop = Desktop()
        self._path = [self._desktop]
        self._current_item = self._desktop
        self._elements = []

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

    @property
    def items(self):
        return self._items

    # Aggiorna l'elemento corrente a quello aperto nella gui
    def set_current_item(self, index):
        to_update = False
        self._current_item = self._items[index]
        self.update_items()

        # Controllo se l'elemento è già selezionato (file già aperto)
        if self._path[-1] != self._current_item:
            if not isinstance(self._current_item, File):
                self._path.append(self._current_item)
            to_update = True
        return to_update

    # Torna indietro nel percorso e lo aggiorna
    def pop_path(self):
        self._path.pop()
        self.update_current_item()
        self.update_items()

    # Aggiorna l'elemento corrente all'ultimo del percorso
    def update_current_item(self):
        if not isinstance(self._path[-1], File):
            self._current_item = self._path[-1]

    # Aggiorna gli oggetti a quelli dell'elemento corrente
    def update_items(self):
        if not isinstance(self._current_item, File):
            self._items = self._current_item.get_items()

    # Crea un file
    def create_file(self):
        self._current_item.add(File(""))

    # Crea una cartella
    def create_folder(self):
        self._current_item.add(Folder(""))

    # Cerca un percorso
    def search_path(self, path):
        print(path)
        i = 1
        current = None
        last = path[-1]
        error = False
        new_path = []

        # Controllo primo elemento
        if current is None:
            if path[0] == self._desktop.name:
                current = self._desktop
            else:
                error = True

        if len(path) > 1:
            current, new_path, error = self.search_rec(current, i, path, new_path, last, error)

        return current, new_path, error

    def search_rec(self, current, index, path, new_path, last, error):
        print(index, last, path)  #TODO: elimina

        for element in current.get_items():
            if element == path[index]:
                current = element
                new_path.append(element)
                error = False
                break
            else:
                error = True

        if not error:
            if index != len(path) - 1:
                current, new_path, error = self.search_rec(current, index + 1, path, new_path, last, error)
            else:
                return current, new_path, error


        # while not error and not finished:
        #     if len(path)
        #     while i < len(path):
        #         found = False
        #         print(i, len(path))
        #         for element in current.get_items():
        #             if path[i+1] == element.name:
        #                 current = element
        #                 found = True
        #                 i += 1
        #                 break
        #         if not found:
        #             error = True
        #             break
        #
        #         if element.name == path[-1]:
        #             finished = True

        # print(current.name)
        #
        # # Controllo elemento
        # if current.name == path[-1]:
        #     return error, current
        # else:
        #     if i < len(path) - 1 and not error:
        #         print(i, len(path) -1)
        #         for element in current.get_items():
        #             # print(element.name)
        #             if path[i+1] == element.name:
        #                 current = element
        #                 # print(element.name)
        #                 return self.search_path(path, i+1, current)
