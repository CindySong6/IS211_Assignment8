from player_factory import PlayerFactory
from dice import Dice


class Game:

    def __init__(self):
        self.players = []
        self.game_over = False
        self.die1 = Dice()

# def game(player1, player2):
#     players = []
#     game_over = False
#     die1 = Dice()

    # explaining game rule
    def rule(self):
        print(
    """
    Welcome to Pig!
    If you reach the score of 100 you win the game!
    You can choose to hold or roll the dice.
    If your roll is 1, your turn doesn't count.
    Good luck!
    """
        )

    # set up players
    def setupPlayers(self, player1, player2):
        self.players.append(PlayerFactory.build_player(player1, 'Player 1'))
        self.players.append(PlayerFactory.build_player(player2, 'Player 2'))

    # # taking turns until the game is done
    def runGame(self):
        while not self.game_over:
            for current_player in self.players:
                player_name = current_player.check_player_name()
                print("==================\n{} it's your turn!".format(player_name))
                print("Your total score:{}".format(current_player.check_total_score()))
                current_player.start_turn()

        #         # 1. prompt the user to roll or hold
        #         # 2. if the prompt is invalid, just keep prompting
        #         # 3. if the input is r, roll the dice; if h, hold
        #         # 4. if the player is winning (100+ total score), end the game
                while current_player.check_turn() and current_player.check_winning_status() == False:
                    current_player.action(self.die1)
                    if current_player.check_winning_status():
                        self.game_over = True
                        return