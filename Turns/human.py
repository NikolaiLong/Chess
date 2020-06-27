# Chess Turns:
#             for two and one player games only

import numpy as np

import sys
sys.path.append(".")

# two player turn
def turn(board, color):
    if color == 'w':
        print("\nturn %d: white to move" %board.turnNum)
    else:
        print("\nturn %d: black to move" %board.turnNum)
    while True:
        try:
            
            pdstr = input("<char><int>;<char><int>: ")
            if pdstr == 'q':
                break
            elif pdstr == 'help':
                helpDialogue()
            elif pdstr == 'log':
                logDisp()
            else:
                place, dest = pdstr.split(";")
                char1 = ord(place[0])
                num1 = ord(place[1])
                char2 = ord(dest[0])
                num2 = ord(dest[1])
                if (len(pdstr) != 5 or char1 < 97 or char1 > 104 or num1 < 49 or num1 > 56 or 
                        char2 < 97 or char2 > 104 or num2 < 49 or num2 > 56):
                    print("2: invalid syntax; retry input or quit")
                else:
                    break
        except:
            print("1: invalid syntax; retry input or quit")
    if pdstr == 'q':
        quit()
    if color == "w":
        board.log.append(str(board.turnNum) + '. ' + str(place) + " " + str(dest))
    else:
        board.log.append("   " + str(place) + " " + str(dest))
    print(board.turnNum, '.', place, dest)
    p1 = char1 - 97
    p2 = num1 - 49
    d1 = char2 - 97
    d2 = num2 - 49
    p2, d2 = flipCoordinates(p2, d2)
    #move(p1, p2, d1, d2, color)

# display help dialogue
def helpDialogue():
    print("\nhelp dialogue:---------------------------------------------------------------------------")
    print("| type the square of the piece you want to move <;> then the square of its destination  |")
    print("| example turn input: c2;c4 (the English Opening)                                       |")
    #print("| type cs for short castle, cl for long castle") need to implement castling
    print("| disclaimer: inputs must be lower case                                                 |")
    print("|                                                                                       |")
    print("| at any time:                                                                          |")
    print("| type 'q' to quit                                                                      |")
    print("| type 'help' to display this dialogue again                                            |")
    print("| type 'log' to display the game log of all the moves made                              |")
    #print("| type 'print' to write the log to a csv file which you can load to resume the game     |")
    print("-----------------------------------------------------------------------------------------")

# display move log
def logDisp(self):
    print("\nlog:--------")
    for t in self.log:
        print("|", t, "|")
    print("------------")

# flip the coordinates to account for
def flipCoordinates(self, y1, y2):
    y1 = 4 - (y1 - 3)
    y2 = 4 - (y2 - 3)
    return y1, y2        

def move(self, p1, p2, d1, d2, color):
    place = self.board.grid[p2, p1]
    dest = self.board.grid[d2, d1]
    if self.badMove(place, dest, color):
        print("3: invalid move; retry the turn or quit")
        self.turn2(color)
    elif type(dest) == Empty:
        if place.swap(dest):
            self.board.swap(p1, p2, d1, d2)
        else:
            print("4: invalid move; retry the turn or quit")
            self.turn2(color)
    elif (type(dest) != Empty):
        if place.capture(dest):
            self.board.capture(p1, p2, d1, d2)
        else:
            print("5: invalid move; retry the turn or quit")
            self.turn2(color)
    else:
        print("6: invalid move; retry the turn or quit")
        self.turn2(color)

def badMove(self, place, dest, color):
    if not isinstance(place, Piece) or not isinstance(dest, Piece) or type(place) == Empty:
        return True
    if place.color != color:
        return True
    #elif : king is in check situations
    return False