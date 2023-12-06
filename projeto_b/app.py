from flask import Flask, Response
from flask_cors import CORS
from pymongo import MongoClient
import json
from bson import json_util, ObjectId

app = Flask(__name__)
CORS(app)

# Configurar o cliente MongoDB aqui
app.config['MONGO_URI'] = 'mongodb://localhost:27017'
mongo_client = MongoClient(app.config['MONGO_URI'])
db = mongo_client.bancomongo

@app.route('/items', methods=['GET'])
def get_all_items():
    items_cursor = db.items.find()  # Esta linha busca todos os documentos na coleção 'items'
    items_list = list(items_cursor)  # Converte o cursor em uma lista
    # Usar json_util para serializar a lista de itens para JSON
    return Response(json.dumps(items_list, default=json_util.default), mimetype='application/json')

@app.route('/items/<string:item_id>', methods=['GET'])  # item_id deve ser uma string para corresponder ao formato do ObjectId
def get_item(item_id):
    try:
        # O ObjectId precisa ser passado corretamente para a consulta
        item = db.items.find_one({"_id": ObjectId(item_id)})
        # Usar json_util para serializar o item para JSON
        return Response(json.dumps(item, default=json_util.default), mimetype='application/json') if item else ('', 404)
    except Exception as e:
        # Se o ObjectId for inválido ou outro erro ocorrer, retornar erro 400
        return Response(json.dumps({"error": str(e)}, default=json_util.default), status=400, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
