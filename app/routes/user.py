from flask import request
from flask_restful import Resource, reqparse
from ..models.user import ModelUser
from .. import db
from ..performance.time_measuring import time_function


class User(Resource):

    @time_function
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'id',
            type=str,
            help='ID of the user'
        )
        parser.add_argument(
            'email',
            type=str,
            help='Email of the user'
        )
        args = parser.parse_args(strict=True)

        if args.id:
            result = ModelUser.query.filter_by(id=args.id).first()
        elif args.email:
            result = ModelUser.query.filter_by(email=args.email).first()
        else:
            return {'message': "Request must contain an 'id' or 'email' argument"}, 400

        if not result:
            return {'message': 'User not found'}, 404
        return {
            "id": result.id,
            "email": result.email,
            "password": result.password,
            "name": result.name
        }

    @time_function
    def post(self):
        body = request.get_json()
        if (body is None or any(map(lambda attribute: attribute not in body, ["email", "password", "name"]))):
            return {'message': "Request must have body with 'email', 'password' and 'name'"}, 400
        user = ModelUser(
            email=body["email"],
            password=body["password"],
            name=body["name"],
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'Created!'}
