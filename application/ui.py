"""UI class."""


class UI:
    """A class made for the user interface.

    ### Description:
    A class for managing the user interface of the Pig game.
    It handles most, if not all, print operations.

    ### Attributes:
    - None

    ### Methods:
    - display_welcome(self): Displays a welcome message.
    - display_scores(self, player1, player2): Displays the scores of the
      players.
    - display_roll(self, roll): Displays the result of a roll.
    - display_bust(self): Displays a message when the user busts.
    - ask_roll(self): Asks the user if they want to roll again.
    - display_turn(self, name): Displays the name of the player whose turn it
      is.
    - display_turn_end(self, name): Displays a message when a player's turn is
      over.
    - display_game_over(self): Displays a message when the game is over.
    - display_high_scores(self, highscores): Displays the high scores.
    - display_rules(self): Displays the rules of the game.
    - ask_player_name(self, players): Asks the name(s) of the player(s).
    - display_menu(self): Displays the game menu with options and returns user
      input.
    - ask_player_amount(self): Asks the number of players for a game.
    - display_turn_score(self, points): Displays the score for the current
      turn.
    """

    def display_welcome(self):
        """Welcome.

        ### Description:
        Prints a simple welcome message when the game starts.
        """
        print("\nWelcome to Pig!")

    def display_scores(self, player1, player2):
        """Display scores.

        ### Description:
        Displays the current scores of the game between the two players,
        or player and computer. This is printed every time a player
        is about to roll.

        ### Args:
        - player1 (obj): The object of the first player.
        - player2 (obj): The object of the second player.
        """
        # pylint: disable-msg=C0301
        print("\n---------------\n")
        print(f"Current Scores:\n{player1.name}: {player1.score}\n{player2.name}: {player2.score}\n") # noqa

    def display_roll(self, roll):
        """Display the roll.

        ### Description:
        Displays the result of a roll.

        ### Args:
        - roll (int): The result of the roll
        """
        print(f"Roll: {roll}")

    def display_bust(self):
        """Display when user busts.

        ### Description:
        This is printed when the player rolls a one.
        """
        print("Bust! Your turn is over.")

    def ask_roll(self):
        """Ask user if they want to roll.

        ### Description:
        Asks the user if they want to roll, accepts an input.

        ### Returns:
        - string: Whatever the user inputted, will print 'Invalid Input' if
          they input something other than 'y', 'n', 'cheat', 'rename' or 'exit'
        """
        return input("Roll? [y/n]\n").lower()

    def display_turn(self, name):
        """Display turn.

        ### Description:
        Displays whose turn it is.

        ### Args:
        - name (string): The name of the player whose turn it is.
        """
        print(f"{name}'s turn!")

    def display_turn_end(self, name):
        """Display turn end.

        ### Description:
        Displays the name of the player whose turn is over.

        ### Args:
        - name (str): The name of the player whose turn is over.
        """
        print(f"{name}'s turn is over.")

    def display_game_over(self):
        """Display game over.

        ### Description:
        Displays 'Game over!' when someone successfully reaches 100 points
        and chooses to hold.
        """
        print("Game over!")

    def display_high_scores(self, highscores):
        """Display high scores.

        ## Description:
        Displays the local high scores.

        ### Args:
        - highscores (list): The list of the high scores, containing strings
          of the names and number of turns to reach 100 points.
        """
        print("\nHigh Scores:")
        for score in highscores:
            print(score)
        print()

    def display_rules(self):
        """Display rules.

        ### Description:
        Displays the rules of the game.
        """
        # pylint: disable-msg=C0301
        print("Rules:\n- Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold.") # noqa
        print("- If the player rolls a 1, they score nothing and their turn ends.")  # noqa
        print("- If the player rolls any other number, it is added to their turn total and the player's turn continues.") # noqa
        print("- If the player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")  # noqa
        print("- The first player to score 100 or more points wins.\n")

    def ask_player_name(self, players):
        """Ask player name.

        ### Description:
        Asks the player to enter their name before the game starts.

        ### Args:
        - players (int): The number of players.

        ### Returns:
        - str: The name of the player in a single player game
        - list: The names of both players in a two player game.
        """
        if players == 1:
            return input("\nEnter your name: ")

        player1 = input("\nEnter the first player's name: ")
        player2 = input("Enter the second player's name: ")
        return [player1, player2]

    def display_menu(self):
        """Display menu.

        ### Description:
        Displays the menu with four different options and returns the input.

        ### Returns:
        - int: The option the user chose.
        """
        return input("1. Start Game\n2. Rules\n3. High Scores\n4. Exit\n")

    def ask_player_amount(self):
        """Ask player amount.

        ### Description:
        Ask how many players will play.

        ### Returns:
        - int: One or two, depending on how many will play.
        """
        return input("\n1. One Player\n2. Two Players\n")

    def display_turn_score(self, points):
        """Display turn score.

        ### Description:
        Displays the score for the current turn.
        """
        print(f"Total points this turn: {points}")
