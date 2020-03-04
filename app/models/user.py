from .. import db
from sqlalchemy import types


class ModelUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    birthdate = db.Column(db.String, nullable=False)
    cpf = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    cart = db.Column(db.Integer, nullable=False)
    purchases = db.Column(db.String(128), nullable=False)
    profilePic = db.Column(db.String, nullable=False)

    def __init__(self, email, password, name, birthdate, cpf, phone, address):
        self.email = email
        self.password = password
        self.name = name
        self.birthdate = birthdate
        self.cpf = cpf
        self.phone = phone
        self.address = address
        self.cart = 0
        self.purchases = '[]'
        self.profilePic = ""

    def __repr__(self):
        return f'<User(name:{self.name}, email:{self.email}, id:{self.id})>'
