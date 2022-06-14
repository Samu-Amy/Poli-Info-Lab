class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def pressed(self, i, j):
        val = self._model.pressed(i, j)
        self._view.expose(i, j, val[0])
        if len(val[1]) > 0:
            for coord in val[1]:
                self._view.pressed(*coord)
