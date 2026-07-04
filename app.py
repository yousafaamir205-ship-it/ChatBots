from flask import Flask, render_template, request, jsonify

from chatbot.engine import find_answer
from chatbot.database import load_knowledge, add_knowledge

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    knowledge = load_knowledge()

    message = request.json["message"]

    answer = find_answer(message, knowledge)

    if answer:
        return jsonify({
            "reply": answer,
            "known": True
        })

    return jsonify({
        "reply": "Sorry, I don't know that yet.",
        "known": False
    })


@app.route("/teach", methods=["POST"])
def teach():

    data = request.json

    add_knowledge(
        data["question"],
        data["answer"],
        data["topic"]
    )

    return jsonify({
        "status": "success"
    })


if __name__ == "__main__":
    app.run(debug=True)