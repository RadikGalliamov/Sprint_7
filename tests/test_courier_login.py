import allure
from helpers.api_helpers import register_courier, login_courier


@allure.title("Успешный вход курьера в систему")
def test_successful_courier_login():
    courier_credentials = register_courier()
    response = login_courier(courier_credentials)
    assert response.status_code == 200
    assert "id" in response.json()


@allure.title("Вход курьера с неверными учетными данными")
def test_invalid_courier_login():
    response = login_courier({"login": "nonexistent", "password": "invalid"})
    assert response.status_code == 401  # Предполагаем, что 401 - корректный код ошибки для неверного входа
    assert response.json()["error"] == "Invalid login or password"
