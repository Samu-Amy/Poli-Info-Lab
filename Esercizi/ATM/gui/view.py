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
        self._amount = StringVar()

        self.log_in_page()

    def log_in_page(self):
        self.reset()
        self.title("Log in")
        self.create_form("Name:", self._owner, 0, 0, (20, 10), (20, 10))
        self.create_form("Pin:", self._pin, 0, 1, (10, 20), (20, 10))
        self.create_form("Balance (new account):", self._amount, 1, 0, (20, 10), (10, 10))
        self.create_button("Create account", 2, 0, (20, 10), (10, 20), "w", lambda: self._controller.create_account(self._owner.get(), self._pin.get(), self._amount.get()))
        self.create_button("Log in", 2, 1, (10, 20), (10, 20), "e", lambda: self._controller.log_in(self._owner.get(), self._pin.get()))

    def main_page(self):
        self.reset()
        self.title("Bank account")

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
        self._amount.set("")

    def show_error(self, title, message):
        messagebox.showerror(title=title, message=message)
