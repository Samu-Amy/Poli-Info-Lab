
def binary_numbers(lenght):
    digits = ["0", "1"]
    number = "0" * lenght
    if number == "1"*(lenght-1) + "0":
        number = "1"+lenght
        print(number)
    else:
        pass


binary_numbers(3)
