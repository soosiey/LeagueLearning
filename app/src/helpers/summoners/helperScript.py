import json


d = {}
d2 = None
with open('champions.json') as f:
    d2 = json.load(f)
for i in d2:
    d[d2[i]] = i

with open('champions.json','w') as f:
    json.dump(d,f)
