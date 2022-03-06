# Scrivete un programma che legga una parola da console e visualizzi tutte le sue sottostringhe,
# ordinate per lunghezza crescente.

word = input("Inserisci una parola: ")
lenght = len(word) - 1

for n in range(1, len(word)):
    for charIn in range(len(word) - n + 1):
        sottostringa = word[charIn:charIn + n]

        print(sottostringa)
