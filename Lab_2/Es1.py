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
coord = None

file = max(elementi) # Numero di file

for i in range(len(schieramento)):
    for j in range(len(schieramento[i])):
        if schieramento[i][j] == "1":
            # Larghezza delle file
            larghezza += 1
            if coord == None:
                coord = (i, j) # Coordinate del primo 1 incontrato

            # Direzione dello schieramento
            if schieramento[i + 1][j] == "2":
                direzione = "Nord"
            elif schieramento[i][j - 1] == "2":
                direzione = "Est"
            elif schieramento[i - 1][j] == "2":
                direzione = "Sud"
            elif schieramento[i][j + 1] == "2":
                direzione = "Ovest"

# Numero di buchi (oppure un dizionario con il numero di num != 0 per ogni riga)

buchiMax = 0

if direzione == "Nord":
    for i in range(coord[0] + 1, coord[0] + int(file)):
        buchi = 0
        for j in range(coord[1], coord[1] + larghezza):
            if schieramento[i][j] == "0":
                buchi += 1
        if buchi > buchiMax:
            buchiMax = buchi
            filaBuchiMax = schieramento[i][coord[1]]

if direzione == "Sud":
    for i in range(coord[0] - int(file) + 1, coord[0]):
        buchi = 0
        for j in range(coord[1], coord[1] + larghezza):
            if schieramento[i][j] == "0":
                buchi += 1
        if buchi > buchiMax:
            buchiMax = buchi
            filaBuchiMax = schieramento[i][coord[1]]

if direzione == "Est":
    for j in range(coord[0] - int(file) + 1, coord[0]):
        buchi = 0
        for i in range(coord[1], coord[1] + larghezza):
            if schieramento[i][j] == "0":
                buchi += 1
        if buchi > buchiMax:
            buchiMax = buchi
            filaBuchiMax = schieramento[coord[0]][j]

if direzione == "Ovest":
    for j in range(coord[0] + 1, coord[0] + int(file)):
        buchi = 0
        for i in range(coord[1], coord[1] + larghezza):
            if schieramento[i][j] == "0":
                buchi += 1
        if buchi > buchiMax:
            buchiMax = buchi
            filaBuchiMax = schieramento[coord[0]][j]


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
