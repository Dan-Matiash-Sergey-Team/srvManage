from pymongo import MongoClient

username = 'universai'
password = 'cumzone'
cluster = '127.0.0.1:1488'
client = MongoClient(f"mongodb://{username}:{password}@{cluster}")
db1 = client.dtp.dtp
db2 = client.dtpsFull

def address(data):
    add = ""
    s = str(data['data']['infoDtp']['street'])
    h = str(data['data']['infoDtp']['house']).replace(' ', '/')
    d = str(data['data']['infoDtp']['dor'])
    km = str(data['data']['infoDtp']['km'])
    m = str(data['data']['infoDtp']['m'])
    if 'МКАД' in d:
        s = 'МКАД'
    
    if s != '' and h != '':
        add = s + ", дом " + h
    elif km != '' and d != '':
        add = d + ', ' + km + 'км' + (', ' + m + 'м' if m != '' and int(m) != 0 else '')
    elif s != '':
        add = s
    elif d != '':
        add = d
    else:
        add = 'Точный адрес ДТП не указан'
    return [s, add]

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
            res = address(i)
            i['data']['infoDtp']['street'] = res[0]
            i['data']['infoDtp']['address'] = res[1]
            count += 1
            col.insert_one(i)
