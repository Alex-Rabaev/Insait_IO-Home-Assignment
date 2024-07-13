from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)

app.config.from_object(Config)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]

db = SQLAlchemy(app)


from app import routes
