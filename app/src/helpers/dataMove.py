import argparse
from . import infoRequests as infoRequests
import time
import sys
from . import summonerClass as summon
import os

def move():
    parser = argparse.ArgumentParser(description = 'Get LoL user information')
    parser.add_argument('filename', metavar='f', type=str, help='name of the json file')
    args = parser.parse_args()

    summoner = summon.summoner("")
    curr_path = os.path.dirname(__file__)
    curr_path += '/summoners/' + args.filename
    summoner.load(curr_path)
    summoner.move()
    summoner.printToFile(curr_path)
