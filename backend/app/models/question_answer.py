from database import db


class QuestionAnswer(db.Model):
    __tablename__ = "questions_answers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)
