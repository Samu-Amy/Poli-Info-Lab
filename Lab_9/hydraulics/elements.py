from typing import List, Optional
from abc import ABC


class Element(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._connection = None  # Elemento a cui è connessa l'uscita dell'elemento

    def get_name(self) -> str:
        return self._name

    def connect(self, elm: "Element") -> None:
        if isinstance(self, Sink):
            pass
        else:
            self._connection = elm

    def get_output(self) -> Optional["Element"]:
        return self._connection


class Source(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def set_flow(self, flow: float) -> None:
        pass


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def set_status(self, to_open: bool = True) -> None:
        pass


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Split(Element):
    def __init__(self, name: str) -> None:
        self._name = name
        self._connections = [None, None]

    def connect_at(self, elm: Element, pos: int) -> None:
        if isinstance(self, Sink):
            pass
        else:
            self._connections[pos] = elm

    def get_outputs(self) -> List[Optional[Element]]:
        return self._connections
