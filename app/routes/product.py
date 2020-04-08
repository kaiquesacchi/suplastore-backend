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
        parser.add_argument(
            'page_number',
            type=int,
            help="Pagination's page number"
        )
        parser.add_argument(
            'page_size',
            type=int,
            help="Pagination's page size"
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

        result = ModelProduct.query

        if args.type:
            result = result.filter_by(type=args.type)

        if args.page_number is None or args.page_size is None:
            result = result.all()
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

        result = result.paginate(
            page=args.page_number, per_page=args.page_size)
        return {
            'products': list(map(lambda x: {
                "name": x.name,
                "description": x.description,
                "availableQuantity": x.availableQuantity,
                "price": x.price,
                "image": x.image,
                "type": x.type,
                "id": x.id
            }, result.items)),
            'pages': result.pages
        }

        return

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
