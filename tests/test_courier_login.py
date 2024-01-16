import allure
from helpers.api_helpers import login_courier
from data import TestDataLogin


class TestCourierLogin:
    @allure.title("Успешный вход курьера в систему")
    def test_authorization_with_valid_login_and_password(self):
        response = login_courier(TestDataLogin.valid_login_and_valid_password)
        assert response.status_code == 200, f"Ожидался код состояния 200, но был получен {response.status_code}. Ответ: {response.text}"

    @allure.title("При авторизации без обязательного поля login - получаем ошибку")
    def test_authorization_with_login_is_invalid(self):
        response = login_courier(TestDataLogin.without_login_valid_password)
        assert response.status_code == 404, f"Ожидался код состояния 404, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("При авторизации без обязательного поля password - получаем ошибку")
    def test_authorization_without_field_password(self):
        response = login_courier(TestDataLogin.valid_login_without_password)
        assert response.status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Cистема вернёт ошибку, если неправильно указать логин")
    def test_authorization_with_login_is_invalid(self):
        response = login_courier(TestDataLogin.valid_non_existent_login)
        assert response.status_code == 404, f"Ожидался код состояния 404, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("При авторизации без обязательного поля password - получаем ошибку")
    def test_authorization_with_password_is_invalid(self):
        response = login_courier(TestDataLogin.valid_login_without_password)
        assert response.status_code == 400, f"Ожидался код состояния 400, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку")
    def test_authorization_with_non_existent_user(self):
        response = login_courier(TestDataLogin.non_existent_user)
        assert response.status_code == 404, f"Ожидался код состояния 404, но был получен {response.status_code}. Ответ: {response.text}"
        assert response.json()["message"] == "Учетная запись не найдена", f"Ответ: {response.text}"

    @allure.title("Успешный запрос возвращает id")
    def test_authorization_successful_request_returns_id(self):
        response = login_courier(TestDataLogin.valid_login_and_valid_password)
        assert response.status_code == 200, f"Ожидался код состояния 200, но был получен {response.status_code}. Ответ: {response.text}"
        assert "id" in response.json(), "Неверный или не получен id курьера"
