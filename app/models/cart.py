from .. import db


class ModelCart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products = db.Column(db.ARRAY(db.Integer), nullable=False)
    status = db.Column(db.String(128), nullable=False)

    def __init__(self, products, status):
        self.products = products
        self.status = status
        
    def __repr__(self):
        return f'<Cart(products:{self.products}, id:{self.id})>'
