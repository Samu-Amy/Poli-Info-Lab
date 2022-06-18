
class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def update(self, folder="Desktop"):
        if folder == "Desktop":
            folder = self._model.get_desktop()
        else:
            pass

        items = folder.get_items()
        for index in range(len(items)):
            item = items[index]
            self._view.create(item.name, item.format, index)
