"""This class tests the Game class of the application."""
import unittest
from unittest.mock import patch, MagicMock, call, Mock
from io import StringIO

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
        self.ui = UI()

    @patch.object(Game, "game_two_players", return_value=None)
    @patch.object(Game, "game_one_player", return_value=None)
    @patch.object(UI, "ask_player_amount", side_effect=["1", "2"])
    @patch.object(UI, "display_menu", side_effect=["2", "3", "1", "4"])
    def test_game_start(self, mock_menu_options, mock_player_amount, mock_game_one_player, mock_game_two_players):
        """."""
        with self.assertRaises(SystemExit):
            self.game.game_start()

    @patch.object(Game, "play_turn_computer", side_effect=[True, False])
    @patch.object(Game, "play_turn", side_effect=[True, False, False])
    @patch.object(UI, "ask_player_name", return_value="Sandra")
    def test_game_one_player(self, mock_player_name, mock_player_turn, mock_computer_turn):
        """."""
        self.game.game_one_player()
        self.game.game_one_player()

    @patch.object(Game, "play_turn", side_effect=[True, False, True])
    @patch.object(UI, "ask_player_name", return_value=["Sandra", "Felix"])
    def test_game_two_players(self, mock_player_name, mock_player_turn):
        """."""
        self.game.game_two_players()

    
    @patch("builtins.input", side_effect=["n", "y", "n", "exit", "rename", "Bob", "n", "y", "cheat", "n"])
    @patch.object(Player, "roll_dice", return_value=2)
    def test_play_turn(self, mock_dice_roll, mock_input):
        """."""
        # Don't roll again
        self.assertFalse(self.game.play_turn(self.player1, self.player2))

        # Roll once
        self.assertFalse(self.game.play_turn(self.player1, self.player2))

        # Exit game
        self.assertTrue(self.game.play_turn(self.player1, self.player2))

        # Rename to Bob
        self.assertFalse(self.game.play_turn(self.player1, self.player2))

        # Roll and bust
        mock_dice_roll.return_value = 1
        print(self.player1.roll_dice())
        self.assertFalse(self.game.play_turn(self.player1, self.player2))

        # Cheat and win
        self.assertTrue(self.game.play_turn(self.player1, self.player2))

        

    @patch.object(ComputerPlayer, "choose_move", side_effect=["hold", "roll", "hold", "roll"])
    @patch.object(Player, "roll_dice", return_value=100)
    def test_play_turn_computer(self, mock_dice_roll, mock_computer_moves):
        """."""
        self.assertFalse(self.game.play_turn_computer(self.player2, self.player1))

        self.assertTrue(self.game.play_turn_computer(self.player2, self.player1))

        mock_dice_roll.return_value = 1
        self.assertFalse(self.game.play_turn_computer(self.player2, self.player1))

    def test_rename_player(self):
        """."""
        with patch("builtins.input", return_value="Alex"):
            self.game.rename_player(self.player1)
            self.assertEqual(self.player1.name, "Alex")


if __name__ == "__main__":
    unittest.main()
