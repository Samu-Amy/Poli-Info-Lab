
class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def update(self, folder="Desktop"):
        self._view.clear()

        if folder == "Desktop":
            folder = self._model.current_item
        else:
            pass

        items = folder.get_items()
        for index in range(len(items)):
            item = items[index]
            self._view.create(item.name, item.format, index)

        self._view.update_path(self._model.path)

    def open(self, index):
        self._model.current_item = index
        self.update()
