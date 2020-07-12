# Chess Pieces

from abc import ABC
import sys
sys.path.append(".")
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
    
    # special display of: position
    def dispCPP(self):
        return #position
#
# End: Empty Place Class #####################################################################################

# Begin: Pawn Class ##########################################################################################
#
class Pawn(Piece):
    # initialize
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()
        self.generatePossibleMoves()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        if self.color == 'w':
            self.allDestinations = [tuple(map(sum, zip(self.position,(-1,0)))),
                                    tuple(map(sum, zip(self.position,(-2,0)))),
                                    tuple(map(sum, zip(self.position,(-1,-1)))),
                                    tuple(map(sum, zip(self.position,(-1,1))))]
        elif self.color == 'b':
            self.allDestinations = [tuple(map(sum, zip(self.position,(1,0)))),
                                    tuple(map(sum, zip(self.position,(2,0)))),
                                    tuple(map(sum, zip(self.position,(1,-1)))),
                                    tuple(map(sum, zip(self.position,(1,1))))]
        else:
            print('color assignment error')
            quit()

    # generate possible moves
    def generatePossibleMoves(self):
        self.allMoves = []
        for dest in self.allDestinations:
            self.allMoves.append(Move(self, dest))

    # display self
    def display(self):
        return self.color+'P'

    # display moves
    def displayMoves(self):
        for m in self.allMoves:
            m.display()
#
# End: Pawn Class ###########################################################################################

# Begin: Rook Class ########################################################################################
#
class Rook(Piece):
    # initialize
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()
        self.generatePossibleMoves()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))), # moving left
                                tuple(map(sum, zip(self.position,(0,-2)))),
                                tuple(map(sum, zip(self.position,(0,-3)))),
                                tuple(map(sum, zip(self.position,(0,-4)))),
                                tuple(map(sum, zip(self.position,(0,-5)))),
                                tuple(map(sum, zip(self.position,(0,-6)))),
                                tuple(map(sum, zip(self.position,(0,-7)))),
                                tuple(map(sum, zip(self.position,(0,1)))), # moving right
                                tuple(map(sum, zip(self.position,(0,2)))),
                                tuple(map(sum, zip(self.position,(0,3)))),
                                tuple(map(sum, zip(self.position,(0,4)))),
                                tuple(map(sum, zip(self.position,(0,5)))),
                                tuple(map(sum, zip(self.position,(0,6)))),
                                tuple(map(sum, zip(self.position,(0,7)))),
                                tuple(map(sum, zip(self.position,(-1,0)))), # moving down
                                tuple(map(sum, zip(self.position,(-2,0)))),
                                tuple(map(sum, zip(self.position,(-3,0)))),
                                tuple(map(sum, zip(self.position,(-4,0)))),
                                tuple(map(sum, zip(self.position,(-5,0)))),
                                tuple(map(sum, zip(self.position,(-6,0)))),
                                tuple(map(sum, zip(self.position,(-7,0)))),
                                tuple(map(sum, zip(self.position,(1,0)))), # moving right
                                tuple(map(sum, zip(self.position,(2,0)))),
                                tuple(map(sum, zip(self.position,(3,0)))),
                                tuple(map(sum, zip(self.position,(4,0)))),
                                tuple(map(sum, zip(self.position,(5,0)))),
                                tuple(map(sum, zip(self.position,(6,0)))),
                                tuple(map(sum, zip(self.position,(7,0))))]

    # generate possible moves
    def generatePossibleMoves(self):
        self.allMoves = []
        for dest in self.allDestinations:
            self.allMoves.append(Move(self, dest))

    # display self
    def display(self):
        return self.color+'R'

    # display moves
    def displayMoves(self):
        for m in self.allMoves:
            m.display()
#
# End: Rook Class ##########################################################################################

# Begin: Knight Class #######################################################################################
#
class Knight(Piece):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.generatePossibleDestinations()
        self.generatePossibleMoves()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(2,-1)))),
                                tuple(map(sum, zip(self.position,(2,1)))),
                                tuple(map(sum, zip(self.position,(1,-2)))),
                                tuple(map(sum, zip(self.position,(1,2)))),
                                tuple(map(sum, zip(self.position,(-2,-1)))),
                                tuple(map(sum, zip(self.position,(-2,1)))),
                                tuple(map(sum, zip(self.position,(-1,-2)))),
                                tuple(map(sum, zip(self.position,(-1,2))))]

    # generate possible moves
    def generatePossibleMoves(self):
        self.allMoves = []
        for dest in self.allDestinations:
            self.allMoves.append(Move(self, dest))

    # display self
    def display(self):
        return self.color+'N'

    # display moves
    def displayMoves(self):
        for m in self.allMoves:
            m.display()
