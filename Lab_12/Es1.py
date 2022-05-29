
def somma(n):
    ris = 0
    if n > 1:
        return ris + n + somma(n-1)
    else:
        return 1


num = int(input("Inserisci un numero: "))
print(somma(num))
