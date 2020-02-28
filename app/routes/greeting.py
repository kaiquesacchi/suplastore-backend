from flask import request
from flask_restful import Resource, reqparse
from ..models.greetings import ModelGreetings
from .. import db


class Greeting(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'name',
            type=str,
            help='Name of the person receiving the greetings'
        )
        args = parser.parse_args(strict=True)
        result = ModelGreetings.query.filter_by(name=args.name).first()

        return {'message': result.greeting}

    def post(self):
        body = request.get_json()
        if body is None or not "name" in body or not "greeting" in body:
            return {'message': "Request must have body with 'name' and 'greeting'"}, 400
        greeting = ModelGreetings(name=body["name"], greeting=body["greeting"])
        db.session.add(greeting)
        db.session.commit()
        return {'message': str(greeting)}
