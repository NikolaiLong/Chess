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

# load a game ################################################################################
def loadGame():
    step = input("\nlet pick up where we left off; would you like to step through each move? (Yes='enter', No=n")
    pass

# two player game ############################################################################
def play2():
    print("\noh, so you want to play against a friend, let's see who's on their game")
    load = ""
    load = input("\nwould you like to load a game? If yes, copy the log file into the Controls directory and type it's name here. If not hit 'enter'. ")
    if load != "":
        loadGame()
        return
    print("\ni started a game for you,")
    print("pulled a board off the bookshelf,")
    print("and dusted off some pieces; enjoy..")
    board = Board()
    helpDialogue()
    board.display()
    outFile = open("out.txt", "w")
    outFile.close()
    logFile = open("log.txt", "w")
    logFile.write("log:--------\n")
    logFile.close()
    printLast = False
    while not board.gameOver:
        turn(board, "w")
        if board.turnNum > 1:
            logFile = open("log.txt", "a")
            logFile.write(board.log[board.turnNum-2]+"\n")
            logFile.close()
        if board.gameOver:
            break
        board.display()
        printLast = True
        turn(board, "b")
        if not board.gameOver:
            printLast = False
            board.display()
        board.turnNum += 1
    logFile = open("log.txt", "a")
    if printLast:
        logFile.write(board.log[board.turnNum-2]+"\n")
    logFile.write("------------")
    logFile.close()
    print("\ngreat game! the game log has been stored in log.txt; change it's name if you don't want it to be overwritten!")
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
    if toDo == '2' or toDo == '1' or toDo == '':
        break
    print("incorrect input, try again...")
print()
print(start)
if toDo == "2" or toDo == "":
    play2()
else:
    print("the computer has not been taught how to play chess yet, sorry")
    quit()
    play1()