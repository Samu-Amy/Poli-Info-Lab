alph = "abcdefghijklmnopqrstuvwxyz"

string_1 = input("Scrivi una frase: ")
string_2 = input("Scrivi un'altra frase: ")

string_1 = set(string_1)
string_2 = set(string_2)


print("\nCaratteri presenti in entrambe le frasi:")

for i in string_1:
    if i in string_2:
        if i != " ":
            print(i, end = " ")


print("\n\nCaratteri presenti in solo una delle due frasi:")

for i in string_1:
    if i not in string_2:
        if i != " ":
            print(i, end = " ")

for i in string_2:
    if i not in string_1:
        if i != " ":
            print(i, end = " ")


print("\n\nLettere che non compaiono in nessuna delle due frasi:")

for i in alph:
    if i not in string_1 and i not in string_2:
        print(i, end = " ")

print() #Spazio finale