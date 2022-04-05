class IdentityCard:
    documents = 0

    def __init__(self, name, surname, year=2022):
        IdentityCard.documents += 1
        self.name = name
        self.surname = surname
        self.year = year
        self.birthYear = None
        self.documentNumber = IdentityCard.documents

    def set_birth_year(self, birthYear):
        if birthYear < self.year:
            self.birthYear = birthYear
        else:
            self.birthYear = self.year

    def get_birth_year(self):
        return self.birthYear

    def get_document_number(self):
        return self.documentNumber


def main():
    card1 = IdentityCard("Gianni", "Porta", 2019)
    card1.set_birth_year(2001)
    birth1 = card1.get_birth_year()
    number1 = card1.get_document_number()

    card2 = IdentityCard("Bob", "White")
    card2.set_birth_year(2025)
    birth2 = card2.get_birth_year()
    number2 = card2.get_document_number()

    card3 = IdentityCard("Robert", "Green", 2016)
    card3.set_birth_year(2020)
    birth3 = card3.get_birth_year()
    number3 = card3.get_document_number()

    print(f"Documento di {card1.name}, nato nel {birth1}, documento numero {number1}, rilasciato nel {card1.year}")
    print(f"Documento di {card2.name}, nato nel {birth2}, documento numero {number2}, rilasciato nel {card2.year}")
    print(f"Documento di {card3.name}, nato nel {birth3}, documento numero {number3}, rilasciato nel {card3.year}")


main()
