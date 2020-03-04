from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app(debug=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')

    db.init_app(app)
    api = Api(app)
    define_routes(api)

    # Starts server.
    app.run(debug=debug)


def define_routes(api):
    from .routes.greeting import Greeting
    from .routes.app_settings import AppSettings
    from .routes.product import Product
    from .routes.user import User

    api.add_resource(Product, '/product')
    api.add_resource(User, '/user')

    # Development only
    api.add_resource(AppSettings, '/appsettings')
    api.add_resource(Greeting, '/greeting')
