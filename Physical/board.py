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
        self.wPlayer = Player('w', self.wPieces, self)
        self.bPlayer = Player('b', self.bPieces, self)
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
            self.wPieces.append(Pawn('w',(i,1)))
            self.bPieces.append(Pawn('b',(i,6)))
        for i in [0,7]:
            self.wPieces.append(Rook('w',(i,0)))
            self.bPieces.append(Rook('b',(i,7)))
        for i in [1,6]:
            self.wPieces.append(Knight('w',(i,0)))
            self.bPieces.append(Knight('b',(i,7)))
        for i in [2,5]:
            self.wPieces.append(Bishop('w',(i,0)))
            self.bPieces.append(Bishop('b',(i,7)))
        self.wPieces.append(Queen('w',(3,0)))
        self.bPieces.append(Queen('b',(3,7)))
        self.wPieces.append(King('w',(4,0)))
        self.bPieces.append(King('b',(4,7)))
        for i in range(8):
            self.empty.append(Empty((i,2)))
            self.empty.append(Empty((i,3)))
            self.empty.append(Empty((i,4)))
            self.empty.append(Empty((i,5)))
        self.allPieces = self.wPieces + self.bPieces + self.empty

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

    def findPiece(self, position):
        for p in self.allPieces:
            if p.position == position:
                return p
        return None

    # prints the board
    def display(self):
        for p in self.wPieces:
            self.grid[7-p.position[1], p.position[0]] = p
        for p in self.bPieces:
            self.grid[7-p.position[1], p.position[0]] = p
        for e in self.empty:
            self.grid[7-e.position[1], e.position[0]] = e
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

    # prints a row with peices
    def printSpecial(self, row):
        print("| %s | %s | %s | %s | %s | %s | %s | %s |" %
            (self.grid[row,0].display(), self.grid[row,1].display(), self.grid[row,2].display(),
            self.grid[row,3].display(), self.grid[row,4].display(), self.grid[row,5].display(),
            self.grid[row,6].display(), self.grid[row,7].display()))
#
# End: Board Class #######################################################################################