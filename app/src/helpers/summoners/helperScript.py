import json


d = {}
d2 = None
with open('champions.json') as f:
    d2 = json.load(f)
d2 = d2['data']
for i in d2:
    d[i] = d2[i]['key']

with open('champions.json','w') as f:
    json.dump(d,f)
