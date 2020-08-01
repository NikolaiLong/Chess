# Chess Pieces

from abc import ABC
import sys
sys.path.append(".")
from board import *
from player import *
from moves import *

# Begin: Abstract Piece Class ##################################################################################
#
class Piece():
    # initialize - will never be used
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
    
    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: Empty Place Class #####################################################################################

# Begin: Pawn Class ##########################################################################################
#
class Pawn(Piece):
    # initialize
    def __init__(self, color, position, id):
        self.id = id
        self.color = color
        self.position = position
        self.hasMoved = False
        self.hasMoved2 = False
        self.generatePossibleDestinations()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        if self.color == 'b':
            self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))),
                                    tuple(map(sum, zip(self.position,(0,-2)))),
                                    tuple(map(sum, zip(self.position,(-1,-1)))),
                                    tuple(map(sum, zip(self.position,(1,-1))))]
        elif self.color == 'w':
            self.allDestinations = [tuple(map(sum, zip(self.position,(0,1)))),
                                    tuple(map(sum, zip(self.position,(0,2)))),
                                    tuple(map(sum, zip(self.position,(-1,1)))),
                                    tuple(map(sum, zip(self.position,(1,1))))]
        else:
            print("!!!!!!!!!!!!!!color error!!!!!!!!!!!!!!!!!!!")

    # display self
    def display(self):
        return self.color+'P'

    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: Pawn Class ###########################################################################################

# Begin: Rook Class ########################################################################################
#
class Rook(Piece):
    # initialize
    def __init__(self, color, position, id):
        self.id = id
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))), # moving down, 0
                                tuple(map(sum, zip(self.position,(0,-2)))),
                                tuple(map(sum, zip(self.position,(0,-3)))),
                                tuple(map(sum, zip(self.position,(0,-4)))),
                                tuple(map(sum, zip(self.position,(0,-5)))),
                                tuple(map(sum, zip(self.position,(0,-6)))),
                                tuple(map(sum, zip(self.position,(0,-7)))),
                                tuple(map(sum, zip(self.position,(0,1)))), # moving up, 7
                                tuple(map(sum, zip(self.position,(0,2)))),
                                tuple(map(sum, zip(self.position,(0,3)))),
                                tuple(map(sum, zip(self.position,(0,4)))),
                                tuple(map(sum, zip(self.position,(0,5)))),
                                tuple(map(sum, zip(self.position,(0,6)))),
                                tuple(map(sum, zip(self.position,(0,7)))),
                                tuple(map(sum, zip(self.position,(-1,0)))), # moving left, 14
                                tuple(map(sum, zip(self.position,(-2,0)))),
                                tuple(map(sum, zip(self.position,(-3,0)))),
                                tuple(map(sum, zip(self.position,(-4,0)))),
                                tuple(map(sum, zip(self.position,(-5,0)))),
                                tuple(map(sum, zip(self.position,(-6,0)))),
                                tuple(map(sum, zip(self.position,(-7,0)))),
                                tuple(map(sum, zip(self.position,(1,0)))), # moving right, 21
                                tuple(map(sum, zip(self.position,(2,0)))),
                                tuple(map(sum, zip(self.position,(3,0)))),
                                tuple(map(sum, zip(self.position,(4,0)))),
                                tuple(map(sum, zip(self.position,(5,0)))),
                                tuple(map(sum, zip(self.position,(6,0)))),
                                tuple(map(sum, zip(self.position,(7,0))))] # 27

    # display self
    def display(self):
        return self.color+'R'

    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: Rook Class ##########################################################################################

# Begin: Knight Class #######################################################################################
#
class Knight(Piece):
    def __init__(self, color, position, id):
        self.id = id
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(2,-1)))),
                                tuple(map(sum, zip(self.position,(2,1)))),
                                tuple(map(sum, zip(self.position,(1,-2)))),
                                tuple(map(sum, zip(self.position,(1,2)))),
                                tuple(map(sum, zip(self.position,(-2,-1)))),
                                tuple(map(sum, zip(self.position,(-2,1)))),
                                tuple(map(sum, zip(self.position,(-1,-2)))),
                                tuple(map(sum, zip(self.position,(-1,2))))] # 8

    # display self
    def display(self):
        return self.color+'N'

    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: Knight Class ########################################################################################

