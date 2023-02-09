
import sys

sys.path.append(".")
from board import Board

##########################################################################################
### defines player #######################################################################
##########################################################################################

class Player():
  def __init__(self, machine: bool, color : int, board : Board):
    self.machine = machine
    self.color = color
    self.board = board

    self.in_check_mate = False
    self.in_check = False

    self.moves = self.find_all_moves()


  def find_all_moves(self) -> None:

    self.find_in_check_or_mate()
    if (self.in_check_mate):
      return
    
    self.get_moves()


  def find_in_check_or_mate(self) -> None:
    return 0


  def get_moves(self) -> list:
    # 1. get list of possible moves
    # 2. validate moves
    #   a. board constraints
    #   b. piece constraints
    #     i. self pieces
    #     ii. enemy pieces
    #   c. non-check constraints
    return []
    