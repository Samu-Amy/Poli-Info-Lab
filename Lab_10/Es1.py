from abc import ABC, abstractmethod
from math import sqrt


class Shape(ABC):

    def __init__(self, name: str) -> None:
        self._name = name

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def get_perimeter(self) -> float:
        pass

    @abstractmethod
    def get_area(self) -> float:
        pass


class Triangle(Shape):

    def __init__(self, name: str, *sides: float) -> None:
        super().__init__(name)
        self._sides: tuple = sides

    def get_perimeter(self) -> float:
        if len(self._sides) == 1:
            return self._sides[0]*3
        elif len(self._sides) == 2:
            return self._sides[0] + self._sides[1]*2
        elif len(self._sides) == 3:
            return self._sides[0] + self._sides[1] + self._sides[2]
        else:
            raise Exception("Too many sides")

    def get_area(self) -> float:
        ris = 0
        if len(self._sides) == 1:
            ris = sqrt(3)/4 * (self._sides[0]) ** 2
        elif len(self._sides) == 2:
            h = sqrt(self._sides[1] ** 2 - (self._sides[0]) ** 2)
            ris = (self._sides[0] * h) / 2
        elif len(self._sides) == 3:
            p = self.get_perimeter() / 2
            ris = sqrt(p * (p - self._sides[0]) * (p - self._sides[1]) * (p - self._sides[2]))
        else:
            raise Exception("Too many sides")
        return ris


class Square(Shape):

    def __init__(self, name: str, side: float) -> None:
        super().__init__(name)
        self._side = side

    def get_perimeter(self) -> float:
        return self._side * 4

    def get_area(self) -> float:
        return self._side ** 2


def main():

    triangle1 = Triangle("T1", 8)
    triangle2 = Triangle("T2", 4, 9)
    triangle3 = Triangle("T3", 2, 4, 3)
    print(f"Il triangolo {triangle1.get_name()} ha perimetro: {triangle1.get_perimeter()} e area {triangle1.get_area(): .3f}")
    print(f"Il triangolo {triangle2.get_name()} ha perimetro: {triangle2.get_perimeter()} e area {triangle2.get_area(): .3f}")
    print(f"Il triangolo {triangle3.get_name()} ha perimetro: {triangle3.get_perimeter()} e area {triangle3.get_area(): .3f}")

    square = Square("S", 5)
    print(f"Il quadrato {square.get_name()} ha perimetro: {square.get_perimeter()} e area {square.get_area(): .3f}")


main()