#
# End: Knight Class ########################################################################################

# Begin: Bishop Class #######################################################################################
#
class Bishop(Piece):
    # initialize
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.generatePossibleDestinations()
        self.generatePossibleMoves()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(-1,-1)))), # moving down-left
                                tuple(map(sum, zip(self.position,(-2,-2)))),
                                tuple(map(sum, zip(self.position,(-3,-3)))),
                                tuple(map(sum, zip(self.position,(-4,-4)))),
                                tuple(map(sum, zip(self.position,(-5,-5)))),
                                tuple(map(sum, zip(self.position,(-6,-6)))),
                                tuple(map(sum, zip(self.position,(-7,-7)))),
                                tuple(map(sum, zip(self.position,(1,1)))), # moving up-right
                                tuple(map(sum, zip(self.position,(2,2)))),
                                tuple(map(sum, zip(self.position,(3,3)))),
                                tuple(map(sum, zip(self.position,(4,4)))),
                                tuple(map(sum, zip(self.position,(5,5)))),
                                tuple(map(sum, zip(self.position,(6,6)))),
                                tuple(map(sum, zip(self.position,(7,7)))),
                                tuple(map(sum, zip(self.position,(-1,1)))), # moving down-right
                                tuple(map(sum, zip(self.position,(-2,2)))),
                                tuple(map(sum, zip(self.position,(-3,3)))),
                                tuple(map(sum, zip(self.position,(-4,4)))),
                                tuple(map(sum, zip(self.position,(-5,5)))),
                                tuple(map(sum, zip(self.position,(-6,6)))),
                                tuple(map(sum, zip(self.position,(-7,7)))),
                                tuple(map(sum, zip(self.position,(1,-1)))), # moving up-left
                                tuple(map(sum, zip(self.position,(2,-2)))),
                                tuple(map(sum, zip(self.position,(3,-3)))),
                                tuple(map(sum, zip(self.position,(4,-4)))),
                                tuple(map(sum, zip(self.position,(5,-5)))),
                                tuple(map(sum, zip(self.position,(6,-6)))),
                                tuple(map(sum, zip(self.position,(7,-7))))]

    # generate possible moves
    def generatePossibleMoves(self):
        self.allMoves = []
        for dest in self.allDestinations:
            self.allMoves.append(Move(self, dest))

    # display self
    def display(self):
        return self.color+'B'

    # display moves
    def displayMoves(self):
        for m in self.allMoves:
            m.display()
#
# End: Bishop Class #########################################################################################

