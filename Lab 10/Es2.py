class Thermostat:

    def __init__(self, target_temp: float, is_celsius: bool) -> None:
        self._is_celsius = is_celsius
        if target_temp > 30:
            self._target_temp = 30
        else:
            self._target_temp = target_temp

    def imposta(func):

        def inner(*args, **kargs):
            print("A quanti gradi vuoi settare il termostato?")
            func(*args, **kargs)
            print("Temperatura impostata correttamente")

        return inner

    @property
    def target_temp(self) -> float:
        """Target temperature"""
        return self._target_temp

    @property
    def is_celsius(self) -> bool:
        """Unit of measure"""
        return self._is_celsius

    @imposta
    @target_temp.setter
    def target_temp(self, target_temp: float) -> None:
        if target_temp > 30:
            self._target_temp = 30
        else:
            self._target_temp = target_temp

    @is_celsius.setter
    def is_celsius(self, is_celsius: bool) -> None:
        self._is_celsius = is_celsius

    @staticmethod
    def convert_to_celsius(target_temp) -> float:
        return target_temp * 1.8 + 32

    @staticmethod
    def convert_to_fahrenheit(target_temp) -> float:
        return (target_temp - 32) / 1.8

    @classmethod
    def copy(cls, other: object) -> object:
        return cls(other.target_temp, other.is_celsius)


def main():

    term = Thermostat(50, True)
    print(term.target_temp)
    term.target_temp = 25
    print(term.target_temp)
    print(term.is_celsius)

    print("\nClasse copia:")
    term2 = Thermostat.copy(term)
    print(term2.target_temp)
    print(term2.is_celsius)


main()
