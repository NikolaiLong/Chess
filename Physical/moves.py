# Chess Move

# Begin Move Class ##########################################
#
class Move():
    # initialize
    def __init__(self, piece, dest):
        self.piece = piece
        self.dest = dest

    # display
    def display(self):
        print(self.piece.display(), self.dest)
#
# End Move Class ############################################