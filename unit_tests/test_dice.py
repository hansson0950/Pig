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
        """Create a Dice to be used for the tests."""
        self.dice = Dice()

    def test_roll(self):
        """Test that roll() returns a value from 1-6."""
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
