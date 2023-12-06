from models import db, Item

class ItemRepository:

    def add_item(self, item):
        db.session.add(item)
        db.session.commit()

    def update_item(self, item_id, update_data):
        item = Item.query.filter_by(id=item_id).first()
        if item:
            item.name = update_data.get('name', item.name)
            item.description = update_data.get('description', item.description)
            db.session.commit()

    def delete_item(self, item_id):
        item = Item.query.filter_by(id=item_id).first()
        if item:
            db.session.delete(item)
            db.session.commit()

