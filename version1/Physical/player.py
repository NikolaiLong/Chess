# Chess Player
import copy
import sys
sys.path.append(".")
from board import *
from pieces import *
from moves import *

##########################################################################################################################################################
# Begin Player Class #####################################################################################################################################
##########################################################################################################################################################
class Player():
    # initialize a player
    # Begin Init ####################
    def __init__(self, color, board):
        self.check = False
        self.checkMate = False
        self.color = color
        self.board = board
        self.findAllPieces()
        self.findAllDestinations()
        self.findValidMoves()
    # End Init ######################

    # find all remaining pieces from the board
    # Begin Find All Peices ##################
    def findAllPieces(self):
        if(self.color == 'w'):
            self.pieces = self.board.wPieces
        elif(self.color == 'b'):
            self.pieces = self.board.bPieces
        else:
            print("!!!!!!!!!!!!!!color error!!!!!!!!!!!!!!!!!!!")
    # End Find All Pieces ####################

    # find all the desinations of the remaining pieces
    # Begin Find All Destinations ####################
    def findAllDestinations(self):
        for p in self.pieces:
            p.generatePossibleDestinations()
    # End Find All Destinations ######################

    # find all the valid moves from the destinations of the remaining pieces
    # Begin Find Valid Moves ###############################################
    def findValidMoves(self):
        from pieces import Empty
        self.validMoves = []
        self.check = False

        # check pawns
        from pieces import Pawn
        for p in self.pieces:
            if type(p) == Pawn:
                d = self.board.findPiece(p.allDestinations[0])
                if(d != None and type(d) == Empty):
                    self.validMoves.append(Move(p,d,'m',self.board)) # move
                    d = self.board.findPiece(p.allDestinations[1])
                    if(type(d) == Empty and not p.hasMoved):
                        self.validMoves.append(Move(p,d,'m2',self.board)) # move
                d = self.board.findPiece(p.allDestinations[2])
                if(d != None and type(d) != Empty and d.color != p.color):
                    self.validMoves.append(Move(p,d,'c',self.board)) # capture
                d = self.board.findPiece(p.allDestinations[3])
                if(d != None and type(d) != Empty and d.color != p.color):
                    self.validMoves.append(Move(p,d,'c',self.board)) # capture
                if self.color == 'w':
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[2], (0,-1)))))
                    if(d != None and type(d) == Pawn and d.hasMoved2 and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[3], (0,-1)))))
                    if(d != None and type(d) == Pawn and d.hasMoved2 and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture
                else:
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[2], (0,1)))))
                    if(d != None and type(d) == Pawn and d.hasMoved2 and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture
                    d = self.board.findPiece(tuple(map(sum, zip(p.allDestinations[3], (0,1)))))
                    if(d != None and type(d) == Pawn and d.hasMoved2 and d.color != p.color):
                        self.validMoves.append(Move(p,d,'ep',self.board)) # en passant capture

        # check rooks and bishops
        from pieces import Rook
        from pieces import Bishop
        self.tupleList = [(0,7),(7,14),(14,21),(21,28)]
        for p in self.pieces:
            if type(p) == Rook or type(p) == Bishop:
                for ind in range(4):
                    for num in range(self.tupleList[ind][0], self.tupleList[ind][1]):
                        d = self.board.findPiece(p.allDestinations[num])
                        if(d != None and type(d) == Empty):
                            self.validMoves.append(Move(p,d,'m',self.board)) # move
                        elif(d != None and type(d) != Empty and p.color != d.color):
                            self.validMoves.append(Move(p,d,'c',self.board)) # capture
                            break
                        else:
                            break

        # check knights
        from pieces import Knight
        for p in self.pieces:
            if type(p) == Knight:
                for num in range(8):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.validMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture

        # check queen
        from pieces import Queen
        self.tupleList = [(0,7),(7,14),(14,21),(21,28),(28,35),(35,42),(42,49),(49,56)]
        for p in self.pieces:
            if type(p) == Queen:
                for ind in range(8):
                    for num in range(self.tupleList[ind][0], self.tupleList[ind][1]):
                        d = self.board.findPiece(p.allDestinations[num])
                        if(d != None and type(d) == Empty):
                            self.validMoves.append(Move(p,d,'m',self.board)) # move
                        elif(d != None and type(d) != Empty and p.color != d.color):
                            self.validMoves.append(Move(p,d,'c',self.board)) # capture
                            break
                        else:
                            break

        # check king
        from pieces import King
        for p in self.pieces:
            if type(p) == King:
                self.king = p
                for num in range(8):
                    d = self.board.findPiece(p.allDestinations[num])
                    if(d != None and type(d) == Empty):
                        self.validMoves.append(Move(p,d,'m',self.board)) # move
                    elif(d != None and type(d) != Empty and p.color != d.color):
                        self.validMoves.append(Move(p,d,'c',self.board)) # capture
                if not p.hasMoved:
                    d = self.board.findPiece(p.allDestinations[8])
                    for r in self.pieces:
                        if(d != None and type(r) == Rook and r.position[0] == 0 and not r.hasMoved):
                            p1 = self.board.findPiece(tuple(map(sum, zip(p.position, (-1,0)))))
                            p2 = self.board.findPiece(tuple(map(sum, zip(p.position, (-2,0)))))
                            p3 = self.board.findPiece(tuple(map(sum, zip(p.position, (-3,0)))))
                            if(type(p1) == Empty and type(p2) == Empty and type(p3) == Empty):
                                self.validMoves.append(Move(p,d,'cl',self.board)) # castle long
                            break
                    d = self.board.findPiece(p.allDestinations[9])
                    for r in self.pieces:
                        if(d != None and type(r) == Rook and r.position[0] == 7 and not r.hasMoved):
                            p1 = self.board.findPiece(tuple(map(sum, zip(p.position, (1,0)))))
                            p2 = self.board.findPiece(tuple(map(sum, zip(p.position, (2,0)))))
                            if(type(p1) == Empty and type(p2) == Empty):
                                self.validMoves.append(Move(p,d,'cs',self.board)) # castle short
                            break
                break

        # check for king in check or in a pin
        count = self.kingCheck(self.king.position, 's')
        if(count > 0):
            self.check = True
        # check for king moving into or castling through check
        vCopy = copy.deepcopy(self.validMoves)
        for m in vCopy:
            for vm in self.validMoves:
                if(m.dest.position == vm.dest.position and m.piece.position == vm.piece.position):
                    m = vm
            if(type(m.piece) == King and (m.type == 'm' or m.type == 'c')):
                count = self.kingCheck(m.dest.position, 'm')
                if(count > 0):
                    self.validMoves.remove(m)
                    outFile = open("out.txt", "a")
                    outFile.write('KING REMOVE\n')
                    outFile.close()
            elif(type(m.piece) == King and m.type == 'cl'):
                count = self.kingCheck(m.piece.position, 'm')
                count = count + self.kingCheck(tuple(map(sum, zip(m.piece.position, (-1,0)))), 'm')
                count = count + self.kingCheck(tuple(map(sum, zip(m.piece.position, (-2,0)))), 'm')
                if(count > 0):
                    self.validMoves.remove(m)
                    outFile = open("out.txt", "a")
                    outFile.write('KING REMOVE\n')
                    outFile.close()
            elif(type(m.piece) == King and m.type == 'cs'):
                count = self.kingCheck(m.piece.position, 'm')
                count = count + self.kingCheck(tuple(map(sum, zip(m.piece.position, (1,0)))), 'm')
                count = count + self.kingCheck(tuple(map(sum, zip(m.piece.position, (2,0)))), 'm')
                if(count > 0):
                    self.validMoves.remove(m)
                    outFile = open("out.txt", "a")
                    outFile.write('KING REMOVE\n')
                    outFile.close()
        
        # check for checkmate
        if(len(self.validMoves) == 0):
            if(self.color == 'b'):
                self.cmNum = 1
            else:
                self.cmNum = 2
            self.board.log[self.board.turnNum-self.cmNum] += "#"
            self.checkMate = True
            print('\nCheckmate!')

        # check for check
        if(self.check and not self.checkMate):
            if(self.color == 'b'):
                self.cNum = 1
            else:
                self.cNum = 2
            self.board.log[self.board.turnNum-self.cNum] += "!"
            print('\nCheck!')
    # End Find Valid Moves #################################################

    # a position for all possibilities of being in check
    # Begin King Check #################################
    def kingCheck(self, position, tpe):
        from pieces import Empty
        from pieces import King
        count = 0
        
        # check by knight
        from pieces import Knight
        testKnight = Knight(self.color, position, 0)
        for num in range(8):
            d = self.board.findPiece(testKnight.allDestinations[num])
            if(d != None and type(d) == Knight and self.color != d.color):
                count = 1
                outFile = open("out.txt", "a")
                outFile.write('\n\nKNIGHT CHECK\n')
                outFile.close()
                if(tpe == 's'):
                    for index in range(len(self.validMoves)):
                        if(self.validMoves[index] != None and type(self.validMoves[index].piece) != King and self.validMoves[index].dest != d):
                            self.validMoves[index] = None
                            outFile = open("out.txt", "a")
                            outFile.write('KNIGHT REMOVE\n')
                            outFile.close()
                            

        # check by rook then bishop, i.e. queen
        from pieces import Rook
        from pieces import Bishop
        from pieces import Queen
        self.tupleList = [(0,7),(7,14),(14,21),(21,28)]
        for ip in range(2):
            if(ip == 0):
                self.printName = 'ROOK'
                self.printIDs = ['DOWN', 'UP', 'LEFT', 'RIGHT']
                self.testPiece = Rook(self.color, position, 0)
            else:
                self.printName = 'BISHOP'
                self.printIDs = ['DOWN-LEFT', 'UP-RIGHT', 'UP-LEFT', 'DOWN-RIGHT']
                self.testPiece = Bishop(self.color, position, 0)
            for ind in range(4):
                self.pin = False
                self.infront = 0
                self.pinnedPiece = self.testPiece
                self.checkDestinations = []
                for num in range(self.tupleList[ind][0], self.tupleList[ind][1]):
                    d = self.board.findPiece(self.testPiece.allDestinations[num])
                    self.checkDestinations.append(self.testPiece.allDestinations[num])
                    if(d != None and type(d) != Empty and ((self.color == d.color) or not (type(d) == type(self.testPiece) or type(d) == Queen))):
                        self.infront += 1
                        if(self.color == d.color):
                            self.pinnedPiece = d
                    elif(d != None and self.color != d.color and (type(d) == type(self.testPiece) or type(d) == Queen)):
                        if(self.infront == 1 and tpe == 's'):
                            self.pin = True
                        elif(self.infront == 0):
                            count = 1
                            outFile = open("out.txt", "a")
                            outFile.write(self.printName + ' CHECK ' + self.printIDs[ind] + '\n')
                            outFile.close()
                            if(tpe == 's'):
                                for index in range(len(self.validMoves)):
                                    self.cRB = 0
                                    if(self.validMoves[index] != None and type(self.validMoves[index].piece) == King and self.validMoves[index].dest.position == self.checkDestinations[0]):
                                        self.validMoves[index] = None
                                        outFile = open("out.txt", "a")
                                        outFile.write(self.printName + ' REMOVE' + '\n')
                                        outFile.close()
                                    if(self.validMoves[index] != None and type(self.validMoves[index].piece) != King):
                                        for pind in range(len(self.checkDestinations)):
                                            if(self.validMoves[index] != None and self.validMoves[index].dest.position == self.checkDestinations[pind]):
                                                self.cRB = 1
                                        if(self.cRB == 0):
                                            self.validMoves[index] = None
                                            outFile = open("out.txt", "a")
                                            outFile.write(self.printName + ' REMOVE' + '\n')
                                            outFile.close()
                        break
                if(tpe == 's' and self.pin):
                    outFile = open("out.txt", "a")
                    outFile.write(self.printName + ' PIN DETECTED ' + self.printIDs[ind] + '\n')
                    outFile.close()
                    for index in range(len(self.validMoves)):
                        self.canMovePin = False
                        if(self.validMoves[index] != None and self.validMoves[index].piece == self.pinnedPiece):
                            for pind in range(len(self.checkDestinations)):
                                if(self.validMoves[index].dest.position == self.checkDestinations[pind]):
                                    self.canMovePin = True
                            if(not self.canMovePin):
                                self.validMoves[index] = None
                                outFile = open("out.txt", "a")
                                outFile.write(self.printName + ' PIN REMOVE' + '\n')
                                outFile.close()
                                
        # check by pawn
        from pieces import Pawn
        if(self.color == 'w'):
            d1 = self.board.findPiece(tuple(map(sum, zip(position,(-1,1)))))
            d2 = self.board.findPiece(tuple(map(sum, zip(position,(1,1)))))
        else:
            d1 = self.board.findPiece(tuple(map(sum, zip(position,(-1,-1)))))
            d2 = self.board.findPiece(tuple(map(sum, zip(position,(1,-1)))))
        for ind in range(2):
            if(ind == 0):
                self.d = d1
                self.pawnID = 'LEFT'
            else:
                self.d = d2
                self.pawnID = 'RIGHT'
            if(self.d != None and type(self.d) == Pawn and self.color != self.d.color):
                count = 1
                outFile = open("out.txt", "a")
                outFile.write('PAWN CHECK ' + self.pawnID + '\n')
                outFile.close()
                if(tpe == 's'):
                    for index in range(len(self.validMoves)):
                        if(self.validMoves[index] != None and type(self.validMoves[index].piece) != King and self.validMoves[index].dest.position != self.d.position):
                            self.validMoves[index] = None
                            outFile = open("out.txt", "a")
                            outFile.write('PAWN REMOVE\n')
                            outFile.close()

        # eliminate None elements
        length = len(self.validMoves)
        i = 0
        while(i<length):
            if(self.validMoves[i] == None):
                self.validMoves.remove(self.validMoves[i])
                length -= 1
                continue
            i += 1

        return count
    # End King Check ###################################

    def executeMove2(self, dest, tpe):
        from pieces import Pawn
        for m in self.validMoves:
            if(tpe == 'cs' and m.type == tpe):
                m.execute()
                return True
            elif(type(m.piece) == Pawn and m.dest.position == dest):
                m.execute()
                return True
        return False

    def executeMove3(self, piece, dest, tpe):
        from pieces import Rook, Knight, Bishop, Queen, King
        move = None
        count = 0
        for m in self.validMoves:
            if(tpe == 'cl' and m.type == tpe):
                m.execute()
                return True
            elif(type(piece) == type(m.piece) and m.dest.position == dest):
                move = m
                count += 1
        if(count == 1):
            move.execute()
            return True
        elif(count > 1):
            print('more than one piece of the specified type can move to the specified destination')
            print("add the desired piece's position before it's destination")
        return False

    def executeMove4(self, column, dest):
        from pieces import Pawn
        for m in self.validMoves:
            if(type(m.piece) == Pawn and m.dest.position == dest and m.piece.position[0] == column):
                m.execute()
                return True
        return False

    def executeMove5(self, piece, place, dest):
        for m in self.validMoves:
            if(type(m.piece) == type(piece) and m.piece.position == place and m.dest.position == dest):
                m.execute()
                return True
        return False

    def executeMove6(self, piece, place, dest):
        for m in self.validMoves:
            if(type(m.piece) == type(piece) and m.piece.position == place and m.dest.position == dest):
                m.execute()
                return True
        return False

    # Display all available moves a player can make
    # Begin Display Moves #########################
    def displayMoves(self):
        for m in self.validMoves:
            m.display()
    # End Display Moves ###########################

    def displayMovesNice(self):
        for m in self.validMoves:
            m.displayNice()
##########################################################################################################################################################
# End Player Class #######################################################################################################################################
##########################################################################################################################################################