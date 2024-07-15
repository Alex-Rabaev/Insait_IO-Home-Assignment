from dotenv import load_dotenv

import os

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    TEST_SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL")
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
