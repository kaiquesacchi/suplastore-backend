from .. import db


class ModelUsers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(128), nullable=False)
    cart = db.Column(db.Integer, nullable=False)
    purchases = db.Column(db.ARRAY(db.String(128)), nullable=False)
    profilePic = db.Column(db.String, nullable=False)
    address = db.Column(db.String(256), nullable=True)
    def __init__(self, email, password, name, birthdate, cpf, phone):
        self.email = email
        self.password = password
        self.name = name
        self.birthdate = birthdate
        self.cpf = cpf
        self.phone = phone

    def __repr__(self):
        return f'<User(name:{self.name}, email:{self.email}, id:{self.id})>'
