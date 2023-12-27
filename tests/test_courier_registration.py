import allure
import requests
from helpers.api_helpers import register_courier, check_duplicate_courier_registration


@allure.title("Курьера можно создать")
def test_successful_courier_registration():
    response = register_courier()
    assert response.status_code == 201  # Проверка, что код ответа - 201 Created
    assert response.json()["ok"] == True  # Проверка, что возвращается {"ok": true}


@allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля")
def test_missing_data_courier_registration():
    payload = {}  # Пустой запрос
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert response.status_code == 400
    assert response.json()["message"] == "Недостаточно данных для создания учетной записи"


@allure.title("Нельзя создать двух одинаковых курьеров")
def test_duplicate_login_courier_registration():
    first_courier = register_courier()

    # Пытаемся создать второго курьера с тем же логином
    payload = {
        "login": first_courier["login"],
        "password": "password456",
        "firstName": "Jane"
    }
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
    assert response.status_code == 409
    assert response.json()["message"] == "Этот логин уже используется"
