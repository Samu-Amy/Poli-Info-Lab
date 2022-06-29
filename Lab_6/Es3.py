class Player:

    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.team = None

    def get_values(self):
        return [self.name, self.surname, self.age]

    def set_team(self, team):
        self.team = team

    def get_team(self):
        return self.team

class Team:

    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.players = []

    def get_info(self):
        return [self.name, self.city]

    def add_player(self, player):
        self.players.append(player)

    def get_players(self):
        return self.players


# Test
def main():

    player1 = Player("Gianni", "Rossi", 21)
    player2 = Player("Bob", "Green", 24)

    team1 = Team("Red", "Torino")


    player1.set_team(team1)
    player2.set_team(team1)

    team1.add_player(player1)
    team1.add_player(player2)


    info = player1.get_values()
    print(f"\nDettagli giocatore 1: {info[0]} {info[1]}, {info[2]} anni")

    info = player2.get_values()
    print(f"Dettagli giocatore 2: {info[0]} {info[1]}, {info[2]} anni")

    print(f"\nFanno parte della squadra {player1.get_team().get_info()[0]}")

    teamInfo = team1.get_info()
    print(f"\nDettagli squadra:\nNome: {teamInfo[0]}\nCittà: {teamInfo[1]}\n")

    teamPlayers = team1.get_players()
    print(f"Di cui fanno parte: {teamPlayers[0].get_values()[0]} {teamPlayers[0].get_values()[1]} e {teamPlayers[1].get_values()[0]} {teamPlayers[1].get_values()[1]}")

main()
