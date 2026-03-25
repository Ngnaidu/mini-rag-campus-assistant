from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_empty_question():

    response = client.post("/chat", json={"question": ""})

    assert response.status_code == 200