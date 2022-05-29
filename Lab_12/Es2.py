
def binary_numbers_rec(lenght, number, end, pos=0):
    print(number)
    if number == end:
        return number
    elif number[pos] == "0":
        number[pos] = "1"
        return binary_numbers_rec(lenght, number, end, pos)
    elif number[pos] == "1":
        number[pos] = "0"
        return binary_numbers_rec(lenght, number, end, pos-1)


def binary_numbers(lenght):
    return binary_numbers_rec(lenght, ["0"] * lenght, ["1"] * lenght, lenght-1)


lenght = int(input("Inserisci un numero: "))
print(binary_numbers(lenght))
