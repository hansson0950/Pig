"""Game class."""
import sys
import time
from ui import UI
from computer import ComputerPlayer
from player import Player
from high_score import HighScore


class Game:
    """Game class."""

    def __init__(self):
        """."""
        self.computer = ComputerPlayer()
        self.ui = UI()  # pylint: disable-msg=C0103
        self.high_score = HighScore()

    def game_start(self):
        """."""
        self.high_score.load_scores("high_scores.txt")
        self.ui.display_welcome()
        while True:
            option = self.ui.display_menu()
            if option == "1":
                players = self.ui.ask_player_amount()
                if players == "1":
                    self.game_one_player()
                elif players == "2":
                    self.game_two_players()
                else:
                    print("Invalid input")

            elif option == "2":
                self.ui.display_rules()

            elif option == "3":
                scores = self.high_score.get_high_scores()
                self.ui.display_high_scores(scores)

            elif option == "4":
                self.high_score.save_scores("high_scores.txt")
                sys.exit()

            else:
                print("Invalid input")

    def game_one_player(self):
        """."""
        name = self.ui.ask_player_name(1)
        player1 = Player(name)
        player2 = self.computer
        while True:
            if not self.play_turn(player1, player2):
                break
            # pylint: disable-msg=W1114
            if not self.play_turn_computer(player2, player1):
                break

    def game_two_players(self):
        """."""
        names = self.ui.ask_player_name(2)
        player1 = Player(names[0])
        player2 = Player(names[1])
        while True:
            if not self.play_turn(player1, player2):
                break
            # pylint: disable-msg=W1114
            if not self.play_turn(player2, player1):
                break

    def play_turn(self, player1, player2):
        """."""
        while True:
            player1.total_turns += 1
            self.ui.display_scores(player1, player2)
            self.ui.display_turn(player1.name)
            roll = player1.roll_dice()
            if roll == 1:
                self.ui.display_bust()
                player1.reset_turn_score()
                player1.end_turn()
                time.sleep(3)
                return True

            player1.add_to_turn(roll)
            self.ui.display_turn_score(player1.turn_score)

            option = ""
            while option not in ("n", "y", "cheat"):
                option = self.ui.ask_roll_again()

            if option == "n":
                if player1.add_to_score(player1.turn_score) >= 100:
                    self.ui.display_scores(player1, player2)
                    self.ui.display_game_over()
                    self.high_score.is_high_score(
                        player1.total_turns, player1.name)
                    self.high_score.save_scores("high_scores.txt")
                    return False
                player1.reset_turn_score()
                player1.end_turn()
                time.sleep(3)
                return True

            if option == "y":
                continue

            if option == "cheat":
                player1.turn_score = 100

            else:
                print("Invalid input\n")

    def play_turn_computer(self, player1, player2):
        """."""
        while True:
            player1.total_turns += 1
            time.sleep(3)
            self.ui.display_scores(player1, player2)
            self.ui.display_turn(player1.name)
            roll = player1.roll_dice()
            if roll == 1:
                self.ui.display_bust()
                player1.reset_turn_score()
                player1.end_turn()
                time.sleep(3)
                return True

            player1.add_to_turn(roll)
            self.ui.display_turn_score(player1.turn_score)

            if self.computer.choose_move() == "hold":
                if player1.add_to_score(player1.turn_score) >= 100:
                    self.ui.display_scores(player1, player2)
                    self.ui.display_game_over()
                    return False
                player1.reset_turn_score()
                player1.end_turn()
                time.sleep(3)
                return True


if __name__ == "__main__":
    game = Game()
    game.game_start()
