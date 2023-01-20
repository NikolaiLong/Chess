
import sys

sys.path.append("./game")
from player import Player
from board import Board


def play(board : Board, black : Player, white : Player, algo : int, train : bool):
  return 0