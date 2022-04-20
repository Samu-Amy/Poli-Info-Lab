class Matrix:

    def __init__(self, matrice):
        self.matrice = [["",""],["",""]]
        for i in range(len(matrice)):
            for j in range(len(matrice[i])):
                self.matrice[i][j] = matrice[i][j]

    # def get_rows(self):
    #     for i in range(len(self.matrice)):
    #         print(self.matrice[i])
    #
    # def get_columns(self):
    #     for i in range(len(self.matrice)):
    #         for j in range(len(self.matrice[i])):
    #             print(self.matrice[j][i])
    #         print()

    def __add__(self, other):
        tab = [["",""], ["",""]]
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                tab[i][j] = self.matrice[i][j] + other.matrice[i][j]

        return Matrix(tab)

    def __sub__(self, other):
        tab = [["",""], ["",""]]
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                tab[i][j] = self.matrice[i][j] - other.matrice[i][j]

        return Matrix(tab)

    def __mul__(self, other):
        tab = [[0,0], [0,0]]
        matrice2 = [[other.matrice[0][0], other.matrice[1][0]], [other.matrice[0][1], other.matrice[1][1]]]
        for i in range(len(self.matrice)):
            riga = self.matrice[i]
            for j in range(len(matrice2)):
                riga2 = matrice2[j]
                for element in range(len(riga)):
                    tab[i][j] += riga[element] * riga2[element]

        return Matrix(tab)

    def __eq__(self, other):
        uguali = True
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                if self.matrice[i][j] != other.matrice[i][j]:
                    uguali = False
                    break
        return uguali

    def __str__(self):
        string = ""
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                string += str(self.matrice[i][j]) + " "
            if i < len(self.matrice) - 1: #Se non è all'ultima riga
                string += "/ "

        return string

    def stampa(self):
        for i in range(len(self.matrice)):
            for j in range(len(self.matrice[i])):
                print(self.matrice[i][j], end=" ")
            print()


def main():

    tabella1 = [[2,3], [8,5]]
    tabella2 = [[4,6], [9,2]]

    matrice1 = Matrix(tabella1)
    matrice2 = Matrix(tabella2)
    matrice4 = Matrix(tabella1)
    matrice5 = matrice1

    # matrice1.get_rows()
    # matrice1.get_columns()

    matrice1.stampa()
    print()
    matrice2.stampa()

    print("\nSomma:")
    matrice3 = matrice1 + matrice2
    matrice3.stampa()

    print("\nSottrazione:")
    matrice3 = matrice1 - matrice2
    matrice3.stampa()

    print("\nMoltiplicazione:")
    matrice3 = matrice1 * matrice2
    matrice3.stampa()

    print("\nUguaglianza tra 1 e 2:")
    if matrice1 == matrice2:
        print("Sono uguali")
    else:
        print("Sono diverse")

    print("\nUguaglianza tra 1 e 4:")
    if matrice1 == matrice4:
        print("Sono uguali")
    else:
        print("Sono diverse")

    print("\nUguaglianza tra 1 e 5:")
    if matrice1 == matrice5:
        print("Sono uguali")
    else:
        print("Sono diverse")

    print(f"\nStringa matrice 1: {str(matrice1)}")


main()
