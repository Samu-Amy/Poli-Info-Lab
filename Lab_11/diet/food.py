from typing import List
from diet.nutritional import NutritionalElement, RawMaterial, PrepackagedProduct
from diet.elements import Recipe, Menu


class Food:

    def __init__(self) -> None:
        self._material = None
        self._product = None
        self._material_list = []
        self._material_names = set()
        self._product_list = []
        self._product_names = set()

    # R1
    def define_raw_material(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:  # Per 100g
        if name not in self._material_names:
            self._material = RawMaterial(name, calories, proteins, carbs, fats)
            self._material_list.append(self._material)
            self._material_names.add(name)
        else:
            raise ValueError


    @property
    def raw_materials(self) -> List[NutritionalElement]:
        return sorted(self._material_list)

    def get_raw_material(self, name: str) -> NutritionalElement:
        for mat in self._material_list:
            if mat.name == name:
                return mat

    # R2
    def define_product(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        if name not in self._product_names:
            self._product = PrepackagedProduct(name, calories, proteins, carbs, fats)
            self._product_list.append(self._product)
            self._product_names.add(name)
        else:
            raise ValueError

    @property
    def products(self) -> List[NutritionalElement]:
        return self._product_list

    def get_product(self, name: str) -> NutritionalElement:
        for prod in self._product_list:
            if prod.name == name:
                return prod

    # R3
    def create_recipe(self, name: str) -> Recipe:
        pass

    @property
    def recipes(self) -> List[Recipe]:
        pass

    def get_recipe(self, name: str) -> Recipe:
        pass

    # R5
    def create_menu(self, name: str) -> Menu:
        pass




