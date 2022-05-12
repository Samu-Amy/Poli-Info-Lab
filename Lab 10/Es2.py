class Thermostat:

    def __init__(self, target_temp: float, is_celsius: bool) -> None:
        self._targetTemp = target_temp
        self._isCelsius = is_celsius

    def decor_get_temp(function):
        def inner(self):
            print("The target temperature is: ", end="")
            function(self)
        return inner

    def set_target_temp(self, target_temp: float) -> None:
        self._targetTemp = target_temp

    def set_is_celsius(self, is_celsius: bool) -> None:
        self._isCelsius = is_celsius

    @decor_get_temp
    def get_target_temp(self) -> float:
        return self._targetTemp

    def get_is_celsius(self) -> bool:
        return self._isCelsius

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
