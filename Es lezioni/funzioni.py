class Data:

    def __init__(self, data):
        self._data = data

    def get(self):
        return self._data

d1 = Data(1)
d2 = Data(5)
d3 = Data(12)
print(d1.get())
print(d2.get())
print(d3.get())

l = [d1, d2, d3]

print(*l)
# print(*l.get())  Non funziona
print()


def fun(**par):
    for k in par:
        print("Chiave:", k, "Valore:", par[k])

fun(a=3, b=15, c=120)

d = {"a": 1, "b": 2, "c": 3}

print(*d)
# print(**d)  Non funziona
# fun(d)  Non funziona

print()

l = [1, 2, 3]
arg = {"sep": ", ", "end": "\n"}
print(*l, **arg)


def potenze(n):
    def f(x):
        return x**n
    return f

p = potenze(2)

print(p(5))


def counter_factory():
    l=0
    def f():
        print(l)
        l+=1  # Non può modificarlo
    return f

def counter_factory():
    l=[0]
    def f():
        print(l[0])
        l[0]+=1  # Può modificarlo
    return f

f=counter_factory()
f2=counter_factory()
f()  #0
f()  #1
f2() #0
f()  #2


n1 = 5
n2 = 3
print((lambda a, b: a+b)(n1, n2))

lambda_fun = lambda a, b=2: a+b

print(lambda_fun(5))

print()

def decoratore(f):
    def f2(*args, **kargs):
        print("Inserisci un numero: ", end="")
        r = f(*args, **kargs)
        print("Grazie")
        return r
    return f2

@decoratore
def multiplo(div):
    n = int(input())
    if n % div == 0:
        print("multiplo di", div)
        ris = True
    else:
        print("non multiplo di", div)
        ris = False
    return ris

risultato=multiplo(3)
