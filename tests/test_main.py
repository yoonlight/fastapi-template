from main import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_item():
    response = client.get("/items/1?q=5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "5"}
