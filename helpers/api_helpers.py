import allure
import requests
import random
import string
from data import TestDataUrl
from data import TestOrderCreation


@allure.step("Генерация случайной строки заданной длины")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.step("Регистрация нового курьера")
def register_courier(payload=None):
    if payload is None:
        payload = {}

    # Генерируем новые значения для полей, если они не были переданы применяя функцию - generate_random_strin
    payload["login"] = payload.get("login", generate_random_string(10))
    payload["password"] = payload.get("password", generate_random_string(10))
    payload["firstName"] = payload.get("firstName", generate_random_string(10))

    response = requests.post(TestDataUrl.COURIER_URL, data=payload)
    return {"login": payload["login"], "password": payload["password"], "first_name": payload["firstName"],
            "response": response}


@allure.step("Вход курьера в систему")
def login_courier(credentials):
    payload = {
        "login": credentials["login"],
        "password": credentials["password"]
    }
    response = requests.post(TestDataUrl.LOGIN_COURIER_URL, data=payload)
    return response


@allure.step("Создание заказа")
def create_order(payload=None):
    if payload is None:
        payload = TestOrderCreation.color_black
    response = requests.post(TestDataUrl.ORDER_URL, json=payload)
    return response


@allure.step("Получение списка заказов")
def get_order_list():
    order_list = requests.get(TestDataUrl.ORDER_URL)
    return order_list


@allure.step("Удаление нового курьера")
def delete_courier(id_courier=None):
    response = requests.delete(f"{TestDataUrl.COURIER_URL}{id_courier}")
    return response
