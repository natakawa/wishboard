from app.extensions import db

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    is_private = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    items = db.relationship('Item', backref='wishlist', lazy=True)

    def __repr__(self):
        return f'<Wishlist {self.title}>'
