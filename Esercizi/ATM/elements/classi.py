class Bank:

    def __init__(self):
        self._accounts = []

    def add(self, account):
        self._accounts.append(account)

    def search(self, name, pin):
        found = False
        for account in self._accounts:
            if account.owner == name and account.pin == pin:
                found = True
                return account
        if not found:
            raise AccountError

    def remove(self, name, pin):
        account = self.search(name, pin)
        self._accounts.remove(account)

    def get(self, name, pin):
        account = self.search(name, pin)
        print(account)

    def compute_interest(self):
        for account in self._accounts:
            account.compute_interest()

    def __repr__(self):
        string = ""
        for account in self._accounts:
            string += str(account)
            string += "\n"
        return string


class SavingsAccount:

    RATE = 0.02

    def __init__(self, name, pin, balance):
        self._owner = name
        self._pin = pin
        self._balance = balance

    @property
    def owner(self):
        return self._owner

    @property
    def pin(self):
        return self._pin

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            raise AmountError

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
            else:
                raise FoundError
        else:
            raise AmountError

    def compute_interest(self):
        self._balance += self._balance * SavingsAccount.RATE

    def __repr__(self):
        return f"Name: {self._owner}\nBalance: {self._balance}"


class AmountError(Exception):

    def __init__(self):
        super().__init__("The amount must be greater than 0")


class FoundError(Exception):

    def __init__(self):
        super().__init__("Insufficient founds")


class AccountError(Exception):

    def __init__(self):
        super().__init__("The credentials are wrong or the account doesn't exist")
