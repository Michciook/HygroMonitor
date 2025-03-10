import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_data(client):
    response = client.get('/api/data/')
    assert response.status_code == 200
    assert isinstance(response.json.get('labels'), list)
    assert isinstance(response.json.get('values'), list)


def test_post_invalid_json_format(client):
    response = client.post('/api/get_readings/', json={'humidity_wrong': 200})
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid JSON format'


@pytest.mark.parametrize('invalid_value', [200, -5, 4.6, None, 'string'])
def test_post_invalid_data(client, invalid_value):
    response = client.post('/api/get_readings/', json={'humidity': invalid_value})
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid data'


def test_post_valid_data(client):
    response = client.post('/api/get_readings/', json={'humidity': 80})
    assert response.status_code == 200
    assert response.json['message'] == 'Data received successfully'