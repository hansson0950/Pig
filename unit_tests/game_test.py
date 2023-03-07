"""This class tests the Game class of the application."""
import unittest
from unittest.mock import patch

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from ui import UI # noqa
from game import Game # noqa
from player import Player # noqa
from computer import ComputerPlayer # noqa


class TestGame(unittest.TestCase):
    """This class tests the Game class of the application."""

    def setUp(self):
        """Set up method that creates player objects and game object \
            for testing."""
        self.player1 = Player("John")
        self.player2 = ComputerPlayer()
        self.game = Game()

    def test_is_game_over(self):
        """Test method that checks if the game is over or not."""
        self.assertFalse(self.game.is_game_over())
        self.player1.score = 100
        self.assertTrue(self.game.is_game_over())

    @patch.object(UI, "display_welcome")
    @patch.object(UI, "display_scores")
    @patch.object(UI, "display_game_over")
    def test_start(self, mock_display_game_over,
                   mock_display_scores, mock_display_welcome):
        """Test method that checks the start of the game by verifying the \
            display of welcome message, the scores, \
                and the game over message."""
        self.game.start()
        mock_display_welcome.assert_called_once()
        self.assertTrue(mock_display_scores.call_count > 0)
        mock_display_game_over.assert_called_once()

    @patch.object(Player, "roll_dice", return_value=1)
    @patch.object(UI, "display_turn")
    @patch.object(UI, "display_scores")
    @patch.object(UI, "display_roll")
    @patch.object(UI, "display_bust")
    def test_play_turn_bust(self, mock_display_bust,
                            mock_display_roll, mock_display_scores,
                            mock_display_turn, mock_roll_dice):
        """Test method that checks the play of turn when the player busts."""
        self.game.play_turn()
        mock_display_turn.assert_called_once_with(self.player1)
        mock_roll_dice.assert_called_once()
        mock_display_roll.assert_called_once_with(1)
        mock_display_bust.assert_called_once()
        mock_display_scores.assert_called_once_with(self.player1, self.player2)
        self.assertEqual(self.game.current_player, self.player2)

    @patch.object(Player, "roll_dice", return_value=2)
    @patch.object(UI, "ask_roll_again", return_value=False)
    @patch.object(UI, "display_turn_end")
    @patch.object(UI, "display_scores")
    @patch.object(UI, "display_roll")
    def test_play_turn_no_roll_again(self, mock_display_roll,
                                     mock_display_scores,
                                     mock_display_turn_end,
                                     mock_ask_roll_again,
                                     mock_roll_dice):
        """Test method that checks the play of turn when the player \
            doesn't roll again."""
        self.game.play_turn()
        mock_roll_dice.assert_called_once()
        mock_display_roll.assert_called_once_with(2)
        mock_ask_roll_again.assert_called_once()
        mock_display_scores.assert_called_once_with(self.player1, self.player2)
        mock_display_turn_end.assert_called_once_with(self.player1)
        self.assertEqual(self.game.current_player, self.player2)

    @patch.object(Player, "roll_dice", return_value=3)
    @patch.object(UI, "ask_roll_again", return_value=True)
    @patch.object(UI, "display_scores")
    @patch.object(UI, "display_roll")
    def test_play_turn_roll_again(self, mock_display_roll, mock_display_scores,
                                  mock_ask_roll_again, mock_roll_dice):
        """Test method that checks the play of turn when the player \
            chooses to roll again."""
        self.game.play_turn()
        mock_roll_dice.assert_called_once()
        mock_display_roll.assert_called_once_with(3)
        mock_ask_roll_again.assert_called_once()
        mock_display_scores.assert_called_once_with(self.player1, self.player2)


if __name__ == "__main__":
    unittest.main()
