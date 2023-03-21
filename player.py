class Player:
    player_type = 'human'

    def __init__(self, name):
        self.name = name
        self.total_score = 0
        self.turn_score = 0
        self.my_turn = True
        self.win = False

    def check_player_name(self):
        return self.name
    
    def check_turn(self):
        return self.my_turn
    
    def reset_turn_score(self):
        self.turn_score = 0
    
    def check_total_score(self):
        return self.total_score
    
    def check_winning_status(self):
        return self.win
    
    def start_turn(self):
        self.my_turn = True
        self.win = False

    def action(self, dice):
        player_action = input("type 'r' to roll, type 'h' to hold:")
        if player_action.lower() not in ('r', 'h'):
            print("Not an appropriate input.")
        else:
            player_action = player_action.lower()
            if player_action == 'r':
                dice.roll()
                self.roll(dice.die_result())
            else:
                self.hold()

    def roll(self, current_roll):
        if current_roll == 1:
            self.my_turn = False
            self.reset_turn_score()
            print("You rolled 1, your scores this turn don't count")
        else:
            self.turn_score += current_roll
            potential_score = self.total_score + self.turn_score
            print("You rolled {}, your current turn score is {}, your potential score is {}".format(current_roll, self.turn_score, potential_score))
            if potential_score >= 100:
                self.hold()
                print("{} you won with {} points".format(self.name, self.total_score))
                self.win = True
        

    def hold(self):
        self.total_score += self.turn_score
        self.my_turn = False
        self.turn_score = 0
