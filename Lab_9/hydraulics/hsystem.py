from hydraulics.elements import Element
from typing import List


class HSystem:
    def __init__(self) -> None:
        self._components = []

    def add_element(self, elm: Element) -> None:
        self._components.append(elm)

    def get_elements(self) -> List[Element]:
        return self._components

    def simulate(self) -> List[str]:
        pass


