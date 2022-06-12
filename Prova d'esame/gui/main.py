from controller import Controller
from model import Model
from view import View

m = Model()
c = Controller(m)
v = View(m, c)
c.set_view = v
v.mainloop()
