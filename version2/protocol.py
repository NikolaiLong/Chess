
import sys

sys.path.append("./game")
from player import Player
from board import Board

sys.path.apend("./machine")
from machine import Machine


##########################################################################################
### protocol functions ###################################################################
##########################################################################################


def train(board : Board, black : Player, white : Player, algo : int, diff : int):
  return

def play(board : Board, black : Player, white : Player, algo : int, diff : int):
  machine = None
  if white.machine:
    machine = Machine(board, white, black, algo, diff)
  elif black.machine:
    machine = Machine(board, black, white)

  players = [white, black]
  while 1:
    for player in players:
      if player.in_check_mate:
        print("\ncheckmate!")
        return
      elif player.machine:
        turn_machine(board, machine)
      else:
        turn_user(board, player)


def turn_machine(board, machine):
  # 0: if board.turn == 1 -> print board

  # 1: print message (running algorithm)

  # 2: run algorithm
  return


def turn_user(board, player):
  # 1: print board


  # 2: move input

  # 3: print board
  return


def input_menu() -> str:
  return ""
