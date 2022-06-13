from chess.board import Board, Piece, ChessException


class Model:

    def __init__(self):
        self._board = Board("B1", 8)

        self._board.add_piece(Piece.ROOK, 0, 0)
        self._board.add_piece(Piece.KNIGHT, 0, 1)
        self._board.add_piece(Piece.BISHOP, 0, 2)
        self._board.add_piece(Piece.KING, 0, 3)
        self._board.add_piece(Piece.QUEEN, 0, 4)
        self._board.add_piece(Piece.BISHOP, 0, 5)
        self._board.add_piece(Piece.KNIGHT, 0, 6)
        self._board.add_piece(Piece.ROOK, 0, 7)
        for i in range(8):
            self._board.add_piece(Piece.PAWN, 1, i)

        self._board.add_piece(Piece.ROOK, 7, 0)
        self._board.add_piece(Piece.KNIGHT, 7, 1)
        self._board.add_piece(Piece.BISHOP, 7, 2)
        self._board.add_piece(Piece.KING, 7, 3)
        self._board.add_piece(Piece.QUEEN, 7, 4)
        self._board.add_piece(Piece.BISHOP, 7, 5)
        self._board.add_piece(Piece.KNIGHT, 7, 6)
        self._board.add_piece(Piece.ROOK, 7, 7)
        for i in range(8):
            self._board.add_piece(Piece.PAWN, 6, i)

        self.print_board()

    def print_board(self) -> None:
        if not self._board:
            print(self._board)
            return
        for i in range(self._board.dim):
            for j in range(self._board.dim):
                print("{: >7}".format(self._board.get_piece(i, j) if self._board.get_piece(i, j) is not None else "None"), end="")
            print()
        print()

    def get(self, x, y):
        try:
            return self._board.get_piece(x, y)
        except ChessException:
            return None

    def remove(self, x, y):
        try:
            self._board.add_piece(None, x, y)
            return True
        except ChessException:
            return False
