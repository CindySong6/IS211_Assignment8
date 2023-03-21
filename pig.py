import argparse
from game import Game

def main(player1, player2):
    pig = Game()
    pig.setupPlayers(player1,player2)
    pig.runGame()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", help="human or computer player",type=str, required=True)
    parser.add_argument("--player2", help="human or computer player",type=str, required=True)
    args = parser.parse_args()
    main(args.player1,args.player2)
