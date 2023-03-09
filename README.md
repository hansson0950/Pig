# Pig (Dice Game) with Unittests

## Description
This Python project is an implementation of the classic game of Pig, a simple dice game where two players take turns rolling a die, with the goal of being the first player to reach a certain score threshold. In this implementation, the score threshold is set to 100.

## Installation
You can download the project files from the GitHub repository at https://github.com/hansson0950/Pig. Once downloaded, you can navigate to the project directory and run the game using the following command: <application/game.py>. 

## Usage
When first starting the program, it will prompt the user with a main menu. They get the following options: "1. Start Game, 2. Rules, 3. High Scores and 4. Exit". 
- Option 2 will display the set of rules we chose to use in our version of the game. 
- Option 3 will display the five best scores. The highest scores are determined by the number of turns it took to reach 100 points.
- Option 4 will shut down the program.
- Option 1 will start by asking the user how many players will play. They can choose either one player or two players. Choosing one player will start a game against the computer. Choosing two players will start the game with two players.

When the game starts, the game will ask you if you would like to roll or hold. At this time, you can choose a number of options even though only [y/n] is prompted.
- "y" rolls the die and adds the number of the die to the current turn points. However, if the player rolls a 1, they will get a bust. Current turn points     are lost and the turn goes over to the other player.
- "n" does not roll the die and instead adds the current turn points to the total score.
- "rename" lets the user rename themselves in the midst of an on-going game. 
- "cheat" gives the player 100 points, which means that the user can hold their next move and win (for testing purposes only).
- "exit" quits the current game and navigates the user back to the main menu.

## Unittests
This project also includes a suite of unittests to test the various functions of the game. To run the unittests, navigate to the project directory and run the following command: <python -m unittest discover -s unit_tests>.

This will run all of the unittests in the tests directory and report the results. The unittests cover the following modules:
- game.py: This class starts the program and handles all the necessary logic and method calls.
- player.py: Creates an object of a player and handles most available moves a player can make inside the game.
- computer.py: Inherits the player class, has its own logic for when to roll or hold. The computer will roll until it reaches a turn score of 20 or more,       then it will hold. If the total score + turn score equals 100 or more, it will hold.
- dice.py: Responsible for the dice rolls.
- high_score.py: Handles all high scores by reading and writing to the file called high_scores.txt.
- ui.py: Manages almost, if not all, prints to the terminal.

## Documentation
It is possible to generate documentation from the code and the python docstrings. To do this, navigate to the folder which contains the classes you would like to create documentation for. Then, use the command <python -m pdoc3 --html <class_name.py>> to generate documentation as HTML.

It is also possible to generate UML diagrams for the classes as well as the packages. To do this, navigate to the folder which contains the classes you would like to create UML diagrams for. Then, use the command <pyreverse dice.py> and then <dot -Tpng classes.dot -o classes.png> to get a .png file. You can do the same for the packages with the command <dot -Tpng packages.dot -o packages.png>.

Note: This requires installation of some necessary softwares such as chocolatey and graphviz.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Before submitting a pull request, please make sure that your changes do not break any of the existing unittests and that any new code is properly documented.

## Credits
- Emil Hansson https://github.com/hansson0950
- Simon Wikström https://github.com/Simon-W1

## License
This project is licensed under the MIT License. See the LICENSE.md file for more information.
