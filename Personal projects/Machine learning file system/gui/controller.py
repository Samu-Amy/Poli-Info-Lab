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

        # Elimina gli elementi grafici e apre la cartella
        elif isinstance(item, Folder):
            self._view.clear()
            items = item.get_items()
            for index in range(len(items)):
                item = items[index]
                self._view.create(item.name, item, index, item.name_var)

            self._view.update_path(self._model.path)

    # Apre una cartella o un file
    def open(self, element, item=False):
        if item:
            pass
        else:
            to_update = self._model.set_current_item(element)
            self._model.update_items()
            if to_update:
                self.update()

    # Apre un percorso
    def open_path(self, path_mod):
        path = path_mod.split("/")
        result = self._model.search_path(path)

        current = result[0]
        path = result[1]
        error = result[2]

        if error:
            self._view.show_error_box("Path error", "Path not found")
            self.update_view_path()
        else:
            self._model.open_folder(current, path)
            self.update()

    # Aggiorna percorso view
    def update_view_path(self):
        self._view.update_path(self._model.path)

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
    def create_file(self, name_var):
        self._model.create_file(name_var)
        self.update()
        self._view.rename_file()

    # Crea una cartella
    def create_folder(self, name_var):
        self._model.create_folder(name_var)
        self.update()
        self._view.rename_file()
