from app import app
from flask import request, jsonify


@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.get_json()
    question = data.get("question")
    if not question:
        return jsonify({"error": "No question provided"}), 400

    # For now, just return the received question
    return jsonify({"question": question})


# get messsage ok
@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "ok"})
