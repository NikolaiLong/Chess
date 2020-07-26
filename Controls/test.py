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

def moveB(board, place, dest):
    print('MOVE')
    board.move(board.bPieces[place], board.empty[dest])
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

def captureB(board, place, dest):
    print('CAPTURE')
    board.capture(board.bPieces[place], board.wPieces[dest])
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
def testKing():
    board = Board()
    board.display()

    input('\nwhite to move')
    print('\nWHITE MOVES')
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 2, 9)
    board.wPlayer.pieces[2].hasMoved = True
    
    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 3, 14)
    board.bPlayer.pieces[3].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    capture(board, 2, 3)
    board.wPlayer.pieces[2].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    captureB(board, 13, 2)
    board.bPlayer.pieces[13].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 9, 8)
    board.wPlayer.pieces[9].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 13, 30)
    board.bPlayer.pieces[13].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 9, 17)
    board.wPlayer.pieces[9].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 13, 29)
    board.bPlayer.pieces[13].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 9, 15)
    board.wPlayer.pieces[9].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 14, 33)
    board.bPlayer.pieces[14].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 13, 9)
    board.wPlayer.pieces[13].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 11, 25)
    board.bPlayer.pieces[11].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 1, 4)
    board.wPlayer.pieces[1].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 9, 11)
    board.bPlayer.pieces[9].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 11, 4)
    board.wPlayer.pieces[11].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 5, 27)
    board.bPlayer.pieces[5].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 13, 12)
    board.wPlayer.pieces[13].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 7, 11)
    board.bPlayer.pieces[7].hasMoved = True

    input('\nwhite to move')
    print('\nWHITE MOVES')
    board.wPlayer.findAllPieces()
    board.wPlayer.findAllDestinations()
    board.wPlayer.findValidMoves()
    print(len(board.wPlayer.validMoves))
    board.wPlayer.displayMoves()
    move(board, 9, 22)
    board.wPlayer.pieces[9].hasMoved = True

    input('\nblack to move')
    print('\nBLACK MOVES')
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()
    moveB(board, 9, 13)
    board.bPlayer.pieces[9].hasMoved = True
    board.bPlayer.findAllPieces()
    board.bPlayer.findAllDestinations()
    board.bPlayer.findValidMoves()
    print(len(board.bPlayer.validMoves))
    board.bPlayer.displayMoves()

def testCastle():
    pass

def testPawnPromote():
    pass

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
testKing()