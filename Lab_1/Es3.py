# Lavoro sul file
frasi = []
infile = open("input.txt", "r")
line = infile.readline()
while line != "":
    frasi.append(line.rstrip())
    line = infile.readline()

# Stampo su console il contenuto del file
for frase in frasi:
    print(frase)

# Inverto e scrivo nel file
outfile = open("output.txt", "w")
for frase in frasi[::-1]:
    outfile.write(frase + "\n")
