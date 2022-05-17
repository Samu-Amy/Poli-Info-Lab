class SortableCouple:

    def __init__(self, a: float, b: float) -> None:
        self._couple = (a, b)

    @property
    def first_val(self) -> float:
        """Primo valore coppia"""
        return self._couple[0]

    @property
    def second_val(self) -> float:
        """Primo valore coppia"""
        return self._couple[1]

    def __repr__(self) -> str:
        return f"({self._couple[0]}, {self._couple[1]})"

    def __lt__(self, other) -> bool:
        return (self.first_val + self.second_val) < (other.first_val + other.second_val)


class CoupleSorter:

    def __call__(self, elm: SortableCouple) -> float:
        return elm.first_val - elm.second_val


def main():

    sc1 = SortableCouple(10, 12)
    sc2 = SortableCouple(5, 8)
    sc3 = SortableCouple(4, 16)
    sc4 = SortableCouple(2, 7)
    sc5 = SortableCouple(24, 36)
    sc6 = SortableCouple(10, 0)
    sc7 = SortableCouple(15, 1)
    sc8 = SortableCouple(50, 1)

    couple_list = [sc1, sc2, sc3, sc4, sc5, sc6, sc7, sc8]

    couple_sorter = CoupleSorter()

    # Test 1
    print(sc1)
    print(sc1.first_val)
    print(sc1.second_val)

    # Test 2
    print()
    print(sorted(couple_list))
    print(sorted(couple_list, key=lambda sort_c: sort_c.first_val * sort_c.second_val))

    # Test 3
    print()
    print(couple_sorter(sc1))
    print(couple_sorter(sc2))
    print(sorted(couple_list, key=lambda sort_c: couple_sorter(sort_c)))


if __name__ == "__main__":
    main()
