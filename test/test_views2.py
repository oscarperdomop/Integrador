import pytest
import json
from app import create_app, db

@pytest.fixture
def client():
    app = create_app('config_test')
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_login_user(client):
    response = client.post('/login', data=json.dumps({
        'username': 'testuser',
        'password': 'password'
    }), content_type='application/json')
    assert response.status_code == 200
