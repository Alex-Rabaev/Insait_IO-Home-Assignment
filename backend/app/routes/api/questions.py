from database import db
from flask import Blueprint, request, jsonify
from app.models.question_answer import QuestionAnswer
from app.services.openai_service import get_openai_response


questions = Blueprint("questions", __name__)


@questions.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    answer = get_openai_response(question)

    qa = QuestionAnswer(question=question, answer=answer)
    db.session.add(qa)
    db.session.commit()
    db.session.refresh(qa)

    return jsonify({"id": qa.id, "question": question, "answer": answer})


@questions.route("/", methods=["GET"])
def get_all_questions_answers():
    questions_answers = QuestionAnswer.query.all()
    result = [
        {"id": qa.id, "question": qa.question, "answer": qa.answer}
        for qa in questions_answers
    ]
    return jsonify(result)


@questions.route("/<int:id>", methods=["GET"])
def get_question_answer_by_id(id):
    qa = db.session.get(QuestionAnswer, id)
    if not qa:
        return jsonify({"error": "Question not found"}), 404
    return jsonify({"id": qa.id, "question": qa.question, "answer": qa.answer})


@questions.route("/<int:id>", methods=["DELETE"])
def delete_question_answer_by_id(id):
    qa = db.session.get(QuestionAnswer, id)
    if not qa:
        return jsonify({"error": "Question not found"}), 404
    db.session.delete(qa)
    db.session.commit()
    return jsonify({"message": "Question deleted successfully"})
