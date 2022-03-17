# Creazione tabella e lettura file

schieramento = []
elementi = []
infile = open("schieramento.txt", "r")
line = infile.readline().rstrip()

while line != "":
    row = []
    for element in line:
        row.append(element)
        elementi.append(element) # Lista con tutti gli elementi per calcolare il numero di file
    schieramento.append(row)
    line = infile.readline().rstrip()

infile.close()


# Algoritmo principale

larghezza = 0

file = max(elementi) # Numero di file

for i in range(len(schieramento)):
    for j in range(len(schieramento[i])):
        if schieramento[i][j] == "1":
            # Larghezza delle file
            larghezza += 1

            # Direzione dello schieramento
            if schieramento[i + 1][j] == "2":
                direzione = "Nord"
            elif schieramento[i][j - 1] == "2":
                direzione = "Est"
            elif schieramento[i - 1][j] == "2":
                direzione = "Sud"
            elif schieramento[i][j + 1] == "2":
                direzione = "Ovest"


# Numero di buchi

buchi = [0]*(int(file) + 1)


for i in range(len(schieramento)):
    for j in range(len(schieramento[i])):
        buchi[int(schieramento[i][j])] += 1

filaBuchiMax = buchi.index(min(buchi))


# Stampa della tabella

print("\nSchieramento:")

for i in range(len(schieramento)):
    for j in range(len(schieramento[i])):
        print(schieramento[i][j], end="")
    print()


# Stampa risultati

print("\nLa larghezza dello schieramento è " + str(larghezza))
print("Il numero di file è " + file)
print("La direzione è " + direzione)
print("La fila con più buchi è " + str(filaBuchiMax))
