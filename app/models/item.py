from app.extensions import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    link = db.Column(db.String(255))
    status = db.Column(db.String(50), default="Хочу")  # Возможные статусы: Хочу, Куплено, Подарено
    wishlist_id = db.Column(db.Integer, db.ForeignKey('wishlist.id'), nullable=False)

    def __repr__(self):
        return f'<Item {self.description[:20]}>'
