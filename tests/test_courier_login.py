import allure
from helpers.api_helpers import register_courier, login_courier
from data import TestDataLogin


class TestCourierLogin:
    @allure.title("Успешный вход курьера в систему")
    def test_authorization_with_valid_login_and_password(self):
        response = login_courier(TestDataLogin.valid_login_and_valid_login)
        assert response.status_code == 200, f"Ожидался код состояния 200, но был получен {response.status_code}. Ответ: {response.text}"
        assert "id" in response.json()

    @allure.title("Вход курьера с неверными учетными данными - логин")
    def test_authorization_with_login_is_invalid(self):
        response = login_courier(TestDataLogin.invalid_login_and_password)
        assert response.status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Вход курьера с неверными учетными данными - пароль")
    def test_authorization_with_password_is_invalid(self):
        response = login_courier(TestDataLogin.valid_login_and_invalid_login)
        assert response.status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("если какого-то поля нет, запрос возвращает ошибку;")
    def test_authorization_without_login_and_password(self):
        response = login_courier(TestDataLogin.valid_login_without_password)
        assert response.status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;")
    def test_authorization_without_login_and_password(self):
        response = login_courier(TestDataLogin.non_existent_user)
        assert response.status_code == 404, f"Ожидался код состояния 404, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Учетная запись не найдена", f"Ответ: {response.text}"

    @allure.title("Успешная создание курьера -  получен id")
    def test_authorization_with_valid_login_and_password_return_id(self):
        courier_credentials = register_courier(TestDataLogin.valid_login_and_valid_login)
        response = login_courier(courier_credentials)
        assert "id" in response.json(), "Неверный или не получен id курьера"
