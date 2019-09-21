import numpy as np
import torch
import torch.nn as nn
import helpers.summonerClass as player
import os
import json
import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self,numInputs, hiddenLayers):
        super(Net,self).__init__()
        self.fc1 = nn.Linear(numInputs,hiddenLayers)
        self.act1 = nn.ReLU()
        self.d1 = nn.Dropout(p = .2)
        self.fc2 = nn.Linear(hiddenLayers, 100)
        self.act2 = nn.ReLU()
        self.fc3 = nn.Linear(100,1)

    def forward(self,x):
        f1 = self.fc1(x)
        a1 = self.act1(f1)
        d1 = self.d1(a1)
        f2 = self.fc2(d1)
        a2 = self.act2(f2)
        f3 = self.fc3(a2)
        return f3




summoner = player.summoner("")
curr_path = os.path.dirname(os.path.abspath(__file__))
curr_path += '/helpers/summoners/Hamper.json'
summoner.load(curr_path)

ninputs = summoner.dataset['gameInputs']




epochs = 5000
nlabels = summoner.dataset['gameOutputs']
inputs = []
labels = []
d = np.random.binomial(size=len(ninputs),n=1,p=.8)
for i in range(len(ninputs)):
    if(ninputs[i][14] != -1 and d[i] == 1):
        inputs.append(ninputs[i])
        labels.append(nlabels[i])


losses = []
hiddenLayers = 1000
inputSize = 15
model = Net(inputSize, hiddenLayers)
alpha = .01
criterion = nn.BCEWithLogitsLoss()
optim = torch.optim.SGD(model.parameters(), lr = alpha)
scheduler = torch.optim.lr_scheduler.StepLR(optim,step_size = 500,gamma = .1)
optim.zero_grad()
for epoch in range(epochs):

    inputs = torch.Tensor(inputs)
    labels = torch.Tensor(labels)
    forwardPass = model(inputs).squeeze()
    y = labels
    loss = criterion(forwardPass, y)

    loss.backward()
    print("Loss:", loss)
    losses.append(loss.data.item())
    optim.step()
    optim.zero_grad()
    scheduler.step()

weights = {}
weights['W'] = None
weights['b'] = None
weights['C'] = None
weights['d'] = None
weights['H'] = None
weights['e'] = None
count = 0
for f in model.parameters():
    x = f.data.tolist()
    if(count == 0):
        weights['W'] = x
    elif(count == 1):
        weights['b'] = x
    elif(count == 2):
        weights['C'] = x
    elif(count == 3):
        weights['d'] = x
    elif(count == 4):
        weights['H'] = x
    else:
        weights['e'] = x
    count += 1
curr_path = os.path.dirname(os.path.abspath(__file__))
curr_path += '/outputs/weights.json'
with open(curr_path,'w') as f:
    json.dump(weights,f)
plt.plot(losses[5:])
plt.show()
