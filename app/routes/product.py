from flask import request
from flask_restful import Resource, reqparse
from ..models.product import ModelProduct
from .. import db

from ..performance.time_measuring import time_function


class Product(Resource):

    @time_function
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'id',
            type=str,
            help="Product's ID"
        )
        parser.add_argument(
            'type',
            type=str,
            help="Product's type"
        )
        args = parser.parse_args(strict=True)

        if args.id:
            result = ModelProduct.query.filter_by(id=args.id).first()
            return {
                "name": result.name,
                "description": result.description,
                "availableQuantity": result.availableQuantity,
                "price": result.price,
                "image": result.image,
                "type": result.type,
                "id": result.id
            }
        elif args.type:
            result = ModelProduct.query.filter_by(type=args.type).all()
        else:
            result = ModelProduct.query.all()
        return {
            'products': list(map(lambda x: {
                "name": x.name,
                "description": x.description,
                "availableQuantity": x.availableQuantity,
                "price": x.price,
                "image": x.image,
                "type": x.type,
                "id": x.id
            }, result))
        }

    @time_function
    def post(self):
        body = request.get_json()
        if (body is None or any(map(lambda attribute: attribute not in body, ["name", "description", "availableQuantity", "price", "image", "type"]))):
            return {'message': "Request must have body with 'name', 'description', 'availableQuantity', 'price', 'image' and 'type'"}, 400
        product = ModelProduct(
            name=body["name"],
            description=body["description"],
            availableQuantity=body["availableQuantity"],
            price=body["price"],
            image=body["image"],
            type=body["type"]
        )
        db.session.add(product)
        db.session.commit()
        return {'message': 'Created!'}
