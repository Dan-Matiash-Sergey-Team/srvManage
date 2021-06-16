import json
import pymongo
import shapely.geometry as shpl
import shapely.wkt as wkt
import requests

username = 'universai'
password = 'cumzone'
cluster = '127.0.0.1:1488'
client = pymongo.MongoClient(f"mongodb://{username}:{password}@{cluster}")
db = client.dtp.dtp
coords = json.loads(open('discoords.json', 'r').read())['district_coords']
dist = {}
for i in coords:
    dis = coords[i]
    for j in range(0, len(dis)):
        try:
            dist[i + "%" + str(j)] = shpl.Polygon(dis[j])
        except:
            dist[i + "%" + str(j)] = shpl.Polygon(dis[j][0])

def findDist(dot):
    global dist
    for j in dist:
        try:
            coord = [ float( dot['COORD_W'] ), float( dot['COORD_L'] ) ]
        except:
            continue
        if dist[j].contains(shpl.Point(coord)):
            return(j.split('%')[0])
    return 'NULL'


for f in ["45 г. Москва 1-12.2015.json", "45 г. Москва 1-12.2016.json", "45 г. Москва 1-12.2017.json","45 г. Москва 1-12.2018.json", "45 г. Москва 1-12.2019.json", "45 г. Москва 1-12.2020.json", "45 г. Москва 1-4.2021.json"]:
   with open(f, 'r') as file:
       data = json.loads(file.read())
       print(type(data['data']))
       for card in json.loads(data['data'])['cards']:
                    dat = {}
                    dat['id'] = card['KartId']
                    dat['data'] = card
                    dt = dat['data']['date']
                    dt = dt.split('.')
                    dat['year'] = int(dt[2])
                    dat['month'] = int(dt[1])
                    dat['data']['District'] = findDist(card['infoDtp'])
                    if dat['data']['District'] == 'NULL':
                        continue
                    dat['district_name'] = dat['data']['District']
                    db.insert_one(dat)
