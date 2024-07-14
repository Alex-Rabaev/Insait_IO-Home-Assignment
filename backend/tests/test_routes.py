import pytest
from app import app, db


@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        with app.app_context():
            db.drop_all()


def test_ask_question(client):
    response = client.post("/ask", json={"question": "What is the capital of France?"})
    json_data = response.get_json()
    assert response.status_code == 200
    assert "answer" in json_data
    assert json_data["question"] == "What is the capital of France?"
