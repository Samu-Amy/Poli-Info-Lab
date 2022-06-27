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
        self._window = None

        self.geometry("+540+260")
        self.log_in_page()

    def log_in_page(self):
        self.reset()
        self.title("Log in")

        self.create_form("Name:", self._owner, 0, 0, (20, 10), (20, 10))
        self.create_form("Pin:", self._pin, 0, 1, (10, 20), (20, 10))
        self.create_form("Balance (new account):", self._balance, 1, 0, (20, 10), (10, 10))
        self.create_button("Create account", 2, 0, (20, 10), (10, 20), "w", lambda: self._controller.create_account(self._owner.get(), self._pin.get(), self._balance.get()))
        self.create_button("Log in", 2, 1, (10, 20), (10, 20), "e", lambda: self._controller.log_in(self._owner.get(), self._pin.get()))

    def main_page(self):
        self.reset()
        self.title("Bank account")
        self.update_var()

        # Menu
        menubar = Menu(self)
        self["menu"] = menubar

        menu_options = Menu(menubar, tearoff=0)
        menubar.add_cascade(menu=menu_options, label="Options")

        menu_bank = Menu(menu_options, tearoff=0)
        menu_options.add_cascade(menu=menu_bank, label="Bank")
        menu_bank.add_command(label="View info", command=self._controller.view_bank_info)
        menu_bank.add_command(label="Compute interest", command=self._controller.compute)

        menu_account = Menu(menu_options, tearoff=0)
        menu_options.add_cascade(menu=menu_account, label="Account")
        menu_account.add_command(label="View info", command=self._controller.view_account_info)
        menu_account.add_command(label="Exit from account", command=self._controller.exit_account)
        menu_account.add_command(label="Delete account", command=self.delete_box)

        # Pagina
        ttk.Label(self, textvariable=self._owner_title, font=("", 10)).grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")
        ttk.Label(self, textvariable=self._balance_title, font=("", 10)).grid(row=1, column=0, padx=20, pady=(5, 10), sticky="w")
        self.create_form("Amount:", self._amount, 2, 0, 20, (10, 10))
        self.create_button("Deposit", 3, 0, (20, 10), 10, "w", lambda: self._controller.deposit(self._amount.get()))
        self.create_button("Withdraw", 3, 1, (10, 20), 10, "e", lambda: self._controller.withdraw(self._amount.get()))

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

    def delete_box(self):
        self._window = Toplevel(self)
        self._window.title("Delete account")
        self._window.geometry("+525+300")
        self._window.attributes("-topmost", True)

        frame = Frame(self._window)
        frame.grid(row=0, column=0, padx=(20, 10), pady=(20, 10))
        label = ttk.Label(frame, text="Name:")
        label.grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(frame, textvariable=self._owner)
        entry.grid(row=1, column=0)
        frame = Frame(self._window)

        frame.grid(row=0, column=1, padx=(10, 20), pady=(20, 10))
        label = ttk.Label(frame, text="Pin:")
        label.grid(row=0, column=0, sticky="w")
        entry = ttk.Entry(frame, textvariable=self._pin)
        entry.grid(row=1, column=0)

        button = ttk.Button(self._window, text="Cancel", command=self.close_delete_box)
        button.grid(row=2, column=0, padx=(20, 10), pady=(10, 20), sticky="w")
        button = ttk.Button(self._window, text="Delete", command=lambda: self._controller.delete_account(self._owner.get(), self._pin.get()))
        button.grid(row=2, column=1, padx=(10, 20), pady=(10, 20), sticky="e")

    def close_delete_box(self):
        self.reset_var()
        self.update_var()
        self._window.destroy()

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
        print(self._model.account.owner)
        print(self._model.account.balance)
        self._owner_title.set(f"Owner: {self._owner.get()}")
        self._balance_title.set(f"Balance: {self._balance.get()}")

    def show_error(self, title, message, parent=None):
        if parent is None:
            parent = self
        elif parent == "window":
            parent = self._window
        messagebox.showerror(title=title, message=message, parent=parent)

    def show_info(self, info):
        self._window = Toplevel(self)
        self._window.title("Delete account")
        self._window.geometry("+350+180")
        self._window.attributes("-topmost", True)

        text_box = Text(self._window)
        text_box.insert("end", info)
        text_box.grid(row=0, column=0)

    @staticmethod
    def message_box():
        messagebox.showinfo(title="Option completed successfully", message="Interests computed successfully.")

    def destroy_window(self):
        self._window.destroy()
