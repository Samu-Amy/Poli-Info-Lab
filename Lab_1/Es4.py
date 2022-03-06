# Elaborazione valori input

valori = input("Inserisci due numeri positivi divisi da virgola: ")
valori = valori.split(",")
valore1 = int(valori[0])
valore2 = int(valori[1])


# Definizione delle funzioni

def fattoriale(val):
    for i in range(val - 1, 0, -1):
        val *= i
    return val

def coeffBin(val1, val2):
    ris = fattoriale(val1)/(fattoriale(val2) * fattoriale((val1 - val2)))
    return ris


# Iterazione e calcolo

while str(valore1) != "-1" or str(valore2) != "-1":

    risultato = coeffBin(valore1, valore2)

    print(f"Il coefficiente binomiale dei valori è: {risultato}")

    valori = input("Inserisci due numeri positivi divisi da virgola: ")
    valori = valori.split(",")
    valore1 = int(valori[0])
    valore2 = int(valori[1])
