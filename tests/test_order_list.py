import allure
from helpers.api_helpers import get_order_list


@allure.title("Получение списка заказов")
def test_order_list():
    response = get_order_list()
    assert response.status_code == 200
    assert "orders" in response.json()
