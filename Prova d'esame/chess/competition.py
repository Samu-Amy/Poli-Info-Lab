class Player:
    def __init__(self, name: str, nationality: str, age: int) -> None:
        self._name = name
        self._nationality = nationality
        self._age = age

    @property
    def name(self):
        return self._name

    def __repr__(self) -> str:
        return f"{self._name},{self._nationality},{self._age}"
