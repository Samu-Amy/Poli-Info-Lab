from elements import Desktop, Folder, File


class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    # Aggiorna la gui
    def update(self, item="Desktop"):

        if item == "Desktop":
            item = self._model.current_item

        # Abilita o disabilita il tasto "indietro"
        if len(self._model.path) <= 1:
            self._view.set_return_back("disabled")
        else:
            self._view.set_return_back("normal")

        # Apre il file
        if isinstance(item, File):
            self._view.show(item.data, item.name)

        # Elimina gli elementi e apre la cartella
        elif isinstance(item, Folder):
            self._view.clear()
            items = item.get_items()
            for index in range(len(items)):
                item = items[index]
                self._view.create(item.name, item, index)

            self._view.update_path(self._model.path)

    # Apre una cartella o un file
    def open(self, index):
        to_update = self._model.set_current_item(index)
        self._model.update_items()
        if to_update:
            self.update()

    # Torna all'elemento precedente
    def return_back(self):
        if len(self._model.path) > 1:
            self._model.pop_path()
            self.update()

    # Chiude il file
    def close_file(self):
        self._model.update_current_item()
        self.update()

    # Crea un file
    def create_file(self):
        self._model.create_file()
        self.update()

    # Crea una cartella
    def create_folder(self):
        self._model.create_folder()
        self.update()
