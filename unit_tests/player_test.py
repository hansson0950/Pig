"""A class that tests the methods of the Player class."""
import unittest
from unittest.mock import Mock

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from player import Player # noqa


class TestPlayer(unittest.TestCase):
    """A class that tests the methods of the Player class."""

    def setUp(self):
        """Set up a Player instance for testing."""
        self.player = Player("Alice")

    def test_roll_dice(self):
        """Test the roll_dice method of Player class."""
        with unittest.mock.patch.object(
                self.player.dice, 'roll', return_value=3):
            self.assertEqual(self.player.roll_dice(), 3)

    def test_add_to_score(self):
        """Test the add_to_score method of Player class."""
        self.player.ui = Mock()
        self.player.add_to_score(10)
        self.player.ui.display_scores.assert_called_once_with(self.player)

    def test_end_turn(self):
        """Test the end_turn method of Player class."""
        self.player.ui = Mock()
        self.player.end_turn()
        self.player.ui.display_turn_end.assert_called_once_with(self.player)


if __name__ == '__main__':
    unittest.main()
