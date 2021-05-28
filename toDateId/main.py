from pymongo import MongoClient

username = 'universai'
password = 'cumzone'
cluster = '127.0.0.1:1488'
client = MongoClient(f"mongodb://{username}:{password}@{cluster}")
db1 = client.dtp.dtp
db2 = client.dtpsFull
for y in range(2015, 2022):
    for m in range(1, 13):
        month = f"0{m}" if m < 10 else m
        print(f"{y}:{month}")
        col = db2[f"{y}{month}"]
        count = 0
        for i in db1.find({
            "year":y,
            "month":m
        }):
            i['id'] = f"{y}{month}{count}"
            count += 1
            col.insert_one(i)
