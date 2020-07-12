# testChess.py
## tests the functionality of the board and pieces 

### to do
# - create data structure hierarchy
# 1. get all pieces working
# 2. add castling inputs
# 3. add move restrictions for when the king is in check
# 4. improve input system: Nf3

import sys
sys.path.append("../Physical")
from board import *
from player import *
from pieces import *
from moves import *

# test methods #################################################################################
# test general board movement methods
def move(board):
    board.move(board.wPieces[0], board.empty[12])
    print('number of white pieces:', len(board.wPieces))
    print('number of black pieces:', len(board.bPieces))
    print('number of empty pieces:', len(board.empty))

def capture(board):
    board.capture(board.wPieces[0], board.bPieces[0])
    print('number of white pieces:', len(board.wPieces))
    print('number of black pieces:', len(board.bPieces))
    print('number of empty pieces:', len(board.empty))

# test pawn
def testPawnSwap():
    pass

def testPawnCapture():
    pass

# test knight
def testKnightSwap():
    pass

def testKnightCapture():
    pass

# test bishop
def testBishopSwap():
    pass

def testBishopCapture():
    pass

# test rook
def testRookSwap():
    pass

def testRookCapture():
    pass

# test queen
def testQueenSwap():
    pass

def testQueenapture():
    pass

# test king
def testKingSwap():
    pass

def testKingCapture():
    pass

# initialize an empty board ###################################################################
board = Board()
#for r in range(8):
#    for c in range(8):
#        board.grid[r,c] = Empty((r,c))
#board.grid[3,3] = Pawn('b', (3,3))
board.display()
print('number of white pieces:', len(board.wPieces))
print('number of black pieces:', len(board.bPieces))
print('number of empty pieces:', len(board.empty))
#move(board)
#capture(board)
#print(board.wPieces[0].allDestinations)
#print(board.bPieces[0].allDestinations)
#board.bPieces[15].displayMoves()
#board.display()