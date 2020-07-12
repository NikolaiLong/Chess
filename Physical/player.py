# Chess Player

# Begin Player Class ###########################################
#
class Player():
    # initialize
    def __init__(self, color, pieces):
        self.status = 'n'
        self.pieces = pieces
        self.findValidMoves()

    # find valid moves - rules check
    def findValidMoves(self):
        self.validMoves = []
        pass
#
# End Player Class #############################################