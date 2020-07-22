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

    # display
    def display(self):
        print(self.piece.display(), self.dest.display(), self.type)
#
# End Move Class ############################################