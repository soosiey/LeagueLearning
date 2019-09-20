import argparse
from . import infoRequests as infoRequests
import time
import sys
from . import summonerClass as summon
import os

def collect():
    parser = argparse.ArgumentParser(description = 'Get LoL user information')
    parser.add_argument('username', metavar='uname', type=str, help='username of the user')
    args = parser.parse_args()

    summoner = summon.summoner(args.username)
    summoner.getAccountID()
    summoner.getFullMatches()
    summoner.processMatches()
    curr_path = os.path.dirname(__file__)
    curr_path += '/summoners/Hamper.json'
    summoner.printToFile(curr_path)

