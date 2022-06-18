
class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def update(self, folder="Desktop"):
        print("Prova")
        if folder == "Desktop":
            folder = self._model.get_desktop()

        items = folder.get_items()
        for index in range(len(items)):
            item = items[index]
            print(item)
            self._view.create(item.name, item.format, index)
