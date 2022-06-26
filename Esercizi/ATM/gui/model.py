from elements.classi import Bank, SavingsAccount


class Model:

    def __init__(self):
        self._bank = Bank()
        self._account = None

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

    def delete_account(self, owner, pin):
        print(owner, pin)
        print(self._account.owner, self._account.pin)
        return self._bank.remove(owner, pin)
