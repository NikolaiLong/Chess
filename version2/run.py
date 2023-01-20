
import sys

sys.path.append(".")
from protocol import play

sys.path.append("./game")
from player import Player
from board import Board


def run0():
  board = Board()
  black = Player(1, 1, board)
  white = Player(1, 0, board)

  inpt = None
  while 1:
    try:
      inpt = int(input(
        "\ntrain \n1 - naive neural net \n2 - convolusional neural net\n"
      ))
    except:
      print("type 1 or 2")
    if (inpt == 1 or inpt == 2):
      break
  
  print("\ninitializing training")
  play(board, black, white, inpt, True)
  return 0


def run1():
  inpt = None
  while 1:
    try:
      inpt = int(input("\nplay as black(1) or white(0)?\n"))
    except:
      print("type 0 or 1")
    if (inpt == 0 or inpt == 1):
      break
  board = Board()
  black = Player(not inpt, 1, board)
  white = Player(inpt, 0, board)

  inpt = None
  while 1:
    try:
      inpt = int(input(
        "\nplay against \n0 - decision tree (easy) \n1 - naive neural net (medium) \n2 - convolusional neural net (hard)\n"
      ))
    except:
      print("type 0, 1, or 2")
    if (inpt == 0 or inpt == 1 or inpt == 2):
      break

  print("\ninitializing single player game")
  play(board, black, white, inpt, False)
  return 0


def run2():
  board = Board()
  black = Player(0, 1, board)
  white = Player(0, 0, board)
  print("\ninitializing two player game")
  return 0


##########################################################################################
### run ##################################################################################
##########################################################################################

start = "##########################################################################################"

print(
  start + "\nwelcome to pop chess\n" + start + "\nhow would you like to proceed?" + \
  "\n0 - train a specified algorithm \n1 - play single player \n2 - play two player\n",
  end=""
)

while 1:
  match(input("")):
    case '0':
      cont = run0()
      break
    case '1':
      cont = run1()
      break
    case '2':
      cont = run2()
      break
    case other:
      print("type 0, 1, or 2")
