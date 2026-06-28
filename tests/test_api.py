from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict():
    response = client.post("/predict", json={
        "carat": 0.89,
        "cut": "Premium",
        "color": "H",
        "clarity": "SI1",
        "depth": 62.0,
        "table": 59.0,
        "x": 6.13,
        "y": 6.07,
        "z": 3.78
    })
    assert response.status_code == 200
    assert "predicted_price" in response.json()
    assert response.json()["predicted_price"] > 0


def test_invalid_input():
    response = client.post("/predict", json={
        "carat": -1,
        "cut": "Premium",
        "color": "H",
        "clarity": "SI1",
        "depth": 62.0,
        "table": 59.0,
        "x": 6.13,
        "y": 6.07,
        "z": 3.78
    })
    assert response.status_code == 422 