import argparse
from summoner import summoner
#import os


def collect():
    parser = argparse.ArgumentParser(description = 'Get LoL user information')
    parser.add_argument('username', metavar='uname', type=str, help='username of the user')
    args = parser.parse_args()

    s = summoner.summoner(args.username)
    s.getMatches()
    print(s.data['matchlist'])
    #summoner.getFullMatches()
    #summoner.processMatches()
    #curr_path = os.path.dirname(__file__)
    #curr_path += '/summoners/Hamper.json'
    #summoner.printToFile(curr_path)

if(__name__ == '__main__'):
    collect()
