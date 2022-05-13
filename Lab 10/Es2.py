class Thermostat:

    def __init__(self, target_temp: float, is_celsius: bool) -> None:
        self._target_temp = target_temp
        self._is_celsius = is_celsius

    @target_temp.setter
    def temp(self, target_temp: float) -> None:
        self._target_temp = target_temp

    @property
    def is_celsius(self, is_celsius: bool) -> None:
        self._is_celsius = is_celsius

    @property
    def target_temp(self) -> float:
        """Target temperature"""
        return self._target_temp

    @property
    def is_celsius(self) -> bool:
        """Unit of measure"""
        return self._is_celsius

    @staticmethod
    def convert_to_celsius(target_temp) -> float:
        return target_temp * 1.8 + 32

    @staticmethod
    def convert_to_fahrenheit(targetTemp) -> float:
        return (targetTemp - 32) / 1.8

    @classmethod
    def thermo(cls, target_temp: float, is_celsius: bool) -> object:
        return Thermostat(target_temp, is_celsius)


def main():

    term = Thermostat(50, True)
    term.get_target_temp()


main()
