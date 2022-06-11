
def binary_numbers_rec(number, end, pos):
    print(number)

    number[pos] += 1
    for i in range(pos, -1, -1):
        if number[i] == 2:
            number[i] -= 2
            number[i-1] += 1

    if number == end:
        return number

    return binary_numbers_rec(number, end, pos)


def binary_numbers(nLenght):
    return binary_numbers_rec([0] * nLenght, [1] * nLenght, nLenght-1)


lenght = int(input("Inserisci un numero: "))
print(binary_numbers(lenght))
