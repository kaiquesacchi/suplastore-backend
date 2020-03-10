from .. import db


class ModelCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.String(), nullable=False)
    status = db.Column(db.String(128), nullable=False)

    def __init__(self):
        self.products = '[]'
        self.status = 'open'

    def __repr__(self):
        return f'<Cart(products:{self.products}, id:{self.id})>'
