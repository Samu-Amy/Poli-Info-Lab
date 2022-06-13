class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def get(self, x, y):
        piece = self._model.get(int(x.get()), int(y.get()))
        if piece is not None:
            self._view.show_message(f"The piece is: {piece}")
        else:
            self._view.show_error("Invalid coordinates")

    def remove(self, x, y):
        result = self._model.remove(int(x.get()), int(y.get()))
        if result:
            self._view.show_message("Piece removed successfully")
        else:
            self._view.show_error("Invalid coordinates")

        self._model.print_board()
