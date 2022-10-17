from copy import deepcopy
from pieces import Piece, PieceType, Color


class ChessLogic:
    def __init__(self):
        self.board = [[Empty() for x in range(8)] for y in range(8)]
        self.player_turn = 0
        
        self.STATUS = 1
        self.currentMoveNo = 0

    def check_for_mate(self):

        kingposx, kingposy = self.find_the_king()
        for x in self.board:
            for y in x:
                if y.color != self.player_turn:
                    continue
                if isinstance(y, King) and y.get_moves(self.board):
                    return False
                if isinstance(y, King):
                    continue
                for move in y.get_moves(self.board):
                    xmove, ymove = move
                    tempboard = deepcopy(self.board)
                    tempboard[ymove][xmove] = tempboard[y.y][y.x]
                    tempboard[y.y][y.x] = Empty()
                    if not tempboard[kingposy][kingposx].is_in_check(tempboard):
                        return False
        return True