import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client.list_database_names())
db = client["mongo_demo"]
emp = db["employee"]

cursor = emp.find()
for i in cursor:
    print(i["_id"])