
import sys

sys.path.append(".")
from protocol import play, train

sys.path.append("./game")
from player import Player
from board import Board


##########################################################################################
### run functions ########################################################################
##########################################################################################


def main():
  start = "#########################################################################" + \
    "#################"

  print(
    start + "\nwelcome to pop chess\n" + start + "\nhow would you like to proceed" + \
    "\n0 - train a specified algorithm \n1 - play single player \n2 - play two player\n",
    end=""
  )

  while 1:
    match(input("")):
      case '0':
        run0()
        break
      case '1':
        run1()
        break
      case '2':
        run2()
        break
      case other:
        print("type 0, 1, or 2")


def run0():
  board = Board()
  black = Player(1, 1, board)
  white = Player(1, 0, board)

  algo = None
  while 1:
    try:
      algo = int(input(
        "\ntrain \n1 - neural net \n2 - convolusional neural net " + \
        "\n3 - convolusional neural net with random forest\n"
      ))
    except:
      print("type 1, 2, or 3")
    if (algo == 1 or algo == 2 or algo == 3):
      break

  diff = None
  while 1:
    try:
      diff = int(input(
        "\ndifficulty level easy(0), medium(1), or hard(2)\n"
      ))
    except:
      print("type 0, 1, or 2")
    if (diff == 0 or diff == 1 or diff == 2):
      break
  
  print("\ninitializing training")
  train(board, black, white, algo, diff)
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

  algo = None
  while 1:
    try:
      algo = int(input(
        "\nplay against what algorithm \n0 - decision tree \n1 - neural net " + \
        "\n2 - convolusional neural net \n3 - convolusional neural net with random forest\n"
      ))
    except:
      print("type 0, 1, or 2")
    if (algo == 0 or algo == 1 or algo == 2 or algo == 3):
      break

  diff = None
  while 1:
    try:
      diff = int(input(
        "\ndifficulty level easy(0), medium(1), or hard(2)\n"
      ))
    except:
      print("type 0, 1, or 2")
    if (diff == 0 or diff == 1 or diff == 2):
      break

  print("\ninitializing single player game")
  play(board, black, white, algo, diff)
  return 0


def run2():
  board = Board()
  black = Player(0, 1, board)
  white = Player(0, 0, board)

  print("\ninitializing two player game")
  play(board, black, white, 0, 0)
  return 0


##########################################################################################
### run ##################################################################################
##########################################################################################


if __name__ == "__main__":
  main()
  