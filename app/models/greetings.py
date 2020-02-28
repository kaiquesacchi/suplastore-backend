from .. import db


class ModelGreetings(db.Model):
    name = db.Column(db.String(128), primary_key=True)
    greeting = db.Column(db.String(256), nullable=False)

    def __init__(self, name, greeting):
        self.name = name
        self.greeting = greeting

    def __repr__(self):
        return f'Greeting(name:{self.name}, greeting:{self.greeting})'
