import allure
import requests
from helpers.api_helpers import register_courier
from data import TestDataUrl, TestDataRegisterCourier


class TestCourierRegistration:
    @allure.title("Курьера можно создать")
    def test_successful_courier_registration(self):
        response = register_courier()
        assert response[
                   "response"].status_code == 201, f"Ожидался код состояния 201, но был получен {response.status_code}. Ответ: {response.text}"
        assert response["response"].json()["ok"] == True, "Ожидалось что возвращается {'ok': true}"

    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля - логин")
    def test_missing_data_courier_registration_login(self):
        response = register_courier(TestDataRegisterCourier.couriers_register_with_empty_login)
        assert response[
                   "response"].status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert "Недостаточно данных для создания учетной записи" in response[
            "response"].text, f"Текст ошибки {response.text} не соответствует тексту 'Недостаточно данных для создания учетной записи'"

    @allure.title("Чтобы создать курьера, нужно передать в ручку все обязательные поля - пароль")
    def test_missing_data_courier_registration_password(self):
        response = register_courier(TestDataRegisterCourier.couriers_register_with_empty_password)
        assert response[
                   "response"].status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert "Недостаточно данных для создания учетной записи" in response[
            "response"].text, f"Текст ошибки {response.text} не соответствует тексту 'Недостаточно данных для создания учетной записи'"

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_duplicate_login_courier_registration(self):
        first_courier = register_courier()
        response = requests.post(TestDataUrl.COURIER_URL, data=first_courier)
        assert response.status_code == 409, f"Ожидался код состояния 409, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Этот логин уже используется", "Текст ошибки не соответствует ожидаемому 'Этот логин уже используется'"
