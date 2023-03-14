from api.app import app


def test_root_returns_hello_world():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"<p>Hello, World!</p>"
