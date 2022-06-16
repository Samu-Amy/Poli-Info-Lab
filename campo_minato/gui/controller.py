class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None
        self._pressed = set()

    def set_view(self, view):
        self._view = view

    def initialization(self, dim):
        self._pressed = set()
        self._model.initialization(dim)

    def pressed(self, i, j):
        val = self._model.pressed(i, j)
        self._pressed.add((i, j))
        self._view.expose(i, j, val[0])
        if not val[2]:
            if len(val[1]) > 0:
                for coord in val[1]:
                    if coord not in self._pressed:
                        self._view.pressed(*coord)
        else:
            for coord in val[1]:
                if coord not in self._pressed:
                    self._view.expose(*coord, val[0])
            self._view.show_message("Hai perso", "red", False)
