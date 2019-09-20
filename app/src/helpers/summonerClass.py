from . import infoRequests as infoRequests
import time
import sys
import json
import tqdm
import numpy as np
import os

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

    def load(self,f):
        with open(f) as infile:
            self.dataset = json.load(infile)

    def move(self):
        championList = None
        curr_path = os.path.dirname(__file__)
        curr_path += '/summoners/champions.json'
        with open(curr_path) as f:
            championList = json.load(f)

        for i in range(len(self.dataset['matchList'])):
            currentInput = [0] * 15
            match = self.dataset['matchList'][i]
            matchDetails = self.dataset['games'][i]

            championID = match['champion']
            currentInput[0] = championID


            pid = None
            team = None
            for j in matchDetails['participantIdentities']:
                if(j['player']['summonerName'] == self.dataset['name']):
                    pid = j['participantId']
                    break
            participantList = matchDetails['participants']
            team1 = []
            team2 = []
            currIndex = 0
            currTeam = None
            otherTeam = None
            for j in participantList:
                if(j['teamId'] == 100):
                    team1.append(j['championId'])
                    if(j['participantId'] == pid):
                        team = 100
                        currIndex = len(team1) - 1
                else:
                    team2.append(j['championId'])
                    if(j['participantId'] == pid):
                        team = 200
                        currIndex = len(team2) - 1
            if(team == 100):
                currTeam = team1
                otherTeam = team2
            else:
                currTeam = team2
                otherTeam = team1
            if(len(currTeam) != 5):
                currentInput[14] = -1
                continue
            print(currTeam)
            print(otherTeam)
            for j in range(2,7):
                if(j - 2 != currIndex):
                    currentInput[j] = currTeam[j - 2]
            for j in range(7,12):
                currentInput[j] = otherTeam[j - 7]
            if(match['role'] == 'DUO_SUPPORT'):
                currentInput[1] = DUO_SUPPORT
            elif(match['role'] == 'DUO_CARRY'):
                currentInput[1] = DUO_CARRY
            elif(match['role'] == 'DUO'):
                currentInput[1] = DUO
            elif(match['lane'] == 'TOP'):
                currentInput[1] = TOP
            elif(match['lane'] == 'MID'):
                currentInput[1] = MID
            elif(match['lane'] == 'JUNGLE'):
                currentInput[1] = JUNGLE
            else:
                currentInput[1] = OTHER
            teams = matchDetails['teams']
            for j in teams:
                if(j['teamId'] == team and j['firstDragon']):
                    currentInput[12] = 1
                elif(j['teamId'] == team and not j['firstDragon']):
                    currentInput[12] = -1
                if(j['teamId'] == team and j['firstBaron']):
                    currentInput[13] = 1
                elif(j['teamId'] == team and not j['firstBaron']):
                    currentInput[13] = -1
            self.dataset['gameInputs'].append(currentInput)
