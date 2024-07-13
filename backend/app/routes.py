from app import app, db
from flask import request, jsonify
from app.models import QuestionAnswer
from app.services.openai_service import get_openai_response


@app.route("/ask", methods=["POST"])
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


# get messsage ok
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "ok"})
