import pytest
from app import app  # Импортируем приложение из app.py

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Тест для маршрута '/'"""
    response = client.get('/api/message')
    assert response.status_code == 200
    assert response.json == {"message": "Hello, World!"}
