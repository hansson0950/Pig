"""Test class for the ComputerPlayer class."""
import unittest
from unittest.mock import patch

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from computer import ComputerPlayer # noqa


class TestComputerPlayer(unittest.TestCase):
    """Test class for the ComputerPlayer class."""

    def setUp(self):
        """Set up a ComputerPlayer object for testing."""
        self.computer_player = ComputerPlayer()

    def test_roll_again_true(self):
        """Test the roll_again method when the turn score is less than 20 and \
            the score is less than 100."""
        self.computer_player.turn_score = 10
        self.computer_player.score = 50
        self.assertTrue(self.computer_player.roll_again())

    def test_roll_again_false(self):
        """Test the roll_again method when the turn score is greater than or \
            equal to 20 and the score is less than 100."""
        self.computer_player.turn_score = 20
        self.computer_player.score = 50
        self.assertFalse(self.computer_player.roll_again())

    def test_choose_move_roll(self):
        """Test the choose_move method when the random number generator \
            returns 4."""
        with patch('Intelligence.random.randint', return_value=4):
            self.computer_player.turn_score = 10
            self.computer_player.score = 50
            self.assertEqual(self.computer_player.choose_move(), "roll")

    def test_choose_move_hold(self):
        """Test the choose_move method when the random number generator \
            returns 4."""
        with patch('Intelligence.random.randint', return_value=4):
            self.computer_player.turn_score = 20
            self.computer_player.score = 50
            self.assertEqual(self.computer_player.choose_move(), "hold")

    def test_roll_1(self):
        """Test the roll method when the random number generator returns 1."""
        with patch('Intelligence.random.randint', return_value=1), \
             patch('builtins.print') as mock_print:
            self.computer_player.roll()
            mock_print.assert_called_with(f"{self.computer_player.name} \
                                          rolled a 1 and scored 0 this turn.")

    def test_roll_not_1(self):
        """Test the roll method when the random number generator returns a \
            number other than 1."""
        with patch('Intelligence.random.randint', return_value=4), \
             patch('builtins.print') as mock_print:
            self.computer_player.roll()
            mock_print.assert_called_with(f"{self.computer_player.name} scored \
                                          {self.computer_player.turn_score} \
                                          this turn.")

    def test_reset_turn_score(self):
        """Test that the score is reset to 0 when resetting turn."""
        self.computer_player.turn_score = 10
        self.computer_player.reset()
        self.assertEqual(self.computer_player.turn_score, 0)


if __name__ == '__main__':
    unittest.main()
