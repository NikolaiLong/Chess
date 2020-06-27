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
    def __init__(self):
        print("pulled a board off the shelf,")
        self.grid = np.zeros((8,8), Piece)
        self.addPieces()
        self.gameOver = False
        self.turnNum = 1
        self.log = []

    # add pieces for the begining of a game
    def addPieces(self):
        print("and dusted off pieces; enjoy.. \n")
        for i in range(8):
            self.grid[1,i] = Pawn('b',(1,i), self.grid)
            self.grid[2,i] = Empty((2,i))
            self.grid[3,i] = Empty((3,i))
            self.grid[4,i] = Empty((4,i))
            self.grid[5,i] = Empty((5,i))
            self.grid[6,i] = Pawn('w',(6,i), self.grid)
        for i in [0,7]:
            self.grid[0,i] = Rook('b',(0,i))
            self.grid[7,i] = Rook('w',(7,i))
        for i in [1,6]:
            self.grid[0,i] = Knight('b',(0,i))
            self.grid[7,i] = Knight('w',(7,i))
        for i in [2,5]:
            self.grid[0,i] = Bishop('b',(0,i))
            self.grid[7,i] = Bishop('w',(7,i))
        self.grid[0,3] = Queen('b',(0,3))
        self.grid[7,3] = Queen('w',(7,3))
        self.grid[0,4] = King('b',(0,4))
        self.grid[7,4] = King('w',(7,4))

    # board display methods
    def display(self):
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

    def printSpecial(self, row):
        print("| %s | %s | %s | %s | %s | %s | %s | %s |" %
            (self.grid[row,0].display(), self.grid[row,1].display(), self.grid[row,2].display(),
            self.grid[row,3].display(), self.grid[row,4].display(), self.grid[row,5].display(),
            self.grid[row,6].display(), self.grid[row,7].display()))

    # piece movement method
    def move(self, p1, p2, d1, d2):
        pass

    # test methods
    def addEmpty(self):
        for r in range(8):
            for c in range(8):
                self.grid[r,c] = Empty((r,c))

    def addOne(self, p, r, c):
        self.grid[r, c] = p
        self.display()
#
# End: Board Class #######################################################################################