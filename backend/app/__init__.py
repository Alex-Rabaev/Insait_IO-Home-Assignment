from flask import Flask
from flask_cors import CORS
from config import Config
from app.routes import routes
from database import db


def create_app(testing: bool = False):
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)
    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = app.config["TEST_SQLALCHEMY_DATABASE_URI"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]
    db.init_app(app)

    app.register_blueprint(routes)

    return app
