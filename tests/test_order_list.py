import allure
from helpers.api_helpers import get_order_list


class TestOrderList:
    @allure.title("Получение списка заказов")
    def test_getting_list_of_orders(self):
        response = get_order_list()
        assert response.status_code == 200
        assert "orders" in response.json()
