from typing import Optional


class ChessException(Exception):
    pass


class Piece:
    KING = "KING"
    QUEEN = "QUEEN"
    BISHOP = "BISHOP"
    KNIGHT = "KNIGHT"
    ROOK = "ROOK"
    PAWN = "PAWN"


class Board:
    def __init__(self, name: str, dim: int) -> None:
        self._name = name
        self._dim = dim
        self._board = []
        for i in range(dim):
            self._board.append([None]*dim)

    @property
    def name(self) -> str:
        return self._name

    @property
    def dim(self) -> int:
        return self._dim

    def add_piece(self, piece: Optional[str], x: int, y: int) -> None:
        try:
            self._board[x][y] = piece
        except IndexError:
            raise ChessException

    def get_piece(self, x: int, y: int) -> Optional[str]:
        try:
            return self._board[x][y]
        except IndexError:
            raise ChessException
