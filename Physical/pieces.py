# Chess Pieces

from abc import ABC
import numpy as np
import sys
sys.path.append(".")
from board import *
from moves import *

# Begin: Abstract Piece Class ##################################################################################
#
class Piece():
    def __init__(self):
        pass
#
# End: Abstract Piece Class ###################################################################################

# Begin: Empty Place Class ####################################################################################
#
class Empty(Piece):
    # initiate an empty place with: a position
    def __init__(self, position):
        self.color = 'e'
        self.position = position

    # simple display of: space
    def display(self):
        return '  '
    
    # special display of: position
    def dispCPP(self):
        return #position
#
# End: Empty Place Class #####################################################################################

# Begin: Pawn Class ##########################################################################################
#
class Pawn(Piece):
    # initialize
    def __init__(self, color, position, board):
        self.color = color
        self.position = position
        self.hasMoved = False
        self.promoted = False
        self.mov = []

    # display methods
    def display(self):
        return self.color+'P'

    def dispCPP(self):
        return self.color+'P ' # + position

    # a Pawn can:
    # 1. move one space forward
        # promote to: Queen, Rook, Knight, Bishop
    # 2. move two spaces forward
    # 3. capture left
        # promote to: Queen, Rook, Knight, Bishop
    # 4. capture right
        # promote to: Queen, Rook, Knight, Bishop
    # 5. capture en passant
    def canMove(self):
        pass

    def promote(self, type):
        pass
#
# End: Pawn Class ###########################################################################################

# Begin: Knight Class #######################################################################################
#
class Knight(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def display(self):
        return self.color+'N'

    def swap(self, dest):
        pass

    def capture(self, dest):
        pass
#
# End: Knight Class ########################################################################################

# Begin: Queen Class ########################################################################################
#
class Queen(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def display(self):
        return self.color+'Q'

    def swap(self, dest):
        pass

    def capture(self, dest):
        pass
#
# End: Queen Class ##########################################################################################

# Begin: King Class #########################################################################################
#
class King(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasMoved = False

    def display(self):
        return self.color+'K'

    def swap(self, dest):
        pass

    def capture(self, dest):
        pass
#
# End: King Class ###########################################################################################

# Begin: Bishop Class #######################################################################################
#
class Bishop(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def display(self):
        return self.color+'B'

    def swap(self, dest):
        pass

    def capture(self, dest):
        pass
#
# End: Bishop Class #########################################################################################

# Begin: Rook Class ########################################################################################
#
class Rook(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasMoved = False

    def display(self):
        return self.color+'R'

    def swap(self, dest):
        pass

    def capture(self, dest):
        pass
#
# End: Rook Class ##########################################################################################