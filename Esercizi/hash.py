class Dato:
    def __init__(self, dato):
        self._dato = dato

    @property
    def dato(self):
        return self._dato

    @dato.setter
    def dato(self, dato):
        self._dato = dato

    def __repr__(self):
        return str(self._dato)

    def __eq__(self, other):
        return isinstance(other, Dato) and self._dato == other.dato

    def __hash__(self):
        return hash(self._dato)


a = Dato(12)
b = Dato(13)
s = {a, b}
print(s)  # {12, 13}
a.dato = 13
print(s)  # {13, 13} (non sono la stessa cosa)
