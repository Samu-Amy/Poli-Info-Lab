from gui.model import Model
from gui.controller import Controller
from gui.view import View


m = Model()
c = Controller(m)
v = View(m, c)
c.set_view(v)

m.stampa()

v.mainloop()
