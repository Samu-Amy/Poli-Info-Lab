def selection_sort(a):
    for i in range(len(a) - 1):
        pos_min = i
        for j in range(i + 1, len(a)):
            if a[pos_min] > a[j]:
                pos_min = j
        a[pos_min], a[i] = a[i], a[pos_min]


# Linked list
class Nodo:

    def __init__(self, dato):
        self._dato = dato
        self._next = None

    def set_next(self, nodo):
        self._next = nodo


def main():

    array = [2, 5, 1, 10, 8, 6, 12]
    selection_sort(array)
    print(array)


main()
