from src.app import app
import json


def test_root_returns_hello_world():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"<p>Hello, World!</p>"


def test_hello_route_returns_welcome_message():
    client = app.test_client()
    response = client.get("/hello")
    json_response = json.loads(response.data)
    assert json_response["Hello"] == "Welcome to the garden"
