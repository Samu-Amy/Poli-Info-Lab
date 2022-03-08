# Creazione tabella e lettura file
schieramento = []
elementi = []
infile = open("schieramento2.txt", "r")
line = infile.readline().rstrip()

while line != "":
    row = []
    for element in line:
        row.append(element)
        elementi.append(element)
    schieramento.append(row)
    line = infile.readline().rstrip()

infile.close()


# Algoritmo principale

larghezza = 0
coord = None

file = max(elementi) # File

for i in range(len(schieramento)):
    for j in range(len(schieramento[i])):
        if schieramento[i][j] == "1":
            # Larghezza
            larghezza += 1
            if coord == None:
                coord = (i, j)

            # Direzione
            if schieramento[i + 1][j] == "2":
                direzione = "Nord"
            if schieramento[i][j - 1] == "2":
                direzione = "Est"
            if schieramento[i - 1][j] == "2":
                direzione = "Sud"
            if schieramento[i][j + 1] == "2":
                direzione = "Ovest"

# Numero di buchi

buchiMax = 0

if direzione == "Nord":
    for i in range(coord[0], coord[0] + int(file)):
        buchi = 0
        for j in range(coord[1], coord[1] + larghezza):
            if schieramento[i][j] == "0":
                buchi += 1
        if buchi > buchiMax:
            buchiMax = buchi
            filaBuchiMax = schieramento[i][coord[1]]

if direzione == "Sud":
    for i in range(coord[0], coord[0] - int(file)):
        buchi = 0
        for j in range(coord[1], coord[1] + larghezza):
            if schieramento[i][j] == "0":
                buchi += 1
        if buchi > buchiMax:
            buchiMax = buchi
            filaBuchiMax = schieramento[i][coord[1]]



if direzione == "Est":
    for j in range(coord[1], coord[1] + larghezza):
        for i in range(coord[0], coord[0] - int(file)):
            print(schieramento[i][j], end="")
        print()



# Stampa risultati

print("\nLa larghezza dello schieramento è " + str(larghezza))
print("Il numero di file è " + file)
print("La direzione è " + direzione)
print("La fila con più buchi è " + str(filaBuchiMax))

print(coord)

# Stampa della tabella

print("\nSchieramento:")
for i in range(len(schieramento)):
    for j in range(len(schieramento[i])):
        print(schieramento[i][j], end="")
    print()
