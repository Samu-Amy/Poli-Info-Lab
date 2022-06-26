class Observable:

    def __init__(self):
        self._observers: list = []

    def attach(self, observer: 'Observer') -> None:
        self._observers.append(observer)

    def detach(self, observer: 'Observer') -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for o in self._observers:
            o.update(self)


class Observer:
    def update(self, o: Observable) -> None:
        raise NotImplementedError


class Counter(Observable):

    def __init__(self):
        super().__init__()
        self._numero = 0

    def incrementa(self) -> None:
        self._numero += 1
        self.notify()

    def get_numero(self) -> int:
        return self._numero


class OsservatoreMinoreDi5(Observer):
    def update(self, o: Counter) -> None:
        if o.get_numero() < 5:
            print("Il numero è minore di 5")


class OsservatoreUgualeA10(Observer):
    def update(self, o: Counter) -> None:
        if o.get_numero() == 10:
            print("Il contatore è arrivato a 10")


c = Counter()
o_a = OsservatoreMinoreDi5()
o_b = OsservatoreUgualeA10()
c.attach(o_a)
c.attach(o_b)
for i in range(20):
    c.incrementa()

