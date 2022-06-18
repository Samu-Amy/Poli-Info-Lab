from elements import Desktop, Folder, File


class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def update(self, item="Desktop"):
        self._view.clear()

        if item == "Desktop":
            item = self._model.current_item

        if isinstance(self._model.current_item, Desktop):
            self._view.set_return_back("disabled")
        else:
            self._view.set_return_back("normal")

        if isinstance(item, File):
            self._view.show(item.data)
        elif isinstance(item, Folder):
            items = item.get_items()
            for index in range(len(items)):
                item = items[index]
                self._view.create(item.name, item.format, index)

        self._view.update_path(self._model.path)

    def open(self, index):
        to_update = self._model.set_current_item(index)
        self._model.update_items()
        if not to_update:
            self.update()

    def return_back(self):
        if self._model.current_item.name != "Desktop":
            self._model.pop_path()
            self.update()
