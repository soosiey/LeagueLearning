import numpy as np
import torch
import torch.nn as nn
import helpers.summonerClass as player
import os
import json


class Net(nn.Module):
    def __init__(self,numInputs, hiddenLayers):
        super(Net,self).__init__()
        self.fc1 = nn.Linear(numInputs,hiddenLayers)
        self.act1 = nn.ReLU()
        self.fc2 = nn.Linear(hiddenLayers, 1)

    def forward(self,x):
        f1 = self.fc1(x)
        a1 = self.act1(f1)
        f2 = self.fc2(a1)
        return f2




summoner = player.summoner("")
curr_path = os.path.dirname(os.path.abspath(__file__))
curr_path += '/helpers/summoners/Hamper.json'
summoner.load(curr_path)

ninputs = summoner.dataset['gameInputs']




epochs = 2000
nlabels = summoner.dataset['gameOutputs']
inputs = []
labels = []
for i in range(len(ninputs)):
    if(ninputs[i][14] != -1):
        inputs.append(ninputs[i])
        labels.append(nlabels[i])

inputs = torch.Tensor(inputs)

print(inputs.size())
labels = torch.Tensor(labels)
hiddenLayers = 100
inputSize = 15
model = Net(inputSize, hiddenLayers)
alpha = .001
criterion = nn.BCEWithLogitsLoss()
optim = torch.optim.SGD(model.parameters(), lr = alpha)
optim.zero_grad()
for epoch in range(epochs):


    forwardPass = model(inputs).squeeze()
    y = labels
    loss = criterion(forwardPass, y)

    loss.backward()
    gn = 0
    for f in model.parameters():
        gn = gn + torch.norm(f.grad)
    print("Loss:", loss)
    optim.step()
    optim.zero_grad()

weights = {}
weights['W'] = None
weights['b'] = None
weights['C'] = None
weights['d'] = None
count = 0
for f in model.parameters():
    x = f.data.tolist()
    print(type(x))
    if(count == 0):
        weights['W'] = x
    elif(count == 1):
        weights['b'] = x
    elif(count == 2):
        weights['C'] = x
    else:
        weights['d'] = x
    count += 1
curr_path = os.path.dirname(os.path.abspath(__file__))
curr_path += '/outputs/weights.json'
with open(curr_path,'w') as f:
    json.dump(weights,f)
