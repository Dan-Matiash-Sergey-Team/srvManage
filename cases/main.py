from requests import get
import json

dis = json.loads(open('dis.json', 'r').read())
res = {}
for i in dis:
    res[i] = []
    for j in range(0, 7):
        res[i].append([])
        for k in range(0, 12):
            res[i][j].append(0)
for i in get('http://195.133.147.101:3000/get_dtps_all').json():
    res[i['district']][i['year'] - 2015][i['month'] - 1] += i['death'] #1
open('res.json', 'w').write(json.dumps(res))