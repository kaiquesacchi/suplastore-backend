from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(debug=False):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)
    api = Api(app)
    define_routes(api)

    # Starts server.
    app.run(debug=debug, host='0.0.0.0', port=5000)


def define_routes(api):
    from .routes.app_settings import AppSettings
    from .routes.product import Product
    from .routes.user import User
    from .routes.cart import Cart

    api.add_resource(Product, '/product')
    api.add_resource(User, '/user')
    api.add_resource(Cart, '/cart')
    api.add_resource(AppSettings, '/appsettings')
