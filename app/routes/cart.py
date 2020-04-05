from flask import request
from flask_restful import Resource, reqparse
from ..models.cart import ModelCart
from .. import db
from ..performance.time_measuring import time_function


class Cart(Resource):
    @time_function
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'id',
            type=str,
            help='ID of the cart'
        )
        args = parser.parse_args(strict=True)

        if args.id:
            result = ModelCart.query.filter_by(id=args.id).first()
        else:
            return {'message': "Request must contain an 'id' argument"}, 400

        if not result:
            return {'message': 'Cart not found'}, 404
        return {
            "id": result.id,
            "products": result.products,
            "totalValue": result.totalValue,
            "userId": result.userId
        }

    @time_function
    def post(self):
        body = request.get_json()
        if (body is None or any(map(lambda attribute: attribute not in body, ["products", "totalValue", "userId"]))):
            return {'message': "Request must have body with 'products', 'userId' and 'totalValue'"}, 400
        cart = ModelCart(
            products=body["products"],
            totalValue=body["totalValue"],
            userId=body["userId"]
        )
        db.session.add(cart)
        db.session.commit()
        return {'message': 'Created!', 'id': cart.id}
