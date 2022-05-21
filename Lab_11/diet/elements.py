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
        self._per100g = True
        self._update = False  # Evita il calcolo dei valori ogni volta che vengono richiesti

    def add_ingredient(self, raw_material_name: str, quantity: float) -> "Recipe":
        if raw_material_name in self._ingredients:
            self._ingredients[raw_material_name] += quantity
        else:
            self._ingredients[raw_material_name] = quantity
        self._update = False
        return self

    @property
    def name(self) -> str:
        return self._name

    def calculate(self):
        self._calories = 0
        self._proteins = 0
        self._carbs = 0
        self._fats = 0
        quantity = 0
        for ingredient in self._ingredients.items():
            material = self._food.get_raw_material(ingredient[0])
            self._calories += material.calories * ingredient[1] / 100
            self._proteins += material.proteins * ingredient[1] / 100
            self._carbs += material.carbs * ingredient[1] / 100
            self._fats += material.fats * ingredient[1] / 100
            quantity += ingredient[1]
        self._calories *= 100 / quantity
        self._proteins *= 100 / quantity
        self._carbs *= 100 / quantity
        self._fats *= 100 / quantity
        # print("Calcolo...")
        self._update = True

    @property
    def calories(self) -> float:
        if not self._update:
            self.calculate()
        return self._calories

    @property
    def proteins(self) -> float:
        if not self._update:
            self.calculate()
        return self._proteins

    @property
    def carbs(self) -> float:
        if not self._update:
            self.calculate()
        return self._carbs

    @property
    def fats(self) -> float:
        if not self._update:
            self.calculate()
        return self._fats

    @property
    def per100g(self) -> bool:
        return self._per100g

    def __repr__(self) -> str:
        string = ""
        self._calories = 0
        for material in self._ingredients.items():
            string += f"{material[0]} {material[1]:.1f}\n"
        return string


class Menu(NutritionalElement):

    def __init__(self, name: str, food: "Food") -> None:
        self._name = name
        self._food = food
        self._recipes = {}
        self._products = []
        self._calories = 0
        self._proteins = 0
        self._carbs = 0
        self._fats = 0
        self._per100g = False
        self._update = False

    def add_recipe(self, recipe_name: str, quantity: float) -> "Menu":
        self._recipes[recipe_name] = quantity
        self._update = False
        return self

    def add_product(self, product_name: str) -> "Menu":
        self._products.append(product_name)
        self._update = False
        return self

    @property
    def name(self) -> str:
        return self._name

    def calculate(self):
        self._calories = 0
        self._proteins = 0
        self._carbs = 0
        self._fats = 0
        quantity = 0
        for element in self._recipes.items():
            recipe = self._food.get_recipe(element[0])
            self._calories += recipe.calories * element[1] / 100
            self._proteins += recipe.proteins * element[1] / 100
            self._carbs += recipe.carbs * element[1] / 100
            self._fats += recipe.fats * element[1] / 100
            quantity += element[1]
        for element in self._products:
            product = self._food.get_product(element)
            self._calories += product.calories
            self._proteins += product.proteins
            self._carbs += product.carbs
            self._fats += product.fats
        self._update = True

    @property
    def calories(self) -> float:
        if not self._update:
            self.calculate()
        return self._calories

    @property
    def proteins(self) -> float:
        if not self._update:
            self.calculate()
        return self._proteins

    @property
    def carbs(self) -> float:
        if not self._update:
            self.calculate()
        return self._carbs

    @property
    def fats(self) -> float:
        if not self._update:
            self.calculate()
        return self._fats

    @property
    def per100g(self) -> bool:
        return self._per100g
