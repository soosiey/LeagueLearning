import json
import os
import helpers.summonerClass as player
import numpy as np

DUO_SUPPORT = 5
DUO_CARRY = 4
DUO = 4.5
TOP = 3
MID = 2
JUNGLE = 1
OTHER = 0
currPath = os.path.dirname(os.path.abspath(__file__))
currPath += '/outputs/weights.json'

weights = None
with open(currPath) as f:
    weights = json.load(f)

for i in weights:
    weights[i] = np.array(weights[i])

currPath = os.path.dirname(os.path.abspath(__file__))
currPath += '/helpers/summoners/champions.json'
champions = None
with open(currPath) as f:
    champions = json.load(f)


summoner = player.summoner("")
currPath = os.path.dirname(os.path.abspath(__file__))
currPath += '/helpers/summoners/Hamper.json'
summoner.load(currPath)

input00 = np.zeros(15)
input01 = np.zeros(15)
input10 = np.zeros(15)
input11 = np.zeros(15)

myChampion = "Leona"
myRole = DUO_SUPPORT
myTeam = ['Aatrox', 'Akali', 'Kayle','Ashe']
otherTeam = ['Thresh', 'Caitlyn', 'Nasus', 'Leblanc','Zac']

input00[0] = champions[myChampion]
input01[0] = champions[myChampion]
input10[0] = champions[myChampion]
input11[0] = champions[myChampion]
input00[1] = myRole
input01[1] = myRole
input10[1] = myRole
input11[1] = myRole

for j in range(len(myTeam)):
    input00[j + 2] = champions[myTeam[j]]
    input01[j + 2] = champions[myTeam[j]]
    input10[j + 2] = champions[myTeam[j]]
    input11[j + 2] = champions[myTeam[j]]

for j in range(len(otherTeam)):
    input00[j + 7] = champions[otherTeam[j]]
    input01[j + 7] = champions[otherTeam[j]]
    input10[j + 7] = champions[otherTeam[j]]
    input11[j + 7] = champions[otherTeam[j]]

input00[12] = -1
input01[12] = 1
input10[12] = -1
input11[12] = 1
input00[13] = -1
input01[13] = -1
input10[13] = 1
input11[13] = 1
inputs = [input00,input01,input10,input11]
def ReLU(x):
    for i in range(len(x)):
        if(x[i] < 0):
            x[i] = 0
    return x

def sigmoid(x):
    return 1/(1 + np.e**(-1*x))

chances = []
for i in range(len(inputs)):
    inp = inputs[i]
    out = np.matmul(weights['W'], inp)
    out += weights['b']
    out = ReLU(out)
    out = np.matmul(weights['C'],out)
    out += weights['d']
    out = ReLU(out)
    out = np.matmul(weights['H'],out)
    out += weights['e']
    out = sigmoid(out)
    y = 0
    if(out > .5):
        y = 1
    chances.append(out)

print(chances)

