
import sys

sys.path.append(".")
from piece import Piece

import numpy as np

##########################################################################################
### defines board ########################################################################
##########################################################################################

class Board():

  size_converter = {
    0: [2,5],
    1: [7,19]
  }

  def __init__(self):
    self.grid = np.zeros((8,8), Piece)
    self.size = 1

  def print(self):

    for row in range(0,8):
      for col in range(0,8):
        for 
