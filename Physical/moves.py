# Chess Move

# Begin Move Class ##########################################
#
class Move():
    # initialize both parameters are of Piece type
    def __init__(self, piece, dest, tpe, board):
        self.piece = piece
        self.dest = dest
        self.type = tpe
        self.board = board
        # need special options for pawn promotion
        # special options for castling

    # display
    def display(self):
        print(self.piece.display(), self.piece.position, '|', self.dest.display(), self.dest.position, '|', self.type)
#
# End Move Class ############################################