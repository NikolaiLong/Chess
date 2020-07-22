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

# basic tests #################################################################################
def initi(board):
    print('INITIALIZE')
    board.display()
    print('number of white pieces:', len(board.wPieces))
    print('number of black pieces:', len(board.bPieces))
    print('number of empty pieces:', len(board.empty))
    print()

def move(board, place, dest):
    print('MOVE')
    board.move(board.wPieces[place], board.empty[dest])
    print('number of white pieces:', len(board.wPieces))
    print('number of black pieces:', len(board.bPieces))
    print('number of empty pieces:', len(board.empty))
    board.display()
    print()

def capture(board, place, dest):
    print('CAPTURE')
    board.capture(board.wPieces[place], board.bPieces[dest])
    print('number of white pieces:', len(board.wPieces))
    print('number of black pieces:', len(board.bPieces))
    print('number of empty pieces:', len(board.empty))
    board.display()
    print()

def allDestinations(board, num):
    print('ALL DESTINATIONS')
    print('WHITE:', num)
    print(board.wPieces[num].allDestinations)
    print('BLACK', num)
    print(board.bPieces[num].allDestinations)
    board.display()
    print()

# basic test call
def basicTests():
    board = Board()
    initi(board)
    move(board, 0, 12)
    capture(board, 0, 0)
    allDestinations(board, 0)

# test players #############################################################################
def testPlayers():
    board = Board()
    board.display()
    print('\nWHITE MOVES')
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    print('\nBLACK MOVES')
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    move(board, 2, 8)
    board.wPlayer.pieces[2].hasMoved = True
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print('\nWHITE MOVES')
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()

# test pawn #################################################################################
def testPawnSwap(board, color, num):
    if color == 'w':
        place = board.wPieces[2]
    elif color == 'b':
        place = board.bPieces[2]
    else:
        print("something went wrong")
        quit()
    dest = place.allDestinations[num]
    for e in board.empty:
        if e.position == dest:
            dest = e
    board.move(place, dest)
    board.display()

def testPawnCapture(board, color, num):
    pass

# pawn test call
def pawnTests():
    # WHITE #
    # move forward 1
    print('\n1\nmoving white c pawn 1')
    board = Board()
    testPawnSwap(board, 'w', 0)
    # move forward 2
    print('\n2\nmoving white c pawn 2')
    board = Board()
    testPawnSwap(board, 'w', 1)
    # capture left
    print('\n3\ncapturing with white c pawn on left')
    board = Board()
    testPawnCapture(board, 'w', 2)
    # capture right
    print('\n4\ncapturing with white c pawn on right')
    board = Board()
    testPawnCapture(board, 'w', 3)

    # BLACK #
    # move forward 1
    print('\n1\nmoving black c pawn 1')
    board = Board()
    testPawnSwap(board, 'b', 0)
    # move forward 2
    print('\n2\nmoving black c pawn 2')
    board = Board()
    testPawnSwap(board, 'b', 1)
    # capture left
    print('\n3\ncapturing with black c pawn on left')
    board = Board()
    testPawnCapture(board, 'b', 2)
    # capture right
    print('\n4\ncapturing with black c pawn on right')
    board = Board()
    testPawnCapture(board, 'b', 3)

# test knight #################################################################################
def testKnightSwap():
    pass

def testKnightCapture():
    pass

# test bishop #################################################################################
def testBishopSwap():
    pass

def testBishopCapture():
    pass

# test rook #################################################################################
def testRookSwap():
    pass

def testRookCapture():
    pass

# test queen #################################################################################
def testQueenSwap():
    pass

def testQueenapture():
    pass

# test king #################################################################################
def testKingSwap():
    pass

def testKingCapture():
    pass

# call tests #################################################################################
print("##########################################################################################")
#basicTests()
#pawnTests()
testPlayers()