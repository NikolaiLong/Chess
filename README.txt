# chess
# author: Nikolai Long
# ################################################## #
# COPYRIGHT:                                         #
#           igor's library                           #
# ################################################## #

Prerequisites:
- Python 3 (3.8 or up prefered)
- Python Libraries:
    - numpy
    - abc
    - ...

To Do:
- Play two or one player? $<Controls/play.py> or $<Controls\play.py>
- Test piece movement for accuracy? $<Controls/test.py> or $<Controls\test.py>
- Run the neural network to teach the computer how to play? $<Controls/nn.py> or $<Controls\nn.py>
[depending on your system]

Structure{
> Controls
    - test
    - play
    - nn [neural network]
> Turns
    - human
    - computer
> Physical
    - board
    - pieces
    - moves
    - player
> Storage [TBD]
    - nnData [TBD]
}

Connectivity{
~ Controls | HAVE | Physical
           | USE  | Turns
~ Turns    | USE  | Physical
}

Controls Hierarchy{
test
  |
board

      play
   _____|______
  |     |      |
board human computer

     nn
   ___|___
  |      |
board computer
}

Turns Hierarchy{
human
  |
board

 computer
   __|___
  |     |
board nnData
}

Physical Hierarchy (circular connectivity){
    board
   ___|___
  |      |
pieces player[s]
  |
moves

   player
   ___|___
  |      |
pieces moves
  |
moves
}