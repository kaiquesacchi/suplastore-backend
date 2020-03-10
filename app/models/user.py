from .. import db
from .cart import ModelCart


class ModelUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    cart = db.Column(db.Integer, nullable=False)
    purchases = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password, name):
        cart = ModelCart()
        db.session.add(cart)
        db.session.commit()

        self.email = email
        self.password = password
        self.name = name
        self.cart = cart.id
        self.purchases = '[]'

    def __repr__(self):
        return f'<User(name:{self.name}, email:{self.email}, id:{self.id})>'
