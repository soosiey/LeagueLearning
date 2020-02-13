import json

d = None

with open('champions.json') as f:
    d = json.load(f)

for a in d:
    d[a] = 0.0

with open('champions.json', 'w') as f:
    json.dump(d,f)
