
# Gestisce le interazioni

class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def define(self):
        self._model.define_material()
        # self._view.update()
