class Squadra:

    def __init__(self):
        self.avversari = set() # Per evitare duplicati
        self.canestri = []

    def add_match(self, avversari, canestri):
        self.avversari.add(avversari)
        self.canestri.append(canestri)

    def get_average(self):
        media = 0
        for i in self.canestri:
            media += i
        media /= len(self.canestri)
        return media

    def get_teams(self):
        squadre = []
        for squadra in self.avversari:
            squadre.append(squadra)
        return squadre

    def get_summary(self):
        tot = 0
        for i in self.canestri:
            tot += i
        media = tot/len(self.canestri)
        return tot, media


def main():
    team1 = Squadra()

    team1.add_match("team2", 10)
    team1.add_match("team3", 20)
    team1.add_match("team4", 16)
    team1.add_match("team2", 8)

    media1 = team1.get_average()
    avversari = team1.get_teams()
    (tot, media) = team1.get_summary()

    print(f"Media di canestri per partita: {media1}")
    print("Le squadre contro cui ha giocato sono: ")
    for squadra in avversari:
        print(squadra)
    print(f"Totale canestri: {tot: >3}\nMedia canestri: {media: >3}")


main()
