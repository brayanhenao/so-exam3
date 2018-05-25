import pytest
from op_stats.app import app
from op_stats.stats import Stats


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_get_cpu_percent(mocker, client):
    mocker.patch.object(Stats, 'get_cpu_percent', return_value=100)
    response = client.get('/getStats/cpu')
    assert response.data.decode('utf-8') == '{"Cpu usage": 100}'
    assert response.status_code == 200


def test_get_ram_available(mocker, client):
    mocker.patch.object(Stats, 'get_ram', return_value=3000)
    response = client.get('/getStats/ram')
    assert response.data.decode('utf-8') == '{"Ram available": 3000}'
    assert response.status_code == 200


def test_get_disk_available(mocker, client):
    mocker.patch.object(Stats, 'get_free_disk', return_value=3000)
    response = client.get('/getStats/disk')
    assert response.data.decode('utf-8') == '{"Free disk": 3000}'
    assert response.status_code == 200
