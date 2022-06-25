from tkinter import *
from tkinter import ttk, messagebox


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._components = []
        self._owner = StringVar()
        self._pin = StringVar()
        self._balance = StringVar()
        self._amount = StringVar()
        self._owner_title = StringVar()
        self._balance_title = StringVar()

        self.geometry("+500+250")
        self.log_in_page()

    def log_in_page(self):
        self.reset()
        self.title("Log in")

        self.create_form("Name:", self._owner, 0, 0, (20, 10), (20, 10))
        self.create_form("Pin:", self._pin, 0, 1, (10, 20), (20, 10))
        self.create_form("Balance (new account):", self._amount, 1, 0, (20, 10), (10, 10))
        self.create_button("Create account", 2, 0, (20, 10), (10, 20), "w", lambda: self._controller.create_account(self._owner.get(), self._pin.get(), self._amount.get()))
        self.create_button("Log in", 2, 1, (10, 20), (10, 20), "e", lambda: self._controller.log_in(self._owner.get(), self._pin.get()))

    def main_page(self, owner, balance):
        self.reset()
        self.title("Bank account")
        self.update_var()

        ttk.Label(self, textvariable=self._owner_title, font=("", 10)).grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")
        ttk.Label(self, textvariable=self._balance_title, font=("", 10)).grid(row=1, column=0, padx=20, pady=(5, 10), sticky="w")
        self.create_form("Amount:", self._amount, 2, 0, 20, (10, 10))
        self.create_button("Deposit", 3, 0, (20, 10), 10, "w", lambda: self._controller.deposit(int(self._amount.get())))
        self.create_button("Withdraw", 3, 1, (10, 20), 10, "e", lambda: self._controller.withdraw(int(self._amount.get())))

    def create_form(self, text, variable, row, column, padx, pady):
        frame = Frame(self)
        frame.grid(row=row, column=column, padx=padx, pady=pady)
        label = ttk.Label(frame, text=text)
        label.grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(frame, textvariable=variable)
        entry.grid(row=1, column=0)
        self._components.append(label)
        self._components.append(entry)
        self._components.append(frame)

    def create_button(self, text, row, column, padx, pady, sticky, command):
        button = ttk.Button(self, text=text, command=command)
        button.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
        self._components.append(button)

    def reset(self):
        for component in self._components:
            component.destroy()

    def reset_var(self):
        self._owner.set("")
        self._pin.set("")
        self._balance.set("")

    def reset_amount(self):
        self._amount.set("")

    def update_var(self):
        self._owner.set(self._model.account.owner)
        self._balance.set(self._model.account.balance)
        self._owner_title.set(f"Owner: {self._owner.get()}")
        self._balance_title.set(f"Balance: {self._balance.get()}")

    def show_error(self, title, message):
        messagebox.showerror(title=title, message=message)


    #TODO: elimina account, informazioni account e banca(di tutti gli account), interessi (banca)
