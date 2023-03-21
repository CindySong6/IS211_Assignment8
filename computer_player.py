from player import Player

class ComputerPlayer(Player):
    player_type = 'computer'

    def __init__(self, name):
        super().__init__(name)
    
    def action(self, dice):
        while self.turn_score < 25 and self.my_turn:
            dice.roll()
            self.roll(dice.die_result())
        self.hold()
