"""Game class."""
import sys
import time
from ui import UI
from computer import ComputerPlayer
from player import Player
from high_score import HighScore


class Game:
    """Represents the game of Pig.

    ### Description:
    The game can be played by one or two players.
    Uses the `UI`, `Player`, `ComputerPlayer`, and `HighScore` classes
    to interact with the user, handle player moves and score tracking,
    and display high scores.

    ### Attributes:
    - computer (ComputerPlayer): a computer player instance that plays
      against the user.
    - ui (UI): a user interface instance that handles input/output
      interactions with the user.
    - high_score (HighScore): a high score instance that keeps track of the
      top scores.

    ### Methods:
    - __init__(): Initializes a new instance of the `Game` class, and
      initializes its attributes.
    - game_start(): Starts the game, displays the welcome message and menu,
      and loops until the user quits or a player wins.
    - game_one_player(): Starts a game against the computer player, loops
      until a player wins, and handles each player's turns.
    - game_two_players(): Starts a game between two human players, loops until
      a player wins, and handles each player's turns.
    - play_turn(player1, player2): Handles the turn of a given player,
      displays the current scores, and loops until the player holds or busts.
    - play_turn_computer(player1, player2): Handles the turn of the computer
      player, displays the current scores, and loops until the player holds
      or busts.
    - rename_player(player): Prompts the user to rename themselves.
    """

    def __init__(self):
        """Initialize the game.

        ### Description:
        Initializes a new instance of the `Game` class,
        and initializes its attributes.

        ### Attributes:
        - computer (ComputerPlayer): a computer player instance that plays
          against the user.
        - ui (UI): a user interface instance that handles input/output
          interactions with the user.
        - high_score (HighScore): a high score instance that keeps track
          of the top scores.
        """
        self.computer = ComputerPlayer()
        self.ui = UI()  # pylint: disable-msg=C0103
        self.high_score = HighScore()

    def game_start(self):
        """Start the game.

        ### Description:
        Starts the game and displays the welcome message and menu,
        and loops until the user quits or a player wins.
        """
        self.high_score.create_file()
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
                    print("Invalid input\n")

            elif option == "2":
                self.ui.display_rules()

            elif option == "3":
                scores = self.high_score.get_high_scores()
                self.ui.display_high_scores(scores)

            elif option == "4":
                self.high_score.save_scores("high_scores.txt")
                sys.exit()

            else:
                print("Invalid input\n")

    def game_one_player(self):
        """Start a one-player game.

        ### Description:
        Starts a game against the computer player,
        loops until a player wins, and handles each player's turns.
        """
        name = self.ui.ask_player_name(1)
        player1 = Player(name)
        player2 = self.computer
        while True:
            self.ui.display_scores(player1, player2)
            self.ui.display_turn(player1.name)
            if self.play_turn(player1, player2):
                break
            # pylint: disable-msg=W1114
            self.ui.display_scores(player2, player1)
            self.ui.display_turn(player2.name)
            # pylint: disable-msg=W1114
            if self.play_turn_computer(player2, player1):
                break

    def game_two_players(self):
        """Start a two-player game.

        ### Description:
        This method is responsible for managing the two-player game logic.
        It prompts players to enter their names, displays scores, and turns,
        and calls the play_turn method to handle the gameplay.
        """
        names = self.ui.ask_player_name(2)
        player1 = Player(names[0])
        player2 = Player(names[1])

        while True:
            self.ui.display_scores(player1, player2)
            self.ui.display_turn(player1.name)
            if self.play_turn(player1, player2):
                break
            # pylint: disable-msg=W1114
            self.ui.display_scores(player2, player1)
            self.ui.display_turn(player2.name)
            # pylint: disable-msg=W1114
            if self.play_turn(player2, player1):
                break

    def play_turn(self, player1, player2):
        """Play turn.

        ### Description:
        This method plays one turn of the game for a given player.
        It prompts the player to choose whether to roll or hold,
        displays the turn score and updates the player's total score
        accordingly. It also handles player-specific options,
        such as renaming and cheating.

        ### Args:
        - player1 (Player): the player whose turn it is
        - player2 (Player): the other player in the game

        ### Returns:
        - bool: True if the game has ended, False otherwise
        """
        while True:
            option = self.ui.ask_roll_again()

            if option == "exit":
                return True

            if option == "rename":
                self.rename_player(player1)

            if option == "cheat":
                player1.turn_score = 100

            if option == "y":
                player1.total_turns += 1
                self.ui.display_scores(player1, player2)
                self.ui.display_turn(player1.name)
                roll = player1.roll_dice()

                if roll == 1:
                    self.ui.display_bust()
                    player1.reset_turn_score()
                    player1.end_turn()
                    time.sleep(3)
                    return False

                player1.add_to_turn(roll)
                self.ui.display_turn_score(player1.turn_score)

            if option == "n":
                if player1.add_to_score(player1.turn_score) >= 100:
                    self.ui.display_scores(player1, player2)
                    self.ui.display_game_over()
                    self.high_score.is_high_score(
                        player1.total_turns, player1.name)
                    self.high_score.save_scores("high_scores.txt")
                    return True
                player1.reset_turn_score()
                player1.end_turn()
                time.sleep(3)
                return False

    def play_turn_computer(self, player1, player2):
        """Play computer's turn.

        ### Description:
        This method plays one turn of the game for the computer player.
        It calls the choose_move method of the Computer class to determine
        whether to roll or hold. It then displays the turn score and
        updates the player's total score accordingly.

        ### Args:
        - player1 (Player): the computer player
        - player2 (Player): the human player

        ### Returns:
        - bool: True if the game has ended, False otherwise
        """
        while True:
            move = self.computer.choose_move()
            if move == "roll":
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
                    return False

                player1.add_to_turn(roll)
                self.ui.display_turn_score(player1.turn_score)

            if move == "hold":
                if player1.add_to_score(player1.turn_score) >= 100:
                    self.ui.display_scores(player1, player2)
                    self.ui.display_game_over()
                    self.high_score.is_high_score(
                        player1.total_turns, player1.name)
                    self.high_score.save_scores("high_scores.txt")
                    return True
                player1.reset_turn_score()
                player1.end_turn()
                time.sleep(3)
                return False

    def rename_player(self, player):
        """Rename a player.

        ### Description:
        This method allows the player to rename themselves.
        It prompts the player to enter a new name and updates
        the player's name.

        ### Args:
        - player (Player): the player to be renamed
        """
        new_name = input("Enter a new name: ")
        player.name = new_name


if __name__ == "__main__":
    game = Game()
    game.game_start()
