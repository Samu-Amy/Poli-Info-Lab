N = int(input("Scrivi un numero: "))
tab = []


# Creazione tabella default

for i in range(N):
   row = [0] * N
   tab.append(row)


# Compilazione tabella

for i in range(N):
    for j in range(N):
        if i == 0 or j == 0:
            tab[i][j] = 1
        else:
            tab[i][j] = tab[i-1][j] + tab[i][j-1]


# Stampa tabella

for i in range(N):
    for j in range(N):
        print(str(tab[i][j]) + (" " * ((len(str(tab[N - 1][N - 2])) + 2) - len(str(tab[i][j])))), end="")
    print()
