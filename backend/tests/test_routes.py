import pytest
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


def test_get_all_questions_answers(client):
    client.post("/api/questions/ask", json={"question": "What is the capital of Russia?"})
    response = client.get("/api/questions/")
    json_data = response.get_json()
    assert response.status_code == 200
    assert len(json_data) == 1


def test_get_question_answer_by_id(client):
    response = client.post("/api/questions/ask", json={"question": "What is the capital of Russia?"})
    json_data = response.get_json()
    qa_id = json_data["id"]
    response = client.get(f"/api/questions/{qa_id}")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["question"] == "What is the capital of Russia?"


def test_delete_question_answer_by_id(client):
    response = client.post("/api/questions/ask", json={"question": "What is the capital of Russia?"})
    json_data = response.get_json()
    qa_id = json_data["id"]
    response = client.delete(f"/api/questions/{qa_id}")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["message"] == "Question deleted successfully"
    response = client.get(f"/api/questions/{qa_id}")
    assert response.status_code == 404
    json_data = response.get_json()
    assert json_data["error"] == "Question not found"