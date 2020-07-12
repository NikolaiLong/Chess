# playChess.py
## tests the turns
## plays a chess game

import sys
sys.path.append("../Turns")
from human import *
from computer import *
sys.path.append("../Physical")
from board import *

# define a two player game ############################################################################
def play2():
    print("\noh, so you want to play against a friend, let's see who's on their game")
    print("\ni started a game for you,")
    board = Board()
    board.display()
    helpDialogue()
    while not board.gameOver:
        turn(board, "w")
        if board.gameOver:
            break
        turn(board, "b")
        board.turnNum += 1

# define a one player game ###########################################################################
def play1():
    print("\noh, so you want to play against a me, let's see if you can handle my knowledge")
    print("\ni started a game for us,")
    board = Board()
    board.display()
    helpDialogue()
    while True:
        color = input("\ntype 'b' to play as black and 'w' to play as white: ")
        if color == 'w' or color == 'b':
            break
        print("incorrect input, try again")
    if color == 'w':
        while not board.gameOver:
            turn(board, 'w')
            if board.gameOver:
                break
            nnTurn(board, 'b')
            board.turnNum += 1
    elif color == 'b':
        while not board.gameOver:
            nnTurn(board, 'w')
            if board.gameOver:
                break
            turn(board, 'b')
            board.turnNum += 1

# initialize pregame measures #####################################################################
start = "##########################################################################################"
print('\n')
print(start)
print("copywrite: igor's library")
print(start)
print("\nyoo, i hope your day has been going well; maybe some chess could make it even better!")
print("\nwhat would you like to do?")
while True:
    toDo = input("type: '2' for two player or '1' for one player: ")
    if toDo == '2' or toDo == '1':
        break
    print("incorrect input, try again")
print()
print(start)
if toDo == "2":
    play2()
    cont = True
else:
    play1()
    cont = True