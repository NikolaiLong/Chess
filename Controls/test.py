# testChess.py
## tests the functionality of the board and pieces 

### to do
# - create data structure hierarchy
# 1. get all pieces working
# 2. add castling inputs
# 3. add move restrictions for when the king is in check
# 4. improve input system: Nf3

import sys
sys.path.append("./Physical")
from board import *
from pieces import *
from moves import *

# initialize an empty board ###################################################################
board = Board()
board.addEmpty()
board.display()

# test pieces #################################################################################
# test pawn
def testPawnSwap():
    pass

def testPawnCapture():
    pass

# test knight
def testPawnSwap():
    pass

def testPawnCapture():
    pass

# test bishop
def testPawnSwap():
    pass

def testPawnCapture():
    pass

# test rook
def testPawnSwap():
    pass

def testPawnCapture():
    pass

# test queen
def testPawnSwap():
    pass

def testPawnCapture():
    pass

# test king
def testPawnSwap():
    pass

def testPawnCapture():
    pass