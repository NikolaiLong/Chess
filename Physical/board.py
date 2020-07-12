# Chess Board

import numpy as np
import sys
sys.path.append(".")
from pieces import *
from moves import *
from player import *

# Begin: Board Class ######################################################################################
# inherets object class
#
class Board(object):
    # initialize
    def __init__(self):
        print("pulled a board off the shelf,")
        self.grid = np.zeros((8,8), Piece)
        self.newPieces()
        self.wPlayer = Player('w', self.wPieces)
        self.bPlayer = Player('b', self.bPieces)
        self.gameOver = False
        self.turnNum = 1
        self.log = []

    # create new pieces in their starting positions
    def newPieces(self):
        print("and dusted off pieces; enjoy.. \n")
        self.wPieces = []
        self.bPieces = []
        self.empty = []
        for i in range(8):
            self.wPieces.append(Pawn('w',(1,i)))
            self.bPieces.append(Pawn('b',(6,i)))
        for i in [0,7]:
            self.wPieces.append(Rook('w',(0,i)))
            self.bPieces.append(Rook('b',(7,i)))
        for i in [1,6]:
            self.wPieces.append(Knight('w',(0,i)))
            self.bPieces.append(Knight('b',(7,i)))
        for i in [2,5]:
            self.wPieces.append(Bishop('w',(0,i)))
            self.bPieces.append(Bishop('b',(7,i)))
        self.wPieces.append(Queen('w',(0,3)))
        self.bPieces.append(Queen('b',(7,3)))
        self.wPieces.append(King('w',(0,4)))
        self.bPieces.append(King('b',(7,4)))
        for i in range(8):
            self.empty.append(Empty((2,i)))
            self.empty.append(Empty((3,i)))
            self.empty.append(Empty((4,i)))
            self.empty.append(Empty((5,i)))

    # piece movement method
    def move(self, place, dest):
        position = place.position
        place.position = dest.position
        dest.position = position

    # piece capture method
    def capture(self, place, dest):
        position = place.position
        place.position = dest.position
        if dest.color == 'w':
            self.wPieces.remove(dest)
        elif dest.color == 'b':
            self.bPieces.remove(dest)
        else:
            print('color assignment error')
            quit()
        self.empty.append(Empty(position))

    # prints the board
    def display(self):
        for p in self.wPieces:
            self.grid[self.flipCoordinates(p.position[0]), p.position[1]] = p
        for p in self.bPieces:
            self.grid[self.flipCoordinates(p.position[0]), p.position[1]] = p
        for e in self.empty:
            self.grid[self.flipCoordinates(e.position[0]), e.position[1]] = e
        sides = '____'
        topVerts = '         '
        print(sides.join(topVerts))
        self.printSpecial(0)
        print(sides.join('8||||||||'))
        self.printSpecial(1)
        print(sides.join('7||||||||'))
        self.printSpecial(2)
        print(sides.join('6||||||||'))
        self.printSpecial(3)
        print(sides.join('5||||||||'))
        self.printSpecial(4)
        print(sides.join('4||||||||'))
        self.printSpecial(5)
        print(sides.join('3||||||||'))
        self.printSpecial(6)
        print(sides.join('2||||||||'))
        self.printSpecial(7)
        print(sides.join('1||||||||'))
        print(" A    B    C    D    E    F    G    H")

    # flip the coordinates to account for numpy grid
    def flipCoordinates(self, y):
        y = 4 - (y - 3)
        return y

    # prints a row with peices
    def printSpecial(self, row):
        print("| %s | %s | %s | %s | %s | %s | %s | %s |" %
            (self.grid[row,0].display(), self.grid[row,1].display(), self.grid[row,2].display(),
            self.grid[row,3].display(), self.grid[row,4].display(), self.grid[row,5].display(),
            self.grid[row,6].display(), self.grid[row,7].display()))
#
# End: Board Class #######################################################################################