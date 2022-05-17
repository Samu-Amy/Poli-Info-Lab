from Es3 import SortableCouple


class WeightedSorter:
    
    def __init__(self, weight: float) -> None:
        self._weight = weight

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float) -> None:
        self._weight = weight

    def __call__(self, elm: SortableCouple) -> float:
        return elm.first_val * self._weight + elm.second_val * (1 - self._weight)


def w_sorter(weight: float):
    def action(elm: SortableCouple):
        return elm.first_val * weight + elm.second_val * (1 - weight)
    return action


def main():

    ws = WeightedSorter(0)

    sorter1 = w_sorter(0.25)
    sorter2 = w_sorter(0.5)

    sc1 = SortableCouple(10, 12)
    sc2 = SortableCouple(5, 8)
    sc3 = SortableCouple(4, 16)
    sc4 = SortableCouple(2, 7)
    sc5 = SortableCouple(24, 36)
    sc6 = SortableCouple(10, 0)
    sc7 = SortableCouple(15, 1)
    sc8 = SortableCouple(50, 1)

    couple_list = [sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8]

    print(ws.weight)
    ws.weight = 0.25
    print(ws.weight)

    print()

    print(sorted(couple_list, key=ws))
    ws.weight = 0.5
    print(sorted(couple_list, key=ws))

    print()
    print(sorted(couple_list, key=sorter1))
    print(sorted(couple_list, key=sorter2))


main()
