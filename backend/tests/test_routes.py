import pytest
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database import db


@pytest.fixture
def app():
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_ask_question(client):
    response = client.post("/api/questions/ask", json={"question": "What is the capital of France?"})
    json_data = response.get_json()
    assert response.status_code == 200
    assert "answer" in json_data
    assert json_data["question"] == "What is the capital of France?"
