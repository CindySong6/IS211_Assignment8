from abc import ABC, abstractmethod
from player_factory import PlayerFactory
from dice import Dice

# set up threading
import threading
import time

class IGame(ABC):
    @abstractmethod
    def runGame(self):
        """run the pig game"""                 

class Game(IGame):
    def __init__(self, player1, player2):
        player1 = PlayerFactory.build_player(player1, 'Player 1')
        player2 = PlayerFactory.build_player(player2, 'Player 2')
        self.player1 = player1
        self.player2 = player2

        self.game_over = False
        self.die1 = Dice()

    # compare score
    def compareScores(self):
        if self.player1.check_total_score() > self.player2.check_total_score():
            return "Player 1 is the winner with {} points!".format(self.player1.check_total_score())
        elif self.player2.check_total_score() > self.player1.check_total_score():
            return "Player 2 is the winner with {} points!".format(self.player2.check_total_score())
        else:
            return "Tie!"
        
    # # taking turns until the game is done
    def runGame(self):
        
        while not self.game_over:
            for current_player in [self.player1, self.player2]:
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



class TimedGameProxy(IGame):
    
    def __init__(self, player1, player2, timed):
        self.game = Game(player1, player2)
        self.timed = timed
    
    def oneMinuteTime(self):
        print("Count one minute")
        time.sleep(10)
        self.game.game_over = True
        result = self.game.compareScores()
        print("""
        Times up. 
        {}
        """.format(result))

    def runGame(self):
        """
        has the timed option of the game
        """
        if self.timed:
            print("It's timed")
            one_minute_timer= threading.Thread(target=self.oneMinuteTime, args=())
            one_minute_timer.start()
            self.game.runGame()
        else:
            self.game.runGame()
        