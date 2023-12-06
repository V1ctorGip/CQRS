from repositories import ItemRepository
from models import Item
from mongodb_sync import update_mongodb

class CreateItemCommand:
    def execute(self, data):
        item = Item(name=data['name'], description=data['description'])
        repo = ItemRepository()
        repo.add_item(item)
        update_mongodb(item.id, item.serialize())

class UpdateItemCommand:
    def execute(self, item_id, data):
        repo = ItemRepository()
        updated = repo.update_item(item_id, data)
        if updated:
            updated_item = repo.get_item(item_id)
            update_mongodb(item_id, updated_item.serialize())

class DeleteItemCommand:
    def execute(self, item_id):
        repo = ItemRepository()
        repo.delete_item(item_id)
        update_mongodb(item_id, {"deleted": True})
