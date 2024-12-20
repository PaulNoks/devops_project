import pytest
from app import app  # Импортируем Flask-приложение

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Проверяем, что наш endpoint работает."""
    response = client.get('/api/message')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
