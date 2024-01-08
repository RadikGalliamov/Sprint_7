import allure
from helpers.api_helpers import register_courier, login_courier


@allure.title("Успешный вход курьера в систему")
def successful_courier_login():
    courier_credentials = register_courier()
    response = login_courier(courier_credentials)
    return response
