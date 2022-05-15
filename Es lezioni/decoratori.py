def greet():
    print("Hello")


def repeat_ten_times(func):

    def inner():
        print("Esecuzione della funzione 10 volte:")
        for i in range(10):
            func()

    return inner

@repeat_ten_times
def saluta():
    print("Ciao")


greet()

repeat = repeat_ten_times(greet)
repeat()

saluta()