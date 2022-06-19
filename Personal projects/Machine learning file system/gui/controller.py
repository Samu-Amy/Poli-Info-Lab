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
                self._view.create(item.name, item.format, index)

            self._view.update_path(self._model.path)

    # Apre una cartella o un file
    def open(self, index):
        to_update = self._model.set_current_item(index)
        self._model.update_items()
        if to_update:
            self.update()
        print(self._model.path) #TODO: elimina

    # Torna all'elemento precedente
    def return_back(self):
        if len(self._model.path) > 1:
            self._model.pop_path()
            self.update()
        print(self._model.path) #TODO: elimina
