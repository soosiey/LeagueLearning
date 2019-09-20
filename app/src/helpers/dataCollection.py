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
    curr_path = os.path.dirname(__file__)
    curr_path += '/summoners/Hamper.json'
    summoner.printToFile(curr_path)
"""
success, info = infoRequests.getSumInfo(args.username)

if(not success):
    print(info)
    sys.exit(0)

accountID = info['accountId']
getMatchesSuccess,matchesinfo = infoRequests.getMatchlist(accountID)
if(not getMatchesSuccess):
    print(matchesinfo)
    sys.exit(0)

w,m = breakMatches(matchesinfo)
print("Recent W/L Ratio in", m, "games:",float(w)/float(m))
def breakMatches(matchesInfo,player=args.username):
    matches = matchesInfo['totalGames']
    matchList = matchesInfo['matches']
    wins = 0
    for match in range(len(matchList)):
        if(match % 10 == 0):
            time.sleep(1)
        if(match % 90 == 0):
            time.sleep(120)
        if(match == 100):
            getMatches,matchesinfo = infoRequests.getMatchlist(accountID)
        matchSuccess,matchInfo = infoRequests.processMatch(matchList[match]['gameId'])
        if(not matchSuccess):
            print(matchInfo)
            sys.exit(0)
        plid = -1
        for p in matchInfo['participantIdentities']:
            if(p['player']['summonerName'] ==  player):
                plid = p['participantId']
                break
        for p in matchInfo['participants']:
            if(not p['participantId'] == plid):
                continue
            else:
                pstats = p['stats']
                if(pstats['win']):
                    wins += 1
    return wins,matches


"""

