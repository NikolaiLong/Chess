# Play Chess

import sys
sys.path.append("../Turns")
from human import *
from computer import *
sys.path.append("../Physical")
from board import *
from player import *
from pieces import *
from moves import *

# two player game ############################################################################
def play2():
    print("\noh, so you want to play against a friend, let's see who's on their game")
    print("\ni started a game for you,")
    print("pulled a board off the bookshelf,")
    print("and dusted off some pieces; enjoy..")
    board = Board()
    helpDialogue()
    board.display()
    while not board.gameOver:
        turn(board, "w")
        if board.gameOver:
            break
        board.display()
        turn(board, "b")
        board.display()
        board.turnNum += 1
    print("\ngreat game! the game log has been stored in log.txt, change it's name if you don't want it to be overwritten!")
    print("hope you play again soon! bye..")
    print(start)

# one player game ###########################################################################
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
    print("incorrect input, try again...")
print()
print(start)
if toDo == "2":
    play2()
else:
    print("the computer has not been taught how to play chess yet, sorry")
    quit()
    play1()