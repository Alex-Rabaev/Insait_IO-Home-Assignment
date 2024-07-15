from flask import Blueprint
from app.routes.api.questions import questions


api = Blueprint("api", __name__)

api.register_blueprint(questions, url_prefix="/questions")
