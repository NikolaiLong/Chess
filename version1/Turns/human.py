# Chess Human Turn

import sys
sys.path.append("../Physical")
from board import *
from player import *
from pieces import *
from moves import *

# two player turn
def turn(board, color):
    colorStr = ''
    player = None
    if color == 'w':
        player = board.wPlayer
    else:
        player = board.bPlayer
    player.findAllPieces()
    player.findAllDestinations()
    player.findValidMoves()
    if player.checkMate:
        board.gameOver = True
        return
    elif color == 'w':
        board.log.append(str(board.turnNum)+". ")
        colorStr = 'white'
    else:
        board.log[board.turnNum-1] += " "
        colorStr = 'black'
    while True:
        inStr = input("\nturn %d, %s to move: " %(board.turnNum, colorStr))
        if(inStr == 'q'):
            quit()
        elif(inStr == 'h'):
            helpDialogue()
            continue
        elif(inStr == 'l'):
            logDisp(board)
            continue
        elif(inStr == 'm'):
            print("\nnumber of moves available:", len(player.validMoves), "\navailable moves:\npiece  dest.    move type")
            player.displayMovesNice()
            print()
            continue
        elif(inStr == 'b'):
            boardSelect(board)
            continue
        elif(inStr == 'd'):
            board.display()
            continue
        elif(len(inStr) == 2):
            cont = findMove2(inStr, player)
            if cont:
                break
        elif(len(inStr) == 3):
            cont = findMove3(inStr, player)
            if cont:
                break
        elif(len(inStr) == 4):
            cont = findMove4(inStr, player)
            if cont:
                break
        elif(len(inStr) == 5):
            cont = findMove5(inStr, player)
            if cont:
                break
        elif(len(inStr) == 6):
            cont = findMove6(inStr, player)
            if cont:
                break
        print("incorrect input, type h to display the help dialogue, try again...")

# short castle and pawn push
def findMove2(inStr, player):
    board = player.board
    if(inStr == "oo"):
        ret = player.executeMove2((0,0),"cs")
        if(ret):
            board.log[board.turnNum-1] += "o-o"
            return True
        print("move not available, type m to display all available moves")
        return False
    x = convertL(inStr[0])
    y = convertN(inStr[1])
    if x == -1 or y == -1:
        return False
    ret = player.executeMove2((x,y),"m")
    if(ret):
        board.log[board.turnNum-1] += inStr
        return True
    print("move not available, type m to display all available moves")
    return False

# long castle and moving a piece
def findMove3(inStr, player):
    board = player.board
    if (inStr == "ooo"):
        ret = player.executeMove3(0,0,"cl")
        if(ret):
            board.log[board.turnNum-1] += "o-o-o"
            return True
        print("move not available, type m to display all available moves")
        return False
    p = convertP(inStr[0])
    x = convertL(inStr[1])
    y = convertN(inStr[2])
    if x == -1 or y == -1 or p == -1:
        return False
    ret = player.executeMove3(p,(x,y),"m")
    if(ret):
        board.log[board.turnNum-1] += inStr
        return True
    print("move not available, type m to display all available moves")
    return False

# capture with a pawn
def findMove4(inStr, player):
    board = player.board
    c = convertL(inStr[0])
    x = convertL(inStr[2])
    y = convertN(inStr[3])
    if(inStr[1] != 'x' or c == -1 or x == -1 or y == -1):
        return False
    ret = player.executeMove4(c,(x,y))
    if(ret):
        board.log[board.turnNum-1] += inStr
        return True
    print("move not available, type m to display all available moves")
    return False

# move a piece complex
def findMove5(inStr, player):
    board = player.board
    p = convertP(inStr[0])
    x1 = convertL(inStr[1])
    y1 = convertN(inStr[2])
    x2 = convertL(inStr[3])
    y2 = convertN(inStr[4])
    if(p == -1 or x1 == -1 or y1 == -1 or x2 == -1 or y2 == -1):
        return False
    ret = player.executeMove5(p,(x1,y1),(x2,y2))
    if(ret):
        board.log[board.turnNum-1] += inStr
        return True
    print("move not available, type m to display all available moves")
    return False

