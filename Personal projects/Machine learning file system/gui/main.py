from model import Model
from view import View
from controller import Controller


m = Model()
c = Controller(m)
v = View(m, c)

v.mainloop()
