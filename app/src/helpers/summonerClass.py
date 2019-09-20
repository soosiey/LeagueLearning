from . import infoRequests as infoRequests
import time
import sys
import json


class summoner():

    def __init__(self,name):
        self.dataset = {}
        self.dataset['name'] = name
        self.dataset['games'] = []

    def getAccountID(self):
        success, info = infoRequests.getSumInfo(self.dataset['name'])
        if(not success):
            print(info)
            return -1
        else:
            self.dataset['accountID'] = info['accountId']
            return 0

    def getMatchlist(self,index):
        success, info = infoRequests.getMatchlist(self.dataset['accountID'],index)
        if(not success):
            print(info)
            return -1
        else:
            if('matchList' not in self.dataset):
                self.dataset['matchList'] = info['matches']
            else:
                self.dataset['matchList'].extend(info['matches'])

    def getFullMatches(self):

        for i in range(5):
            current = i * 100
            self.getMatchlist(current)

    def processMatches():
        for match in range(len(self.dataset['matchList'])):
            if(match % 10 == 0):
                time.sleep(1)
            if(match % 90 == 0):
                time.sleep(120)
            success, info = infoRequests.processMatch(self.dataset['matchList'][match]['gameId'])
            if(not success):
                print(matchInfo)
                return -1
            plid = -1
            for p in info['participantIdentities']:
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

    def printToFile(self,f):
        with open(f,'w') as outfile:
            json.dump(self.dataset,outfile)