# capture with a piece
def findMove6(inStr, player):
    board = player.board
    p = convertP(inStr[0])
    x1 = convertL(inStr[1])
    y1 = convertN(inStr[2])
    x2 = convertL(inStr[4])
    y2 = convertN(inStr[5])
    if(inStr[3] != 'x' or p == -1 or x1 == -1 or y1 == -1 or x2 == -1 or y2 == -1):
        return False
    ret = player.executeMove5(p,(x1,y1),(x2,y2))
    if(ret):
        board.log[board.turnNum-1] += inStr
        return True
    print("move not available, type m to display all available moves")
    return False

def convertL(chr):
    if(chr == "a"):
        return 0
    elif(chr == "b"):
        return 1
    elif(chr == "c"):
        return 2
    elif(chr == "d"):
        return 3
    elif(chr == "e"):
        return 4
    elif(chr == "f"):
        return 5
    elif(chr == "g"):
        return 6
    elif(chr == "h"):
        return 7
    return -1

def convertN(chr):
    if(chr == "1"):
        return 0
    elif(chr == "2"):
        return 1
    elif(chr == "3"):
        return 2
    elif(chr == "4"):
        return 3
    elif(chr == "5"):
        return 4
    elif(chr == "6"):
        return 5
    elif(chr == "7"):
        return 6
    elif(chr == "8"):
        return 7
    return -1

def convertP(chr):
    from pieces import Rook, Knight, Bishop, Queen, King
    if(chr == 'r'):
        return Rook(' ',(-1,-1), 1000)
    elif(chr == 'n'):
        return Knight(' ',(-1,-1), 1000)
    elif(chr == 'b'):
        return Bishop(' ',(-1,-1), 1000)
    elif(chr == 'q'):
        return Queen(' ',(-1,-1), 1000)
    elif(chr == 'k'):
        return King(' ',(-1,-1), 1000)
    return -1

# display help dialogue
def helpDialogue():
    print("\nhelp dialogue:------------------------------------------------------")
    print("| types of input:                                                  |")
    print("|    pawn (examples):                                              |")
    print("|       'c4' (to push a pawn)                                      |")
    print("|       'cxe5' (to capture with a pawn)                            |")
    print("|    any other piece (examples):                                   |")
    print("|       'nc3' (to move a knight)                                   |")
    print("|       'nb1c3' (to move a knight)                                 |")
    print("|       'nb1xc3' (to capture with a knight)                        |")
    print("|    to castle:                                                    |")
    print("|       'oo' (castle short)                                        |")
    print("|       'ooo' (castle long)                                        |")
    print("|                                                                  |")
    print("| disclaimer: inputs must be lower case                            |")
    print("|             game log will be printed into log.txt                |")
    print("|             game output information will be printed to out.txt   |")
    print("|                                                                  |")
    print("| at any time:                                                     |")
    print("| type 'q' to quit                                                 |")
    print("| type 'h' to display this dialogue again                          |")
    print("| type 'l' to display the game log of all the moves made           |")
    print("| type 'm' to display all moves available to you                   |")
    print("| type 'b' to change the board size                                |")
    print("| type 'd' to display the board again                              |")
    print("--------------------------------------------------------------------\n")

# display move log
def logDisp(board):
    print("\nlog:--------")
    for t in board.log:
        print(t)
    print("------------")

# select a board
def boardSelect(board):
    print("which board size would you like?\n(small=1, medium=2, large=3, extralarge=4, 'enter' to leave)")
    while(True):
        num = input("")
        if(num == "1"):
            board.boardSize = 1
            board.display()
            break
        elif(num == "2"):
            print("this board size is not supported yet, only small and extralarge are functional")
        elif(num == "3"):
            print("this board size is not supported yet, only small and extralarge are functional")
        elif(num == "4"):
            board.boardSize = 4
            board.display()
            break
        elif(num == ""):
            break