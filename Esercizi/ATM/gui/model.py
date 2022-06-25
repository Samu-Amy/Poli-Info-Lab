from elements.classi import Bank, SavingsAccount


class Model:

    def __init__(self):
        self._bank = Bank()
        self._account = None
        self._attempts = 0

    @property
    def account(self):
        return self._account

    def create_account(self, owner, pin, balance):
        self._account = SavingsAccount(owner, pin, balance)
        self._bank.add(self._account)

    def log_in(self, owner, pin):
        self._account = self._bank.search(owner, pin)
        return self._account

    def deposit(self, amount):
        return self._account.deposit(amount)

    def withdraw(self, amount):
        return self._account.withdraw(amount)

    def increment_attempts(self):
        self._attempts += 1

    def reset_attempts(self):
        self._attempts = 0
