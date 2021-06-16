from pymongo import MongoClient
import requests
import json

# username = 'universai'
# password = 'cumzone'
# cluster = '127.0.0.1:1488'
# client = MongoClient(f"mongodb://{username}:{password}@{cluster}")
# db = client.dtp.dtp

#Общий вид
# com = json.loads(open('com.json', 'r').read())['street']
# for i in com:
#     db.update_many({"data.infoDtp.street" : i}, 
#     {"$set" : { "data.infoDtp.street" : com[i] }})

#Мкад
# MKAD = ["км МКАД 1-й",
#     "км МКАД 10-й",
#     "км МКАД 102-й",
#     "км МКАД 103-й",
#     "км МКАД 104-й",
#     "км МКАД 105-й",
#     "км МКАД 106-й",
#     "км МКАД 109-й",
#     "км МКАД 12-й",
#     "км МКАД 13-й",
#     "км МКАД 14-й",
#     "км МКАД 15-й",
#     "км МКАД 16-й",
#     "км МКАД 17-й",
#     "км МКАД 18-й",
#     "км МКАД 19-й",
#     "км МКАД 2-й",
#     "км МКАД 21-й",
#     "км МКАД 22-й",
#     "км МКАД 23-й",
#     "км МКАД 24-й",
#     "км МКАД 25-й",
#     "км МКАД 26-й",
#     "км МКАД 28-й",
#     "км МКАД 29-й",
#     "км МКАД 3-й",
#     "км МКАД 30-й",
#     "км МКАД 31-й",
#     "км МКАД 32-й",
#     "км МКАД 33-й",
#     "км МКАД 34-й",
#     "км МКАД 35-й",
#     "км МКАД 38-й",
#     "км МКАД 39-й",
#     "км МКАД 4-й",
#     "км МКАД 40-й",
#     "км МКАД 41-й",
#     "км МКАД 42-й",
#     "км МКАД 43-й",
#     "км МКАД 44-й (внешняя сторона)",
#     "км МКАД 46-й",
#     "км МКАД 48-й",
#     "км МКАД 49-й",
#     "км МКАД 5-й",
#     "км МКАД 51-й",
#     "км МКАД 52-й",
#     "км МКАД 53-й",
#     "км МКАД 54-й",
#     "км МКАД 56-й",
#     "км МКАД 58-й",
#     "км МКАД 6-й",
#     "км МКАД 60-й",
#     "км МКАД 62-й",
#     "км МКАД 63-й",
#     "км МКАД 64-й",
#     "км МКАД 65-й",
#     "км МКАД 67-й",
#     "км МКАД 69-й",
#     "км МКАД 7-й",
#     "км МКАД 71-й",
#     "км МКАД 73-й",
#     "км МКАД 74-й",
#     "км МКАД 78-й",
#     "км МКАД 79-й",
#     "км МКАД 8-й",
#     "км МКАД 80-й",
#     "км МКАД 81-й",
#     "км МКАД 82-й",
#     "км МКАД 83-й",
#     "км МКАД 84-й",
#     "км МКАД 87-й",
#     "км МКАД 89-й",
#     "км МКАД 9-й",
#     "км МКАД 90-й",
#     "км МКАД 91-й",
#     "км МКАД 92-й",
#     "км МКАД 93-й",
#     "км МКАД 94-й"]
# for i in MKAD:
#     db.update_many({"data.infoDtp.street" : i}, 
#         {"$set" : { "data.infoDtp.street" : "МКАД",  "data.infoDtp.km" : i.split(" ")[2].split("-")[0]}})
