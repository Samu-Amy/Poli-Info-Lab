from chess.competition import Player

class Tournament:

    def __init__(self, name):
        self._name = name
        self._players = []

    @property
    def name(self):
        return self._name

    def add_player(self, player, score):
        self._players.append((player, score))

    def get_leading(self):
        if len(self._players) > 0:
            best = 0
            index = 0
            for i in range(len(self._players)):
                if self._players[i][1] > best:
                    best = self._players[i][1]
                    index = i
            return f"{str(self._players[index][0]).split(',')[0]}:{self._players[index][1]}"
        else:
            return None