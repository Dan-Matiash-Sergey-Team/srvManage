import json
import pymongo


username = 'universai'
password = 'cumzone'
cluster = '127.0.0.1:1488'
client = pymongo.MongoClient(f"mongodb://{username}:{password}@{cluster}")
db = client.dtp.dtp

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
                    dat['district_name'] = dat['data']['District']
                    db.insert_one(dat)
