# Chess!

!##############!  
!## COPYRIGHT: ##!  
!## igor's library ##!  
!##############!

#### Updates Coming Soon:
* log file upload to resume a position
* Executable file to play chess
* Medium and large chess board sizes (default is currently XL)
* NN advancement - computer is currently non existent

#### Prerequisites:
* Python 3 (3.8 or up prefered)
* Python Libraries:
    * numpy
    * abc
    - ... more in the future (might need to be updated)

#### To Do:
* Navigate to the Controls directory:
    * Play one or two player chess? $<play.py>
    * Run the neural network to teach the computer how to play? $<nn.py>

#### Repository:
Item | Description
-----|------------
Controls | Directory for the source code to run any chess functionality
Physical | Directory for the source code abstractions of physical chess elements
Storage | Directory to store an assortment of files
Turns | Directory for the source code abstractions for a turn in a chess game
info.txt | File with a brief overview of the connectivity of the abstractions

#### Disclaimer:
All coordinates in code are in (x,y) i.e. (column,row) format - then are transformed when printed