from diet.nutritional import NutritionalElement, RawMaterial


class Recipe(NutritionalElement):

    def __init__(self, name: str, food: "Food") -> None:
        self._name = name
        self._food = food
        self._ingredients = {}
        self._calories = 0
        self._proteins = 0
        self._carbs = 0
        self._fats = 0
        self._per100g = False

    def add_ingredient(self, raw_material_name: str, quantity: float) -> "Recipe":
        self._ingredients[raw_material_name] = quantity
        return self

    @property
    def name(self) -> str:
        return self._name

    #TODO: da sistemare i calcoli

    @property
    def calories(self) -> float:
        self._calories = 0
        for ingredient in self._ingredients.items():
            material = self._food.get_raw_material(ingredient[0])
            self._calories += material.calories * ingredient[1] / 100
        return self._calories

    @property
    def proteins(self) -> float:
        self._proteins = 0
        for ingredient in self._ingredients.items():
            material = self._food.get_raw_material(ingredient[0])
            self._proteins += material.proteins * ingredient[1] / 100
        return self._proteins

    @property
    def carbs(self) -> float:
        self._carbs = 0
        for ingredient in self._ingredients.items():
            material = self._food.get_raw_material(ingredient[0])
            self._carbs += material.carbs * ingredient[1] / 100
        return self._carbs

    @property
    def fats(self) -> float:
        self._fats = 0
        for ingredient in self._ingredients.items():
            material = self._food.get_raw_material(ingredient[0])
            self._fats += material.fats * ingredient[1] / 100
        return self._fats

    @property
    def per100g(self) -> bool:
        return self._per100g

    def __repr__(self) -> str:
        string = ""
        self._calories = 0
        for material in self._ingredients.items():
            string += f"{material[0]} {material[1] : .1f}\n"
        return string


class Menu(NutritionalElement):

    def add_recipe(self, recipe_name: str, quantity: float) -> "Menu":
        pass

    def add_product(self, product_name: str) -> "Menu":
        pass

    @property
    def name(self) -> str:
        pass

    @property
    def calories(self) -> float:
        pass

    @property
    def proteins(self) -> float:
        pass

    @property
    def carbs(self) -> float:
        pass

    @property
    def fats(self) -> float:
        pass

    @property
    def per100g(self) -> bool:
        pass
