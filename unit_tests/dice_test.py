"""A class to test the Dice class."""

import unittest
from unittest.mock import patch

import sys
sys.path.append("./application")

# pylint: disable=wrong-import-position
from dice import Dice # noqa


class TestDice(unittest.TestCase):
    """A class to test the Dice class."""

    def setUp(self):
        """Create a Dice instance with 6 sides before each test."""
        self.dice = Dice()

    def test_roll(self):
        """Test that roll() returns values within the range of 1 and the \
            number of sides on the dice, and that the randint function is \
                called with the correct arguments."""
        with patch('random.randint') as mock_randint:
            mock_randint.return_value = 4
            result = self.dice.roll()
            mock_randint.assert_called_once_with(1, 6)
            self.assertEqual(result, 4)

            mock_randint.reset_mock()

            mock_randint.return_value = 1
            result = self.dice.roll()
            mock_randint.assert_called_once_with(1, 6)
            self.assertEqual(result, 1)

            mock_randint.reset_mock()

            mock_randint.return_value = 6
            result = self.dice.roll()
            mock_randint.assert_called_once_with(1, 6)
            self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
