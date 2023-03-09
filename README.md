# Pig (Dice Game) with Unittests

## Description
This Python project is an implementation of the classic game of Pig, a simple dice game where two players take turns rolling a die, with the goal of being the first player to reach a certain score threshold. In this implementation, the score threshold is set to 100.

## Installation
You can download the project files from the GitHub repository at https://github.com/hansson0950/Pig. Once downloaded, you can navigate to the project directory and run the game using the following command: <application/game.py>.

## Unittests
This project also includes a suite of unittests to test the various functions of the game. To run the unittests, navigate to the project directory and run the following command: <python -m unittest discover -s unit_tests>.

This will run all of the unittests in the tests directory and report the results. The unittests cover the following modules:
- game.py: This class starts the program and handles all the necessary logic and method calls.
- player.py: Creates an object of a player and handles most available moves a player can make inside the game.
- computer.py: Inherits the player class, has its own logic for when to roll or hold.
- dice.py: Responsible for the dice rolls.
- high_score.py: Handles all high scores by reading and writing to the file called high_scores.txt.
- ui.py: Manages almost, if not all, prints to the terminal.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Before submitting a pull request, please make sure that your changes do not break any of the existing unittests and that any new code is properly documented.

## Credits
- Emil Hansson https://github.com/hansson0950
- Simon Wikström https://github.com/Simon-W1

## License
This project is licensed under the MIT License. See the LICENSE.md file for more information.