from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_add_valid():
    response = client.post("/calculator/add", json={"numbers": "1,2,3"})
    assert response.status_code == 200
    assert response.json() == {"sum": 6}

def test_api_add_empty():
    response = client.post("/calculator/add", json={"numbers": ""})
    assert response.status_code == 200
    assert response.json() == {"sum": 0}

def test_api_add_newline():
    response = client.post("/calculator/add", json={"numbers": "1\n2,3"})
    assert response.status_code == 200
    assert response.json() == {"sum": 6}

def test_api_add_custom_delimiter():
    response = client.post("/calculator/add", json={"numbers": "//;\n2;3"})
    assert response.status_code == 200
    assert response.json() == {"sum": 5}

def test_api_add_negative():
    response = client.post("/calculator/add", json={"numbers": "1,-2,-3"})
    assert response.status_code == 400
    assert "negative numbers not allowed" in response.json()["detail"]
