from flask_restful import Resource
from .. import db


class AppSettings(Resource):
    def get(self):
        return {'message': 'All set!'}

    def post(self):
        db.create_all()
        return {'message': 'Tables created!'}
