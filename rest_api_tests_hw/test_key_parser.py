import pytest
import requests

#pytest test_key_parser.py --url=https://ya.ru/sfhfhfhfhfhfhfhfh --status_code=404


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return requests.get(base_url), status_code


def test_status_code(api_client):
    res, status_code = api_client
    assert str(res.status_code) == str(status_code)