from flask import Flask, render_template, request, jsonify
from models import db
from commands import CreateItemCommand, UpdateItemCommand, DeleteItemCommand
from flask_cors import CORS
from mongodb_sync import delete_item_mongodb, update_mongodb

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items', methods=['POST'])
def create_item():
    command = CreateItemCommand()
    command.execute(request.json)
    return jsonify({"status": "success"}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    command = UpdateItemCommand()
    command.execute(item_id, data)
    update_mongodb(item_id, data)
    return jsonify({"status": "success"})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    command = DeleteItemCommand()
    command.execute(item_id)
    delete_item_mongodb(item_id)
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)

with app.app_context():
    db.create_all()
