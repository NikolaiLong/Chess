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
        self.grid = np.zeros((8,8), Piece)
        self.newPieces()
        self.wPlayer = Player('w', self)
        self.bPlayer = Player('b', self)
        self.gameOver = False
        self.boardSize = 4
        self.turnNum = 1
        self.log = []

    # create new pieces in their starting positions
    def newPieces(self):
        self.wPieces = []
        self.bPieces = []
        self.empty = []
        for i in range(8):
            self.wPieces.append(Pawn('w',(i,1),10+i))
            self.bPieces.append(Pawn('b',(i,6),10+i))
        for i in [0,7]:
            self.wPieces.append(Rook('w',(i,0),20+i))
            self.bPieces.append(Rook('b',(i,7),20+i))
        for i in [1,6]:
            self.wPieces.append(Knight('w',(i,0),30+i))
            self.bPieces.append(Knight('b',(i,7),30+i))
        for i in [2,5]:
            self.wPieces.append(Bishop('w',(i,0),40+i))
            self.bPieces.append(Bishop('b',(i,7),40+i))
        self.wPieces.append(Queen('w',(3,0),50))
        self.bPieces.append(Queen('b',(3,7),50))
        self.wPieces.append(King('w',(4,0),60))
        self.bPieces.append(King('b',(4,7),60))
        for i in range(8):
            self.empty.append(Empty((i,2)))
            self.empty.append(Empty((i,3)))
            self.empty.append(Empty((i,4)))
            self.empty.append(Empty((i,5)))
        self.allPieces = self.wPieces + self.bPieces + self.empty

    # assign pieces to specific lists
    def allocatePieces(self):
        self.empty = []
        self.wPieces = []
        self.bPieces = []
        for p in self.allPieces:
            p.hasMoved2 = False
            if(type(p) == Empty):
                self.empty.append(p)
            elif(p.color == 'w'):
                self.wPieces.append(p)
            elif(p.color == 'b'):
                self.bPieces.append(p)
            else:
                print("!!!!!!!!!!!!!!color error!!!!!!!!!!!!!!!!!!!")

    def findPiece(self, position):
        for p in self.allPieces:
            if p.position == position:
                return p
        return None

    # choose which display
    def display(self):
        if(self.boardSize == 2):
            self.display2()
        elif(self.boardSize == 3):
            self.display3()
        elif(self.boardSize == 4):
            self.display4()
        else:
            self.display1()

    # prints the small board
    def display1(self):
        self.allocatePieces()
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

    # prints the medium board
    def display2(self):
        pass

    # prints the large board
    def display3(self):
        pass

    # prints the extra large board
    def display4(self):
        self.allocatePieces()
        for p in self.wPieces:
            self.grid[7-p.position[1], p.position[0]] = p
        for p in self.bPieces:
            self.grid[7-p.position[1], p.position[0]] = p
        for e in self.empty:
            self.grid[7-e.position[1], e.position[0]] = e
        self.printTop()
        self.printEvenTop()
        self.printRowEven(0)
        self.printEvenBottom(8)
        self.printOddTop()
        self.printRowOdd(1)
        self.printOddBottom(7)
        self.printEvenTop()
        self.printRowEven(2)
        self.printEvenBottom(6)
        self.printOddTop()
        self.printRowOdd(3)
        self.printOddBottom(5)
        self.printEvenTop()
        self.printRowEven(4)
        self.printEvenBottom(4)
        self.printOddTop()
        self.printRowOdd(5)
        self.printOddBottom(3)
        self.printEvenTop()
        self.printRowEven(6)
        self.printEvenBottom(2)
        self.printOddTop()
        self.printRowOdd(7)
        self.printOddBottom(1)
        print("A                   B                  C                  D                  E                  F                  G                  H")
    
    def printTop(self):
        for index in range(8):
            print(" __________________", end="")
        print()

    def printEvenTop(self):
        for index in range(4):
            print("|##################|                  ", end="")
        print("|")

    def printEvenBottom(self,num):
        print("%d##################|__________________" % (num), end="")
        for index in range(3):
            print("|##################|__________________", end="")
        print("|")

    def printOddTop(self):
        for index in range(4):
            print("|                  |##################", end="")
        print("|")

    def printOddBottom(self,num):
        print("%d__________________|##################" % (num), end="")
        for index in range(3):
            print("|__________________|##################", end="")
        print("|")
    
    def printRowEven(self, row):
        for index in range(5):
            col = 0
            while col < 8:
                self.printRow('w',index,col,row)
                self.printRow('b',index,col+1,row)
                col += 2
            print("|")

    def printRowOdd(self, row):
        for index in range(5):
            col = 0
            while col < 8:
                self.printRow('b',index,col,row)
                self.printRow('w',index,col+1,row)
                col += 2
            print("|")

    def printRow(self, color, index, column, row):
        from pieces import Empty, Pawn, Rook, Knight, Bishop, Queen, King
        p = self.grid[row,column]
        if(type(p) == Empty):
            if color == 'w':
                print("|##################", end="")
            else:
                print("|                  ", end="")
        else:
            print(p.display4(color,index), end="")
                

#
# End: Board Class #######################################################################################