from player import Player
from computer_player import ComputerPlayer

class PlayerFactory:
    @staticmethod
    def build_player(player_type, name):
        if player_type == "human":
            return Player(name)
        if player_type == "computer":
            return ComputerPlayer(name)