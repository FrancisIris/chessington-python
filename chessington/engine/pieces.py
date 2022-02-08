"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod
from tracemalloc import start

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player
        self.hasMoved=False

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)
        self.hasMoved = True


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        moves = []
        if(self.player == Player.WHITE):
            multiplier=1
        else:
            multiplier=-1
        test_square=Square(current_square.row +1*multiplier,current_square.col)
        if board.InBounds(test_square):

            test_square=Square(current_square.row + 1*multiplier, current_square.col-1)
            if board.InBounds(test_square):
                if board.get_piece(test_square) != None and self.player != board.get_piece(test_square).player :
                    moves.append(test_square)

            test_square=Square(current_square.row + 1*multiplier, current_square.col+1)
            if board.InBounds(test_square):
                if board.get_piece(test_square) != None and self.player != board.get_piece(test_square).player :
                    moves.append(test_square)
            
            test_square=Square(current_square.row + 1*multiplier, current_square.col)
            if board.get_piece(test_square) == None :
                moves.append(test_square)
                
                if not self.hasMoved:
                    test_square=Square(current_square.row +2*multiplier,current_square.col)
                    if board.InBounds(test_square):
                        if board.get_piece(test_square) == None :
                            moves.append(test_square)
        return moves
    
class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        row = current_square.row
        col = current_square.col
        moves=[]
        for i in range(-1,2):
            for j in range(-1,2):
                test_square=Square(row+i,col+j)
                if board.InBounds(test_square):
                    if board.get_piece(test_square)==None:
                        moves.append(test_square)
                    elif board.get_piece(test_square).player != self.player:
                        moves.append(test_square)
        return moves

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        moves = []
        startx = 0
        endx = 7
        starty = 0
        endy = 0
        for x in range(current_square.row):
            test_square=Square(x, current_square.col)
            if board.get_piece(test_square) != None:
                startx = x
                
        for x in range(current_square.row + 1,8):
            test_square=Square(x, current_square.col)
            if board.get_piece(test_square) != None:
                endx = x
                break
        for x in range(startx,endx+1):
            if(current_square.row != x):
                moves.append(Square(x,current_square.col))
                
        for x in range(current_square.col):
            test_square=Square( current_square.row,x)
            if board.get_piece(test_square) != None:
                startx = x
                
        for x in range(current_square.row + 1,8):
            test_square=Square( current_square.row,x)
            if board.get_piece(test_square) != None:
                endx = x
                break
        for x in range(startx,endx+1):
            if(current_square.row != x):
                moves.append(Square(current_square.row,x))
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


