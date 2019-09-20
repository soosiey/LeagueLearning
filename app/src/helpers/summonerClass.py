from . import infoRequests as infoRequests
import time
import sys
import json
import tqdm
import numpy

DUO_SUPPORT = 5
DUO_CARRY = 4
DUO = 4.5
TOP = 3
MID = 2
JUNGLE = 1
OTHER = 0

class summoner():

    def __init__(self,name):
        self.dataset = {}
        self.dataset['name'] = name
        self.dataset['games'] = []
        self.dataset['gameInputs'] = []
        self.dataset['gameOutputs'] = []

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

    def processMatches(self):
        wins = 0
        for match in tqdm.tqdm(range(len(self.dataset['matchList']))):
            if(match % 10 == 0):
                time.sleep(1)
            if(match % 90 == 0 and match != 0):
                time.sleep(120)
            success, info = infoRequests.processMatch(self.dataset['matchList'][match]['gameId'])
            if(not success):
                print(info)
                return -1
            self.dataset['games'].append(info)
            plid = -1
            for p in info['participantIdentities']:
                if(p['player']['summonerName'] ==  self.dataset['name']):
                    plid = p['participantId']
                    break
            for p in info['participants']:
                if(not p['participantId'] == plid):
                    continue
                else:
                    pstats = p['stats']
                    if(pstats['win']):
                        self.dataset['gameOutputs'].append(0)
                        wins += 1
                    else:
                        self.dataset['gameOutputs'].append(1)
        self.dataset['wins'] = wins

    def printToFile(self,f):
        with open(f,'w') as outfile:
            json.dump(self.dataset,outfile)
