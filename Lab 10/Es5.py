from time import perf_counter_ns


def repeat_ten_times(func):

    def inner(*args, **kargs):
        print("Esecuzione della funzione 10 volte:")
        for i in range(10):
            func(*args, **kargs)

    return inner


def time_execution(func):

    def inner(*args, **kargs):
        start = perf_counter_ns()
        func(*args, **kargs)
        end = perf_counter_ns()
        print(f"Time execution: {end - start}")

    return inner


class Greet:

    def __init__(self, name: str) -> None:
        self._name = name

    # @repeat_ten_times
    # @time_execution
    # def say_hello(self) -> None:
    #     print("Hello " + self._name)
    #
    # @repeat_ten_times
    # @time_execution
    # def say_good(self, time_of_day: str) -> None:
    #     print(f"Good {time_of_day}, {self._name}")

    @time_execution
    @repeat_ten_times
    def say_hello(self) -> None:
        print("Hello " + self._name)

    @time_execution
    @repeat_ten_times
    def say_good(self, time_of_day: str) -> None:
        print(f"Good {time_of_day}, {self._name}")


greet_pietro = Greet("Pietro")


greet_pietro.say_hello()

print()

greet_pietro.say_good("afternoon")
