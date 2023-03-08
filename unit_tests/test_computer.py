"""Test class for the ComputerPlayer class."""
import unittest

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from computer import ComputerPlayer # noqa


class TestComputerPlayer(unittest.TestCase):
    """Test class for the ComputerPlayer class."""

    def setUp(self):
        """Set up a ComputerPlayer object for testing."""
        self.computer_player = ComputerPlayer()

    def test_choose_move_roll(self):
        """Return "roll" when the turn score is less than 20."""
        self.computer_player.turn_score = 10
        self.computer_player.score = 0
        self.assertEqual(self.computer_player.choose_move(), "roll")

    def test_choose_move_hold(self):
        """Return "hold" when the turn score is more than 20."""
        self.computer_player.turn_score = 20
        self.computer_player.score = 70
        self.assertEqual(self.computer_player.choose_move(), "hold")

    def test_choose_move_win(self):
        """Return "hold" when the total score is more than 100."""
        self.computer_player.turn_score = 10
        self.computer_player.score = 90
        self.assertEqual(self.computer_player.choose_move(), "hold")


if __name__ == "__main__":
    unittest.main()
