from flask import request
from flask_restful import Resource, reqparse
from ..models.cart import ModelCart
from .. import db
import ast

class Cart(Resource):
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
            "products": ast.literal_eval(result.products),
            "status": result.status
        }

    def put(self):
        body = request.get_json()
        if body is None or "id" not in body:
            return {'message': "Request must have body with changes and the 'id' of the cart."}, 400
        cart = ModelCart.query.filter_by(id=body["id"]).first()
        if not cart:
            return {'message': 'Cart not found'}, 404
        
        if "products" in body:
            cart.products = str(body["products"])
        
        if "status" in body:
            cart.status = body["status"]
        
        db.session.commit()
        return {'message': 'Updated!'}
