# Janggi - Korean Chess

## Description

This is an implentation of the board game Janggi (Korean chess). The game engine was written as a class project for CS162 at Oregon State University. The GUI, which makes it much more convenient to play, was developed later after the class concluded.

![janggi_gui](https://user-images.githubusercontent.com/51836567/119905181-9378ba00-bf00-11eb-9547-a01ad44ac678.gif)

## Prerequisites

Python 3 must be installed to run the text-based version and Pygame is additionally required to run the GUI version.

## Setup

JanggiGame.py and JanggiGUI.py must be in the same directory and the images directory should be present as a sub-directory. 

For the text-based version run python.exe JanggiGame.py.

For the GUI version run python.exe JanggiGui.py.

Python and the .py files must be preceded by their respective paths.

The size of the GUI can be adjusted by changing the value of BOARD_TARGET_HEIGHT in JanggiGUI.py.

## How to play

Rules for allowed moves, check, and checkmate conditions can be found at https://en.wikipedia.org/wiki/Janggi. Specifics for the two versions (GUI and text-based) are below. Both versions are for two players. The GUI version also highlights allowed moves and alerts the user of check and checkmate states, making it beginner friendly.

### GUI version

Mouse clicks are used to move pieces by selecting one and choosing one of the highlighted destinations. Pieces can be unselected by clicking them again or  clicking outside of the allowed destinations. The pass button can be used to skip turns. 

### Text-based version

The game is played by entering positions (e.g., a1, i10) when prompted, which indicate which piece to move and where to move it. Turns can be passed by specifying the same position to move to and from. 

## Credit for Assets

The board is from Github user Ka-hu: https://github.com/Ka-hu/chess-pieces

It is licensed under CC-BY-4.0.

The piece images are from Wikimedia Commons: https://commons.wikimedia.org/wiki/Category:Janggi_pieces

They are available under Creative Commons.

## License

The python scripts can be used in accordance with the MIT License.
