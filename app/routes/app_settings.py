from flask_restful import Resource
from .. import db
import requests


class AppSettings(Resource):
    def get(self):
        average_time_microseconds = 0
        for i in range(100):
            result = requests.get('http://localhost:5000/product').json()
            average_time_microseconds += result["time_microseconds"]
        average_time_microseconds /= 100
        size_response = len(result["products"])
        return {
            "average_time_microseconds": average_time_microseconds,
            "size_response": size_response
        }

    def post(self):
        db.create_all()
        return {'message': 'Tables created!'}
