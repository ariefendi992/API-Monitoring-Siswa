from flask import Flask
from settings import Config
from API.registers_blueprint import register_app

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)
    register_app(app)


    return app


def register_extensions(app):
    from API.extensions import db, migrate

    db.init_app(app)
    migrate.init_app(app, db)


app = create_app()