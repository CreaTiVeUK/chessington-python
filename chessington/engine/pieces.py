"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

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

    def is_on_board(self, new_square):
        """
        Check if possible move is on the board
        """
        if new_square.row in range (8) and new_square.col in range (8):
            return True
        else:
            return False

class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        current_square = board.find_piece(self)
        new_squares = []
        if self.player == Player.BLACK:
            direction = -1
            home_row = 6
        else:
            direction = 1
            home_row = 1
            
        new_square = Square.at((current_square.row) + direction, current_square.col)
        if self.is_on_board(new_square):
            if board.get_piece(new_square) == None:
                new_squares.append(new_square)
                if current_square.row == home_row:
                    new_square = Square.at((current_square.row) + direction*2, current_square.col)
                    if board.get_piece(new_square) == None:
                        new_squares.append(new_square)
            
        return new_squares

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
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []