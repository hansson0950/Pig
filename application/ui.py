"""UI class."""


class UI:
    """UI class."""

    def display_welcome(self):
        """Welcome."""
        print("\nWelcome to Pig!")

    def display_scores(self, player1, player2):
        """Display scores."""
        # pylint: disable-msg=C0301
        print("\n---------------\n")
        print(f"Current Scores:\n{player1.name}: {player1.score}\n{player2.name}: {player2.score}\n") # noqa

    def display_roll(self, roll):
        """Display the roll."""
        print(f"Roll: {roll}")

    def display_bust(self):
        """Display when user busts."""
        print("Bust! Your turn is over.")

    def ask_roll_again(self):
        """Ask user if they want to roll again."""
        return input("Roll? [y/n]\n").lower()

    def display_turn(self, name):
        """Display turn."""
        print(f"{name}'s turn!")

    def display_turn_end(self, name):
        """Display turn end."""
        print(f"{name}'s turn is over.")

    def display_game_over(self):
        """Display "Game over!"."""
        print("Game over!")

    def display_high_scores(self, highscores):
        """Display the high scores."""
        print("\nHigh Scores:")
        for score in highscores:
            print(score)
        print()

    def display_rules(self):
        """Display the rules of the game."""
        # pylint: disable-msg=C0301
        print("Rules:\n- Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold.") # noqa
        print("- If the player rolls a 1, they score nothing and their turn ends.")  # noqa
        print("- If the player rolls any other number, it is added to their turn total and the player's turn continues.") # noqa
        print("- If the player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.")  # noqa
        print("- The first player to score 100 or more points wins.\n")

    def ask_player_name(self, players):
        """Ask the name of the player."""
        if players == 1:
            return input("\nEnter your name: ")

        player1 = input("\nEnter the first player's name: ")
        player2 = input("Enter the second player's name: ")
        return [player1, player2]

    def display_menu(self):
        """Display game menu with options and return user input."""
        return input("1. Start Game\n2. Rules\n3. High Scores\n4. Exit\n")

    def ask_player_amount(self):
        """Ask how many players should play a game."""
        return input("\n1. One Player\n2. Two Players\n")

    def display_turn_score(self, points):
        """Display the score for the current turn."""
        print(f"Total points this turn: {points}")
