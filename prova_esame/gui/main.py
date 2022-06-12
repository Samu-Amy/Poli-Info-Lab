from controller import Controller
from model import Model
from view import View
# import sys
# sys.path.append('prova_esame/chess')
# from chess.board import Board

board = Board("B1", 8)
board.add_piece(Piece.ROOK, 0, 0)
board.add_piece(Piece.KNIGHT, 0, 1)
board.add_piece(Piece.BISHOP, 0, 2)
board.add_piece(Piece.KING, 0, 3)
board.add_piece(Piece.QUEEN, 0, 4)
board.add_piece(Piece.BISHOP, 0, 5)
board.add_piece(Piece.KNIGHT, 0, 6)
board.add_piece(Piece.ROOK, 0, 7)
for i in range(8):
    board.add_piece(Piece.PAWN, 1, i)

def print_board(b: Board) -> None:
    if not b:
        print(b)
        return
    for i in range(b.dim):
        for j in range(b.dim):
            print("{: >7}".format(b.get_piece(i, j) if b.get_piece(i, j) is not None else "None"), end="")
        print("")

print_board(board)

m = Model()
c = Controller(m)
v = View(m, c)
c.set_view = v

v.mainloop()
