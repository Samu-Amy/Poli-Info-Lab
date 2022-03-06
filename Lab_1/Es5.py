# Lettura valori

val = input("Inserisci un numero intero: ")
valori = [val]

while val != "":
    val = input("Inserisci un numero intero: ")
    if val != "":
        valori.append(val)


# Ricerca massimi locali

massimi = []

for i in range(len(valori)):

    if i == 0: # Primo valore
        if valori[i] > valori[i + 1]:
            massimi.append(i + 1)

    elif i == (len(valori) - 1): # Ultimo valore
        if valori[i] > valori[i - 1]:
            massimi.append(i + 1)

    else: # Valori centrali
        if valori[i] > valori[i - 1] and valori[i] > valori[i + 1]:
            massimi.append(i + 1)


# Stampo l'output

if len(massimi) != 0:
    print("\nI valori di massimo locale sono nelle posizioni:")
    for i in massimi:
        print(i)

else:
    print("\nNon ci sono massimi locali.")
