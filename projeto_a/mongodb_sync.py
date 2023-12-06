from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "bancomongo"

def update_mongodb(item_id, item_data):
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    db.items.update_one({'id': item_id}, {'$set': item_data}, upsert=True)

def delete_item_mongodb(item_id):
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    db.items.delete_one({'id': item_id})
