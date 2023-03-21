from flask_api.app import app
import json


def test_root_returns_hello_world():
    client = app.test_client()
    response = client.get("/")
    # assert response.data.decode("utf-8") == "<p>Hello, World!</p>"
    assert response.data == b"<p>Hello, World!</p>"


def test_hello_route_returns_welcome_message():
    client = app.test_client()
    response = client.get("/hello")
    response_body = json.loads(response.data)
    assert response.status_code == 200
    assert response_body["Hello"] == "Welcome to the garden"
