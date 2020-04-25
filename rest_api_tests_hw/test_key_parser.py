"""4. Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параметра:
url - должно быть значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200
Параметры должны быть реализованы через pytest.addoption.
Можно положить фикcтуру и тестовую функцию в один файл.
Основная задача чтобы ваш тест проверял по переданному урлу статус ответа тот который передали,
т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404

пример запуска pytest test_module.py --url=https://mail.ru --status_code=200"""

import pytest
import requests


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    status_code = request.config.getoption("--status_code")
    return requests.get(base_url), status_code


def test_status_code(api_client):
    res, status_code = api_client
    assert str(res.status_code) == str(status_code)