# Begin: Queen Class ########################################################################################
#
class Queen(Piece):
    # initialize
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.generatePossibleDestinations()
        self.generatePossibleMoves()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))), # moving left
                                tuple(map(sum, zip(self.position,(0,-2)))),
                                tuple(map(sum, zip(self.position,(0,-3)))),
                                tuple(map(sum, zip(self.position,(0,-4)))),
                                tuple(map(sum, zip(self.position,(0,-5)))),
                                tuple(map(sum, zip(self.position,(0,-6)))),
                                tuple(map(sum, zip(self.position,(0,-7)))),
                                tuple(map(sum, zip(self.position,(0,1)))), # moving right
                                tuple(map(sum, zip(self.position,(0,2)))),
                                tuple(map(sum, zip(self.position,(0,3)))),
                                tuple(map(sum, zip(self.position,(0,4)))),
                                tuple(map(sum, zip(self.position,(0,5)))),
                                tuple(map(sum, zip(self.position,(0,6)))),
                                tuple(map(sum, zip(self.position,(0,7)))),
                                tuple(map(sum, zip(self.position,(-1,0)))), # moving down
                                tuple(map(sum, zip(self.position,(-2,0)))),
                                tuple(map(sum, zip(self.position,(-3,0)))),
                                tuple(map(sum, zip(self.position,(-4,0)))),
                                tuple(map(sum, zip(self.position,(-5,0)))),
                                tuple(map(sum, zip(self.position,(-6,0)))),
                                tuple(map(sum, zip(self.position,(-7,0)))),
                                tuple(map(sum, zip(self.position,(1,0)))), # moving up
                                tuple(map(sum, zip(self.position,(2,0)))),
                                tuple(map(sum, zip(self.position,(3,0)))),
                                tuple(map(sum, zip(self.position,(4,0)))),
                                tuple(map(sum, zip(self.position,(5,0)))),
                                tuple(map(sum, zip(self.position,(6,0)))),
                                tuple(map(sum, zip(self.position,(7,0)))),
                                tuple(map(sum, zip(self.position,(-1,-1)))), # moving down left
                                tuple(map(sum, zip(self.position,(-2,-2)))),
                                tuple(map(sum, zip(self.position,(-3,-3)))),
                                tuple(map(sum, zip(self.position,(-4,-4)))),
                                tuple(map(sum, zip(self.position,(-5,-5)))),
                                tuple(map(sum, zip(self.position,(-6,-6)))),
                                tuple(map(sum, zip(self.position,(-7,-7)))),
                                tuple(map(sum, zip(self.position,(1,1)))), # moving up right
                                tuple(map(sum, zip(self.position,(2,2)))),
                                tuple(map(sum, zip(self.position,(3,3)))),
                                tuple(map(sum, zip(self.position,(4,4)))),
                                tuple(map(sum, zip(self.position,(5,5)))),
                                tuple(map(sum, zip(self.position,(6,6)))),
                                tuple(map(sum, zip(self.position,(7,7)))),
                                tuple(map(sum, zip(self.position,(-1,1)))), # moving down right
                                tuple(map(sum, zip(self.position,(-2,2)))),
                                tuple(map(sum, zip(self.position,(-3,3)))),
                                tuple(map(sum, zip(self.position,(-4,4)))),
                                tuple(map(sum, zip(self.position,(-5,5)))),
                                tuple(map(sum, zip(self.position,(-6,6)))),
                                tuple(map(sum, zip(self.position,(-7,7)))),
                                tuple(map(sum, zip(self.position,(1,-1)))), # moving up left
                                tuple(map(sum, zip(self.position,(2,-2)))),
                                tuple(map(sum, zip(self.position,(3,-3)))),
                                tuple(map(sum, zip(self.position,(4,-4)))),
                                tuple(map(sum, zip(self.position,(5,-5)))),
                                tuple(map(sum, zip(self.position,(6,-6)))),
                                tuple(map(sum, zip(self.position,(7,-7))))]

    # generate possible moves
    def generatePossibleMoves(self):
        self.allMoves = []
        for dest in self.allDestinations:
            self.allMoves.append(Move(self, dest))

    # diplay self
    def display(self):
        return self.color+'Q'

    # display moves
    def displayMoves(self):
        for m in self.allMoves:
            m.display()
#
# End: Queen Class ##########################################################################################

# Begin: King Class #########################################################################################
#
class King(Piece):
    # initialize
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.hasMoved = False
        self.generatePossibleDestinations()
        self.generatePossibleMoves()

    # generate possible move destinations
    def generatePossibleDestinations(self):
        self.allDestinations = [tuple(map(sum, zip(self.position,(0,-1)))),
                                tuple(map(sum, zip(self.position,(0,1)))),
                                tuple(map(sum, zip(self.position,(-1,0)))),
                                tuple(map(sum, zip(self.position,(1,0)))),
                                tuple(map(sum, zip(self.position,(-1,-1)))),
                                tuple(map(sum, zip(self.position,(1,1)))),
                                tuple(map(sum, zip(self.position,(1,-1)))),
                                tuple(map(sum, zip(self.position,(-1,1)))),
                                tuple(map(sum, zip(self.position,(0,-2)))), # castling
                                tuple(map(sum, zip(self.position,(0,2)))),]

    # generate possible moves
    def generatePossibleMoves(self):
        self.allMoves = []
        for dest in self.allDestinations:
            self.allMoves.append(Move(self, dest))

    # display self
    def display(self):
        return self.color+'K'

    # display moves
    def displayMoves(self):
        for m in self.allMoves:
            m.display()
#
# End: King Class ###########################################################################################