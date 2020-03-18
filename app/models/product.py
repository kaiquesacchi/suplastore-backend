from .. import db


class ModelProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, nullable=False)
    availableQuantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image = db.Column(db.String, nullable=False)
    type = db.Column(db.String, nullable=False)

    def __init__(self, name, description, availableQuantity, price, image, type):
        self.name = name
        self.description = description
        self.availableQuantity = availableQuantity
        self.price = price
        self.image = image
        self.type = type

    def __repr__(self):
        return f'<Product(name:{self.name}, id:{self.id})>'