# Begin: Bishop Class #######################################################################################
#
class Bishop(Piece):
    # initialize
    def __init__(self, color, position, id):
        self.id = id
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(-1,-1)))), # moving down-left, 0
                                tuple(map(sum, zip(self.position,(-2,-2)))),
                                tuple(map(sum, zip(self.position,(-3,-3)))),
                                tuple(map(sum, zip(self.position,(-4,-4)))),
                                tuple(map(sum, zip(self.position,(-5,-5)))),
                                tuple(map(sum, zip(self.position,(-6,-6)))),
                                tuple(map(sum, zip(self.position,(-7,-7)))),
                                tuple(map(sum, zip(self.position,(1,1)))), # moving up-right, 7
                                tuple(map(sum, zip(self.position,(2,2)))),
                                tuple(map(sum, zip(self.position,(3,3)))),
                                tuple(map(sum, zip(self.position,(4,4)))),
                                tuple(map(sum, zip(self.position,(5,5)))),
                                tuple(map(sum, zip(self.position,(6,6)))),
                                tuple(map(sum, zip(self.position,(7,7)))),
                                tuple(map(sum, zip(self.position,(-1,1)))), # moving up-left, 14
                                tuple(map(sum, zip(self.position,(-2,2)))),
                                tuple(map(sum, zip(self.position,(-3,3)))),
                                tuple(map(sum, zip(self.position,(-4,4)))),
                                tuple(map(sum, zip(self.position,(-5,5)))),
                                tuple(map(sum, zip(self.position,(-6,6)))),
                                tuple(map(sum, zip(self.position,(-7,7)))),
                                tuple(map(sum, zip(self.position,(1,-1)))), # moving down-right, 21
                                tuple(map(sum, zip(self.position,(2,-2)))),
                                tuple(map(sum, zip(self.position,(3,-3)))),
                                tuple(map(sum, zip(self.position,(4,-4)))),
                                tuple(map(sum, zip(self.position,(5,-5)))),
                                tuple(map(sum, zip(self.position,(6,-6)))),
                                tuple(map(sum, zip(self.position,(7,-7))))] # 27

    # display self
    def display(self):
        return self.color+'B'
    
    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: Bishop Class #########################################################################################

