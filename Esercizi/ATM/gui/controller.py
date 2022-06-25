from elements.classi import AccountError, AmountError, FoundError


class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

    def create_account(self, owner, pin, balance):
        self._model.create_account(owner, pin, balance)
        self._view.reset_var()

    def log_in(self, owner, pin):
        try:
            self._model.log_in(owner, pin)
            self._model.reset_attempts()
            self._view.reset_var()
            self._view.main_page()
        except AccountError:
            self._model.increment_attempts()
            self._view.show_error("Account error", "The credentials are wrong or the account doesn't exist")
