from pymongo import MongoClient

# Configuração do cliente MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["bancomongo"]

class GetItemQuery:
    def execute(self, item_id):
        # A coleção 'items' precisa ser a coleção onde seus itens estão armazenados
        item = db.items.find_one({'_id': item_id})
        
        # Converter o item para um dicionário se não for None, e converter o ObjectId para string
        if item is not None:
            item['_id'] = str(item['_id'])
        return item
