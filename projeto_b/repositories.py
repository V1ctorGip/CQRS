from pymongo import MongoClient
from bson.objectid import ObjectId

# Substitua pelo seu URI de conexão ao MongoDB
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "bancomongo"

class ItemRepository:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]

    def get_item(self, item_id):
        # Converta item_id para ObjectId se estiver usando o padrão do MongoDB
        if isinstance(item_id, str):
            item_id = ObjectId(item_id)
        return self.db.items.find_one({'_id': item_id})
    
    def get_all_items(self):
        # Isso irá buscar todos os itens na coleção e retornar uma lista
        return list(self.db.items.find({}))

