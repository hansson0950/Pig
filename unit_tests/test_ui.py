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

    def setUp(self):
        """Initialize the tests for the UI."""
        self.ui = UI()  # pylint: disable-msg=C0103

    def test_display_welcome(self):
        """Test display welcome message."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_welcome()
            self.assertEqual(fake_out.getvalue().strip(), "Welcome to Pig!")

    def test_display_scores(self):
        """Test display scores in a two-player-game."""
        player1 = Player("John")
        player2 = Player("Rob")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_scores(player1, player2)
            self.assertEqual(
                fake_out.getvalue().strip(),
                "---------------\n\nCurrent Scores:\nJohn: 0\nRob: 0")

    def test_display_roll(self):
        """Test display roll."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_roll(3)
            self.assertEqual(fake_out.getvalue().strip(), "Roll: 3")

    def test_display_bust(self):
        """Test display when a one is rolled."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_bust()
            self.assertEqual(fake_out.getvalue().strip(),
                             "Bust! Your turn is over.")

    def test_display_ask_roll(self):
        """Test display "Roll?"."""
        with patch("builtins.input", return_value="y"):
            self.assertEqual(self.ui.ask_roll(), "y")
        with patch("builtins.input", return_value="n"):
            self.assertEqual(self.ui.ask_roll(), "n")
        with patch("builtins.input", return_value="cheat"):
            self.assertEqual(self.ui.ask_roll(), "cheat")
        with patch("builtins.input", return_value="rename"):
            self.assertEqual(self.ui.ask_roll(), "rename")
        with patch("builtins.input", return_value="exit"):
            self.assertEqual(self.ui.ask_roll(), "exit")

    def test_display_turn(self):
        """Test display turns."""
        player = Player("John")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_turn(player.name)
            self.assertEqual(fake_out.getvalue().strip(), "John's turn!")

    def test_display_turn_end(self):
        """Test display turn end."""
        player = Player("John")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_turn_end(player.name)
            self.assertEqual(fake_out.getvalue().strip(),
                             "John's turn is over.")

    def test_display_game_over(self):
        """Test display game over."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_game_over()
            self.assertEqual(fake_out.getvalue().strip(), "Game over!")

    def test_display_high_scores(self):
        """Test display high scores."""
        high_score = HighScore()
        high_score.is_high_score(5, "John")
        high_score.is_high_score(8, "Rob")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_high_scores(high_score.scores)
            self.assertEqual(fake_out.getvalue().strip(),
                             "High Scores:\nJohn: 5\nRob: 8")

    def test_display_rules(self):
        """Test display rules."""
        # pylint: disable-msg=C0301
        expected_output = "Rules:\n- Each turn, a player repeatedly rolls a die until either a 1 is rolled or the player decides to hold.\n- If the player rolls a 1, they score nothing and their turn ends.\n- If the player rolls any other number, it is added to their turn total and the player's turn continues.\n- If the player chooses to hold, their turn total is added to their score, and it becomes the next player's turn.\n- The first player to score 100 or more points wins."  # noqa
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_rules()
            self.assertEqual(fake_out.getvalue().strip(), expected_output)

    def test_ask_player_name(self):
        """Test ask player name."""
        with patch("builtins.input", return_value="John"):
            self.assertEqual(self.ui.ask_player_name(1), "John")

    def test_display_menu(self):
        """Test display menu options."""
        with patch("builtins.input", return_value="2"):
            self.assertEqual(self.ui.display_menu(), "2")

    def test_ask_player_amount(self):
        """Test ask player amount."""
        with patch("builtins.input", return_value="1"):
            self.assertEqual(self.ui.ask_roll(), "1")
        with patch("builtins.input", return_value="2"):
            self.assertEqual(self.ui.ask_roll(), "2")

    def test_display_turn_score(self):
        """Test display turn score."""
        with patch("sys.stdout", new=StringIO()) as fake_out:
            self.ui.display_turn_score(3)
            self.assertEqual(fake_out.getvalue().strip(),
                             "Total points this turn: 3")


if __name__ == "__main__":
    unittest.main()
