from .. import db


class ModelCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.String(), nullable=False)
    totalValue = db.Column(db.Float, nullable=False)
    userId = db.Column(db.Integer, nullable=False)

    def __init__(self, products, totalValue, userId):
        self.products = products
        self.totalValue = totalValue
        self.userId = userId

    def __repr__(self):
        return f'<Cart(products:{self.products}, id:{self.id})>'
