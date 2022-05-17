import abc
from abc import ABC


class NutritionalElement(ABC):

    @property
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def calories(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def proteins(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def carbs(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def fats(self) -> float:
        pass

    @property
    @abc.abstractmethod
    def per100g(self) -> bool:
        pass


class RawMaterial(NutritionalElement):

    def __init__(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        self._name = name
        self._calories = calories
        self._proteins = proteins
        self._carbs = carbs
        self._fats = fats
        self._per100g = True

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return self._calories

    @property
    def proteins(self) -> float:
        return self._proteins

    @property
    def carbs(self) -> float:
        return  self._carbs

    @property
    def fats(self) -> float:
        return self._fats

    @property
    def per100g(self) -> bool:
        return self._per100g

    def __lt__(self, other) -> bool:
        return self.name < other.name


class PrepackagedProduct(NutritionalElement):

    def __init__(self, name: str, calories: float, proteins: float, carbs: float, fats: float) -> None:
        self._name = name
        self._calories = calories
        self._proteins = proteins
        self._carbs = carbs
        self._fats = fats
        self._per100g = False

    @property
    def name(self) -> str:
        return self._name

    @property
    def calories(self) -> float:
        return self._calories

    @property
    def proteins(self) -> float:
        return self._proteins

    @property
    def carbs(self) -> float:
        return  self._carbs

    @property
    def fats(self) -> float:
        return self._fats

    @property
    def per100g(self) -> bool:
        return self._per100g

    def __lt__(self, other) -> bool:
        return self.name < other.name
