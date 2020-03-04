from flask import request
from flask_restful import Resource, reqparse
from ..models.user import ModelUser
from .. import db


class User(Resource):
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
            "email": result.email,
            "password": result.password,
            "name": result.name,
            "birthdate": result.birthdate,
            "cpf": result.cpf,
            "phone": result.phone,
            "address": result.address,
            "cart": result.cart,
            "purchases": result.purchases,
            "profilePic": result.profilePic
        }

    def post(self):
        body = request.get_json()
        if (body is None or any(map(lambda attribute: attribute not in body, ["email", "password", "name", "birthdate", "cpf", "phone", "address"]))):
            return {'message': "Request must have body with 'email', 'password', 'name', 'birthdate', 'cpf', 'phone', 'address'"}, 400
        user = ModelUser(
            email=body["email"],
            password=body["password"],
            name=body["name"],
            birthdate=body["birthdate"],
            cpf=body["cpf"],
            phone=body["phone"],
            address=body["address"]
        )
        db.session.add(user)
        db.session.commit()
        return {'message': 'Created!'}
