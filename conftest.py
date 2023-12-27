import pytest
from helpers.api_helpers import BASE_URL

"""
Фикстура для передачи базового URL в тесты
"""


@pytest.fixture(scope="session", autouse=True)
def base_url():
    return BASE_URL
