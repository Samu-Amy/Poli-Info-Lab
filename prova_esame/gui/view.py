from tkinter import *
from tkinter import ttk


class View(Tk):

    def __init__(self, model, controller):
        super().__init__()
        self._model = model
        self._controller = controller
        self._x = StringVar()
        self._y = StringVar()
        self._message = StringVar()
        self._message_box = None

        # Grafica
        self.title("Chess")

        frame_get = Frame(self)
        frame_get.grid(row=0, column=0, padx=20, pady=20)

        title = ttk.Label(frame_get, text="Insert coordinates", font=("", 12))
        title.grid(row=0, column=0, columnspan=2, pady=10)

        x_label = ttk.Label(frame_get, text="X:")
        x_label.grid(row=1, column=0, sticky="w")
        y_label = ttk.Label(frame_get, text="Y:")
        y_label.grid(row=1, column=1, sticky="w")

        x_entry = ttk.Entry(frame_get, textvariable=self._x)
        x_entry.grid(row=2, column=0, padx=(0, 20))
        y_entry = ttk.Entry(frame_get, textvariable=self._y)
        y_entry.grid(row=2, column=1)

        submit = ttk.Button(frame_get, text="Remove piece", command=lambda x=self._x, y=self._y: self._controller.remove(x, y))
        submit.grid(row=3, column=0, pady=(20, 0), sticky="w")
        submit = ttk.Button(frame_get, text="Get piece", command=lambda x=self._x, y=self._y: self._controller.get(x, y))
        submit.grid(row=3, column=1, pady=(20, 0), sticky="e")

        self._message_box = ttk.Label(frame_get, textvariable=self._message)
        self._message_box.grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 0))

    def show_message(self, string: str):
        self._message_box["foreground"] = "green"
        self._message.set(string)
        self.reset_variable()

    def show_error(self, string: str):
        self._message_box["foreground"] = "red"
        self._message.set(string)

    def reset_variable(self):
        self._x.set("")
        self._y.set("")
