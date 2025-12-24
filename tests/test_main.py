from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_security_unauthorized():
    response = client.get("/")
    assert response.status_code == 401

def test_security_authorized():
    response = client.get("/", auth=("admin", "secret"))
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, admin!"