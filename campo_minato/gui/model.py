from random import randint


class Model:

    SMALL = (10, 15, 25)
    MEDIUM = (20, 30, 100)
    LARGE = (30, 45, 225)

    def __init__(self):
        self._field = []
        self._x = None
        self._y = None

    def initialization(self, dim):
        self._x = dim[0]
        self._y = dim[1]
        mines = dim[2]

        self._field = []
        for i in range(self._x):
            self._field.append([0]*self._y)

        for i in range(mines):
            placed = False
            while not placed:
                r = randint(0, self._x - 1)
                c = randint(0, self._y - 1)
                if self._field[r][c] != "x":
                    placed = True
            self._field[r][c] = "x"

            for j in range(max(0, r-1), min(self._x, r+2)):
                for k in range(max(0, c-1), min(self._y, c+2)):
                    if self._field[j][k] != "x":
                        self._field[j][k] += 1

    def pressed(self, i, j):
        other = []
        if self._field[i][j] == 0:
            for r in range(max(0, i-1), min(self._x, i+2)):
                for c in range(max(0, j-1), min(self._y, j+2)):
                    other.append((r, c))
        return self._field[i][j], other

    def stampa(self):
        for i in range(len(self._field)):
            for j in range(len(self._field[i])):
                print(self._field[i][j], end=" ")
            print()
