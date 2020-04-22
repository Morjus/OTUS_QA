import pytest
import requests


class ApiClient:
    """
    Простой api клиент.
    Работает через requests.
    """

    def __init__(self, base_address):
        """
        base_address: базовый адрес для инициализации экземпляра
        Например: https://ya.ru/

        """
        self.base_address = base_address

    def post(self, path="/", params=None, data=None, headers=None):
        """
        POST запрос
        В переменную path нужно задавать конкретную страницу на базовом адресе.
        Например 'search/'
        На выходе получится:
        https://ya.ru/search/

        """

        url = self.base_address + path
        print(f"POST request to {url}")
        return requests.post(url=url, params=params, data=data, headers=headers)

    def get(self, path="/", params=None):
        """
        GET запрос
        В переменную path нужно задавать конкретную страницу на базовом адресе.
        Например 'search/'
        На выходе получится:
        https://ya.ru/search/

        """

        url = self.base_address + path
        print(f"GET request to {url}")
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    """
    Параметр parser необходим для корректной работы ключей через pytest.
    Именно он находит соответствие переданного ключа
    и меняет параметры запроса через фикстуру

    """
    parser.addoption("--url",
                     action="store",
                     default="https://ya.ru/",
                     help="Key for request url.")


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return ApiClient(base_address=base_url)
