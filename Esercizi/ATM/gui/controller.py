from elements.classi import Bank, SavingsAccount, AccountError, AmountError, FoundError


class Controller:

    def __init__(self, model):
        self._model = model
        self._view = None

    def set_view(self, view):
        self._view = view

        # TODO: elimina
        self.create_account("Samu", 123, 5000)
        self.log_in("Samu", 123)

    def create_account(self, owner, pin, balance):
        self._model.create_account(owner, pin, balance)
        self._view.reset_var()

    def log_in(self, owner, pin):
        try:
            account = self._model.log_in(owner, pin)
            self._model.reset_attempts()
            self._view.reset_var()
            self._view.main_page()
        except AccountError:
            self._model.increment_attempts()
            self._view.show_error("Account error", "The credentials are wrong or the account doesn't exist")

    def deposit(self, amount):
        try:
            self._model.deposit(amount)
            self._view.reset_amount()
            self._view.update_var()
        except AmountError:
            self._view.show_error("Input error", "The amount must be greater than 0")

    def withdraw(self, amount):
        try:
            self._model.withdraw(amount)
            self._view.reset_amount()
            self._view.update_var()
        except FoundError:
            self._view.show_error("Amount error", "Insufficient founds")
        except AmountError:
            self._view.show_error("Input error", "The amount must be greater than 0")

    def delete_account(self, owner, pin):
        try:
            self._model.delete_account(owner, pin)
            self._view.log_in_page()
            self._view.destroy_window()
        except AccountError:
            self._view.show_error("Account error", "The credentials are wrong.")
