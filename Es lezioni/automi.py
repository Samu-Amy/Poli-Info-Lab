from abc import ABC, abstractmethod
from random import randint


class Piano:

    def __init__(self, righe: int = 100, colonne: int = 100) -> None:
        self._righe = righe
        self._colonne = colonne
        self._posizioni_occupate = set()
        self._automi = []

    def is_libera(self, riga: int, colonna: int) -> bool:
        return 0 <= riga < self._righe and 0 <= colonna < self._colonne and (riga, colonna) not in self._posizioni_occupate

    def _nuova_posizione(self) -> tuple:
        riga = randint(0, self._righe - 1)
        colonna = randint(0, self._colonne - 1)
        while not self.is_libera(riga, colonna):
            riga = randint(0, self._righe - 1)
            colonna = randint(0, self._colonne - 1)
        return riga, colonna

    def alfiere(self) -> None:
        pos = self._nuova_posizione()
        self._automi.append(Alfiere(*pos, piano = self))  # con "*" spacchetto la tupla
        self.occupa(pos)

    def muovi(self) -> None:
        for a in self._automi:
            a.muovi()

    def libera(self, pos: tuple) -> None:
        self._posizioni_occupate.remove(pos)

    def occupa(self, pos: tuple) -> None:
        self._posizioni_occupate.add(pos)

    def __repr__(self) -> str:
        string = ""
        for automa in self._automi:
            string += str(automa)
        return string


class Automa(ABC):

    def __init__(self, riga: int, colonna: int, piano: Piano) -> None:
        self._riga = riga
        self._colonna = colonna
        self._piano = piano

    def muovi(self) -> None:
        nuova_pos = self.posizione_futura()
        if self._piano.is_libera(*nuova_pos):
            self._piano.libera((self._riga, self._colonna))
            self._piano.occupa(nuova_pos)
            self._riga, self._colonna = nuova_pos

    def __repr__(self) -> str:
        return f"{type(self).__name__}: {self._riga},{self._colonna};\n"

    @abstractmethod
    def posizione_futura(self) -> tuple:
        pass


class Alfiere(Automa):

    def posizione_futura(self) -> tuple:
        direzione = randint(0, 3)  # 4 posizioni possibili (il 3 è incluso)
        spostamento = randint(1, 10)
        if direzione == 0:
            ris = (self._riga + spostamento, self._colonna + spostamento)
        elif direzione == 1:
            ris = (self._riga + spostamento, self._colonna - spostamento)
        elif direzione == 2:
            ris = (self._riga - spostamento, self._colonna - spostamento)
        elif direzione == 3:
            ris = (self._riga - spostamento, self._colonna + spostamento)
        return ris

# class Torre

# class Pedone
