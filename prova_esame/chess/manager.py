from chess.board import Board, Piece, ChessException
from chess.competition import Player
from typing import List, Optional
from chess.tournament import Tournament


class ChessManager:
    def __init__(self) -> None:
        self._boards = []
        self._players = []
        self._tournaments = []
        self._tournaments_name = []
        self._assignment = {}

    # R2
    def add_board(self, board: Board) -> None:
        self._boards.append(board)

    def get_board(self, name: str) -> Board:
        for board in self._boards:
            if board.name == name:
                return board

    def add_player(self, player: Player) -> None:
        self._players.append(player)

    def get_player(self, name: str) -> Player:
        for player in self._players:
            if player.name == name:
                return player

    def add_player_to_board(self, player_name: str, board_name: str) -> None:
        if self._assignment.get(self.get_player(player_name)) is None:
            self._assignment[self.get_player(player_name)] = [self.get_board(board_name)]
        else:
            self._assignment[self.get_player(player_name)].append(self.get_board(board_name))

    def get_boards_of_player(self, name: str) -> List[Board]:
        return self._assignment[self.get_player(name)]

    # R3
    def create_tournament(self, name: str) -> None:
        if name not in self._tournaments_name:
            self._tournaments_name.append(name)
            self._tournaments.append(Tournament(name))
        else:
            raise ChessException

    def add_player_score(self, tournament_name: str, player_name: str, score: int) -> None:
        if self.get_player(player_name) in self._players:
            for tournament in self._tournaments:
                if tournament.name == tournament_name:
                    tournament.add_player(self.get_player(player_name), score)
        else:
            raise ChessException

    def get_leading_player(self, tournament_name: str) -> Optional[str]:
        for tournament in self._tournaments:
            if tournament.name == tournament_name:
                return tournament.get_leading()

    # R5
    def fill_queens(self, board_name: str, board_size: int) -> Board:
        board = Board(board_name, board_size)
        for i in range(board_size):
            for j in range(board_size):
                if self.check_queen(board, i, j):
                    board.add_piece(Piece.QUEEN, i, j)
        return board

    @staticmethod
    # METODO GIÀ FORNITO
    # controlla se è possibile inserire regina in posizione x, y:
    # - cella vuota
    # - non sotto attacco da altre regine
    def check_queen(board: Board, x: int, y: int) -> bool:
        # controllo riga-colonna
        for i in range(board.dim):
            if board.get_piece(i, y) is not None or board.get_piece(x, i) is not None:
                return False
        # controllo diagonale primaria
        x_pos = x - min(x, y)
        y_pos = y - min(x, y)
        while x_pos < board.dim and y_pos < board.dim:
            if board.get_piece(x_pos, y_pos) is not None:
                return False
            x_pos += 1
            y_pos += 1
        # controllo diagonale secondaria
        x_pos = x - min(x, board.dim - y - 1)
        y_pos = y + min(x, board.dim - y - 1)
        while x_pos < board.dim and y_pos >= 0:
            if board.get_piece(x_pos, y_pos) is not None:
                return False
            x_pos += 1
            y_pos -= 1
        return True














