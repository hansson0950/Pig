"""Unit tests for the UI."""
import unittest
from unittest.mock import patch
from io import StringIO

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from ui import UI  # noqa
from player import Player  # noqa
from high_score import HighScore  # noqa


class UITest(unittest.TestCase):
    """UI test."""

    def setup(self):
        """Initialize the tests for the UI."""
        self.ui = UI()

    def test_display_welcome(self):
        """Display welcome message."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_welcome()
            self.assertEqual(fake_out.getvalue().strip(), "Welcome to Pig!")

    def test_display_scores_one_player(self):
        """Display scores in a one-player-game."""
        player = Player("John")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_scores(player)
            self.assertEqual(fake_out.getvalue().strip(),
                             "Current Scores:\nJohn: 0")

    def test_display_scores_two_players(self):
        """Display scores in a two-player-game."""
        player1 = Player("John")
        player2 = Player("Rob")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_scores(player1, player2)
            self.assertEqual(fake_out.getvalue().strip(),
                             "Current Scores:\nJohn: 0\nRob: 0")

    def test_display_roll(self):
        """Display the roll."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_roll(3)
            self.assertEqual(fake_out.getvalue().strip(), "Roll: 3")

    def test_display_bust(self):
        """Display when a one is rolled."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_bust()
            self.assertEqual(fake_out.getvalue().strip(),
                             "Bust! Your turn is over.")

    def test_ask_roll_again(self):
        """Display "Roll again?"."""
        with patch('builtins.input', return_value='y'):
            self.assertTrue(self.ui.ask_roll_again())
        with patch('builtins.input', return_value='n'):
            self.assertFalse(self.ui.ask_roll_again())

    def test_display_turn(self):
        """Display turns."""
        player = Player("John")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_turn(player)
            self.assertEqual(fake_out.getvalue().strip(), "John's turn!")

    def test_display_turn_end(self):
        """Display turn end."""
        player = Player("John")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_turn_end(player)
            self.assertEqual(fake_out.getvalue().strip(),
                             "John's turn is over.")

    def test_display_game_over(self):
        """Display game over."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_game_over()
            self.assertEqual(fake_out.getvalue().strip(), "Game over!")

    def test_display_high_scores(self):
        """Display high scores."""
        high_score = HighScore()
        high_score.add_score("John", 100)
        high_score.add_score("Rob", 50)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.ui.display_high_scores(high_score)
            self.assertEqual(fake_out.getvalue().strip(),
                             "High Scores:\n1. John (100)\n2. Rob (50)")

    def test_display_rules(self):
        """Display rules."""
        self.ui.display_rules()
        expected_output = "Rules:\n- Each turn, a player repeatedly rolls a \
          die until either a 1 is rolled or the player decides to hold.\n- If \
          the player rolls a 1, they score nothing and their turn ends.\n- \
          If the player rolls any other number, it is added to their turn \
          total and the player's turn continues.\n- If the player \
          chooses to hold, their turn total is added to their score, \
          and it becomes the next player's turn.\n- The first \
          player to score 100 or more points wins."
        self.assertEqual(
            self.ui.stdout.getvalue().strip(),
            expected_output
        )

    def test_ask_player_name(self):
        """Display player name."""
        self.ui.input = MagicMock(return_value="John")
        self.assertEqual(self.ui.ask_player_name(1), "John")


if __name__ == "__main__":
    unittest.main()
