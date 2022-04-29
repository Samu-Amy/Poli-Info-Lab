class Room:

    def __init__(self, meters: int, windows: int, sockets: int) -> None:
        self._meters = meters
        self._windows = windows
        self._sockets = sockets

    def get_meters(self) -> int:
        return self._meters

    def get_windows(self) -> int:
        return self._windows

    def get_sockets(self) -> int:
        return self._sockets


class BathRoom(Room):

    def __init__(self, meters: int, windows: int, sockets: int, sinks: int, shower: bool, bath: bool, bidet: bool) -> None:
        super().__init__(meters, windows, sockets)
        self._sinks = sinks
        self._shower = shower
        self._bath = bath
        self._bidet = bidet

    def get_sinks(self) -> int:
        return self._sinks

    def get_shower(self) -> bool:
        return self._shower

    def get_bath(self) -> bool:
        return self._bath

    def get_bidet(self) -> bool:
        return self._bidet


def main():

    salotto = Room(8, 3, 6)
    bagno = BathRoom(6, 1, 3, 2, False, True, True)


    print(f"Il salotto è di {salotto.get_meters()} metri quadri, ha {salotto.get_windows()} finestre e {salotto.get_sockets()} prese per la corrente.\n")

    print(f"Il bagno è di {bagno.get_meters()} metri quadri, ha {bagno.get_windows()} finestre e {bagno.get_sockets()} prese per la corrente,\nha {bagno.get_sinks()} lavandini, ", end = "")

    if bagno.get_shower():
        print("ha la doccia, ", end = "")
    else:
        print("non ha la doccia, ", end="")

    if bagno.get_bath():
        print("ha la vasca e ", end = "")
    else:
        print("non ha la vasca e ", end="")

    if bagno.get_bidet():
        print("ha il bidet.\n")
    else:
        print("non ha il bidet.\n")


main()
