"""UI class."""


class UI:
    """UI class."""

    def display_welcome(self):
        """Welcome."""
        print("Welcome to Pig!")

    def display_scores(self, player1, player2):
        """Display scores."""
        # pylint: disable-msg=C0301
        print(f"Current Scores:\n{player1.name}: {player1.score}\n{player2.name}: {player2.score}") # noqa

    def display_roll(self, roll):
        """Display the roll."""
        print(f"Roll: {roll}")

    def display_bust(self):
        """Display when user busts."""
        print("Bust! Your turn is over.")

    def ask_roll_again(self):
        """Ask user if they want to roll again."""
        return input("Roll again? [y/n]").lower() == "y"

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
        print(f"High Scores:\n\
              1. {highscores[0]}\n\
              2. {highscores[1]}\n\
              3. {highscores[2]}\n\
              4. {highscores[3]}\n\
              5. {highscores[4]}")

    def display_rules(self):
        """Display the rules of the game."""
        print("Rules:\n- Each turn, a player repeatedly rolls a \
          die until either a 1 is rolled or the player decides to hold.\n- If \
          the player rolls a 1, they score nothing and their turn ends.\n- \
          If the player rolls any other number, it is added to their turn \
          total and the player's turn continues.\n- If the player \
          chooses to hold, their turn total is added to their score, \
          and it becomes the next player's turn.\n- The first \
          player to score 100 or more points wins.")

    def ask_player_name(self):
        """Ask the name of the player."""
        return input("Enter your name: ")
