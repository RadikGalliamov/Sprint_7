import allure
from helpers.api_helpers import create_order


@allure.title("Успешное создание заказа")
def test_successful_order_creation():
    response = create_order()
    assert response.status_code == 201
    assert "track" in response.json()  # тело ответа содержит track
