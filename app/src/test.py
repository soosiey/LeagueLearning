import json
import os
import helpers.summonerClass as player
import numpy as np

currPath = os.path.dirname(os.path.abspath(__file__))
currPath += '/outputs/weights.json'

weights = None
with open(currPath) as f:
    weights = json.load(f)

for i in weights:
    weights[i] = np.array(weights[i])
summoner = player.summoner("")
currPath = os.path.dirname(os.path.abspath(__file__))
currPath += '/helpers/summoners/Hamper.json'
summoner.load(currPath)

ninputs = summoner.dataset['gameInputs']

nlabels = summoner.dataset['gameOutputs']
inputs = []
labels = []
for i in range(len(ninputs)):
    if(ninputs[i][14] != -1):
        inputs.append(ninputs[i])
        labels.append(nlabels[i])

inputs = np.array(inputs)
labels = np.array(labels)
def ReLU(x):
    for i in range(len(x)):
        if(x[i] < 0):
            x[i] = 0
    return x

def sigmoid(x):
    return 1/(1 + np.e**(-1*x))
corr = 0
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
    if(y == labels[i]):
        corr += 1

print('Correct:', corr)
print('Accuracy:', corr/len(inputs))
