from flask import Blueprint
from app.routes.api import api


routes = Blueprint("routes", __name__)

routes.register_blueprint(api, url_prefix="/api")