# Begin: Queen Class ########################################################################################
#
class Queen(Piece):
    # initialize
    def __init__(self, color, position, id):
        self.id = id
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))), # moving down, 0
                                tuple(map(sum, zip(self.position,(0,-2)))),
                                tuple(map(sum, zip(self.position,(0,-3)))),
                                tuple(map(sum, zip(self.position,(0,-4)))),
                                tuple(map(sum, zip(self.position,(0,-5)))),
                                tuple(map(sum, zip(self.position,(0,-6)))),
                                tuple(map(sum, zip(self.position,(0,-7)))),
                                tuple(map(sum, zip(self.position,(0,1)))), # moving up, 7
                                tuple(map(sum, zip(self.position,(0,2)))),
                                tuple(map(sum, zip(self.position,(0,3)))),
                                tuple(map(sum, zip(self.position,(0,4)))),
                                tuple(map(sum, zip(self.position,(0,5)))),
                                tuple(map(sum, zip(self.position,(0,6)))),
                                tuple(map(sum, zip(self.position,(0,7)))),
                                tuple(map(sum, zip(self.position,(-1,0)))), # moving left, 14
                                tuple(map(sum, zip(self.position,(-2,0)))),
                                tuple(map(sum, zip(self.position,(-3,0)))),
                                tuple(map(sum, zip(self.position,(-4,0)))),
                                tuple(map(sum, zip(self.position,(-5,0)))),
                                tuple(map(sum, zip(self.position,(-6,0)))),
                                tuple(map(sum, zip(self.position,(-7,0)))),
                                tuple(map(sum, zip(self.position,(1,0)))), # moving right, 21
                                tuple(map(sum, zip(self.position,(2,0)))),
                                tuple(map(sum, zip(self.position,(3,0)))),
                                tuple(map(sum, zip(self.position,(4,0)))),
                                tuple(map(sum, zip(self.position,(5,0)))),
                                tuple(map(sum, zip(self.position,(6,0)))),
                                tuple(map(sum, zip(self.position,(7,0)))),
                                tuple(map(sum, zip(self.position,(-1,-1)))), # moving down left, 28
                                tuple(map(sum, zip(self.position,(-2,-2)))),
                                tuple(map(sum, zip(self.position,(-3,-3)))),
                                tuple(map(sum, zip(self.position,(-4,-4)))),
                                tuple(map(sum, zip(self.position,(-5,-5)))),
                                tuple(map(sum, zip(self.position,(-6,-6)))),
                                tuple(map(sum, zip(self.position,(-7,-7)))),
                                tuple(map(sum, zip(self.position,(1,1)))), # moving up right, 35
                                tuple(map(sum, zip(self.position,(2,2)))),
                                tuple(map(sum, zip(self.position,(3,3)))),
                                tuple(map(sum, zip(self.position,(4,4)))),
                                tuple(map(sum, zip(self.position,(5,5)))),
                                tuple(map(sum, zip(self.position,(6,6)))),
                                tuple(map(sum, zip(self.position,(7,7)))),
                                tuple(map(sum, zip(self.position,(-1,1)))), # moving up-left, 42
                                tuple(map(sum, zip(self.position,(-2,2)))),
                                tuple(map(sum, zip(self.position,(-3,3)))),
                                tuple(map(sum, zip(self.position,(-4,4)))),
                                tuple(map(sum, zip(self.position,(-5,5)))),
                                tuple(map(sum, zip(self.position,(-6,6)))),
                                tuple(map(sum, zip(self.position,(-7,7)))),
                                tuple(map(sum, zip(self.position,(1,-1)))), # moving down-right, 49
                                tuple(map(sum, zip(self.position,(2,-2)))),
                                tuple(map(sum, zip(self.position,(3,-3)))),
                                tuple(map(sum, zip(self.position,(4,-4)))),
                                tuple(map(sum, zip(self.position,(5,-5)))),
                                tuple(map(sum, zip(self.position,(6,-6)))),
                                tuple(map(sum, zip(self.position,(7,-7))))] # 55

    # diplay self
    def display(self):
        return self.color+'Q'

    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: Queen Class ##########################################################################################

# Begin: King Class #########################################################################################
#
class King(Piece):
    # initialize
    def __init__(self, color, position, id):
        self.id = id
        self.color = color
        self.position = position
        self.hasMoved = False
        # starting in left upper corner facing oponent (clockwise)
        self.isPinned = [False, False, False, False, False, False, False, False]
        self.generatePossibleDestinations()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))),# 0
                                tuple(map(sum, zip(self.position,(0,1)))),
                                tuple(map(sum, zip(self.position,(-1,0)))),
                                tuple(map(sum, zip(self.position,(1,0)))),
                                tuple(map(sum, zip(self.position,(-1,-1)))),
                                tuple(map(sum, zip(self.position,(1,1)))),
                                tuple(map(sum, zip(self.position,(1,-1)))),
                                tuple(map(sum, zip(self.position,(-1,1)))),
                                tuple(map(sum, zip(self.position,(-2,0)))), # castling, 8
                                tuple(map(sum, zip(self.position,(2,0)))),]

    # display self
    def display(self):
        return self.color+'K'

    def positionNice(self):
        pos = ''
        if(self.position[0] == 0):
            pos = 'A'
        elif(self.position[0] == 1):
            pos = 'B'
        elif(self.position[0] == 2):
            pos = 'C'
        elif(self.position[0] == 3):
            pos = 'D'
        elif(self.position[0] == 4):
            pos = 'E'
        elif(self.position[0] == 5):
            pos = 'F'
        elif(self.position[0] == 6):
            pos = 'G'
        elif(self.position[0] == 7):
            pos = 'H'
        return pos+str(self.position[1]+1)
#
# End: King Class ###########################################################################################