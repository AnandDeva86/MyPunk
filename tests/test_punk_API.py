import requests
import pytest
import json

from src.punk_API import PunkAPI


@pytest.fixture()
def api_connection():
    API_response = requests.get('https://api.punkapi.com/v2/beers')
    return API_response


def test_get_data(api_connection):
    api_response = PunkAPI()
    response = api_response.get_data()
    assert response is not None
    assert response.status_code == 200
    assert response.headers["Content-Type"] == api_connection.headers["Content-Type"]

    json_data = response.json()
    assert len(json_data) == len(json.loads(api_connection.text))
    assert json_data[11]['name'] == 'Arcade Nation'

