from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/hello")
def get_welcome_message():
    return jsonify({"Hello": "Welcome to the garden"})
