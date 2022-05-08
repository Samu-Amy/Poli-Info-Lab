from typing import List, Optional
from abc import ABC


class Element(ABC):
    def __init__(self, name: str) -> None:
        self._name = name
        self._connection = None  # Elemento a cui è connessa l'uscita di questo elemento

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
        self._flow = 0

    def set_flow(self, flow: float) -> None:
        self._flow = flow

    def get_flow(self) -> float:
        return self._flow


class Tap(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._open = None

    def set_status(self, to_open: bool = True) -> None:
        self._open = to_open

    def get_status(self) -> bool:
        return self._open


class Sink(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)


class Split(Element):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._connections = [None, None]

    def connect_at(self, elm: Element, pos: int) -> None:
        if isinstance(self, Sink):
            pass
        else:
            self._connections[pos] = elm

    def get_outputs(self) -> List[Optional[Element]]:
        return self._connections
