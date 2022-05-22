
# Gestisce i dati e le operazioni
from diet.food import Food


class Model:

    def __init__(self):
        self._food = Food()
        self._data = None

    def set_data(self, datas):
        self._data = datas
        for data in self._data[1:]:
            try:
                data = float(data)
            except ValueError:
                print("Error")
                break
        print(self._data)

    def define_material(self):
        self._food.define_raw_material(*self._data)
        for material in self._food.raw_materials:
            print(material.name)
