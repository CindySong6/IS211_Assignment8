import argparse
from proxy import TimedGameProxy

def main(player1, player2, timed=False):
    pig = TimedGameProxy(player1, player2, timed)
    pig.runGame()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--player1", help="input to choose human or computer player",type=str, required=True)
    parser.add_argument("--player2", help="input to choose human or computer player",type=str, required=True)
    parser.add_argument("--timed", help="The game will be timed to finish in one minute", action="store_true")
    args = parser.parse_args()
    print(args.timed)
    main(args.player1,args.player2, args.timed)
