from gui.controller import Controller
from gui.model import Model
from gui.view import View


def main():

    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    controller.set_view(view)

    view.mainloop()

main()
