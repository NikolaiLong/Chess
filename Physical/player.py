# Chess Player
import sys
sys.path.append(".")
from board import *
from pieces import *
from moves import *

# Begin Player Class ###########################################
#
class Player():
    # initialize
    def __init__(self, color, pieces, board):
        self.status = 'n'
        self.color = color
        self.pieces = pieces
        self.board = board
        self.findValidMoves()

    # find valid moves - rules check
    def findValidMoves(self):
        self.validMoves = []

        # check pawns
        for p in self.pieces:
            if type(p) == Pawn:
                d = self.board.findPiece(p.allDestinations[0])
                if(d != None and type(d) == Empty):
                    self.validMoves.append(Move(p,d,'m',self.board)) # move
                    d = self.board.findPiece(p.allDestinations[1])
                    if(type(d) == Empty and not p.hasMoved):
                        self.validMoves.append(Move(p,d,'m',self.board)) # move
                d = self.board.findPiece(p.allDestinations[2])
                if(d != None and type(d) != Empty and d.color != p.color):
                    self.validMoves.append(Move(p,d,'c',self.board)) # capture
                d = self.board.findPiece(p.allDestinations[3])
                if(d != None and type(d) != Empty and d.color != p.color):
                    self.validMoves.append(Move(p,d,'c',self.board)) # capture
                if self.color == 'w':
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[2], (0,-1)))))
                    if(d != None and type(d) == Pawn and d.justMovedTwice and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[3], (0,-1)))))
                    if(d != None and type(d) == Pawn and d.justMovedTwice and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture
                else:
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[2], (0,1)))))
                    if(d != None and type(d) == Pawn and d.justMovedTwice and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[3], (0,1)))))
                    if(d != None and type(d) == Pawn and d.justMovedTwice and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture

        # check rooks and bishops (they have the same movement type)
        for p in self.pieces:
            if type(p) == Rook or type(p) == Bishop:
                for num in range(7):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(7,14):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(14, 21):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(21, 28):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break

        # check knights
        for p in self.pieces:
            if type(p) == Knight:
                for num in range(8):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.validMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture

        # check queen
        for p in self.pieces:
            if type(p) == Queen:
                for num in range(7):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(7,14):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(14, 21):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(21, 28):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(28, 35):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(35, 42):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(42, 49):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                for num in range(49, 56):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                        break
                    else:
                        break
                break

        # check king
        for p in self.pieces:
            if type(p) == King:
                for num in range(8):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.vaildMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                if not p.hasMoved:
                    d = self.board.findPiece(p.allDestinations[8])
                    for r in self.pieces:
                        if(type(r) == Rook and r.position[0] == 0 and not r.hasMoved):
                            p1 = self.board.findPiece(tuple(map(sum, zip(p.position, (-1,0)))))
                            p2 = self.board.findPiece(tuple(map(sum, zip(p.position, (-2,0)))))
                            p3 = self.board.findPiece(tuple(map(sum, zip(p.position, (-3,0)))))
                            if(type(p1) == Empty and type(p2) == Empty and type(p3) == Empty):
                                self.validMoves.append(Move(p,d,'cl',self.board)) # castle long
                            break
                    d = self.board.findPiece(p.allDestinations[9])
                    for r in self.pieces:
                        if(type(r) == Rook and r.position[0] == 7 and not r.hasMoved):
                            p1 = self.board.findPiece(tuple(map(sum, zip(p.position, (1,0)))))
                            p2 = self.board.findPiece(tuple(map(sum, zip(p.position, (2,0)))))
                            if(type(p1) == Empty and type(p2) == Empty):
                                self.validMoves.append(Move(p,d,'cs',self.board)) # castle short
                            break
                break


        # check for king into or castling through check
        
        # check for king moving into check

        # check for pins

    def displayMoves(self):
        for m in self.validMoves:
            m.display()
#
# End Player Class #############################################