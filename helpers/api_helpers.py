import allure
import requests
import json
import random
import string
from data import LOGIN_COURIER_URL, COURIER_URL, ORDER_URL


@allure.step("Регистрация нового пользователя")
# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


@allure.step("Генерация случайной строки заданной длины")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.step("Регистрация нового курьера")
def register_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(COURIER_URL, data=payload)
    return {"login": login, "password": password, "first_name": first_name, "response": response}


@allure.step("Вход курьера в систему")
def login_courier(credentials):
    payload = {
        "login": credentials["login"],
        "password": credentials["password"]
    }
    response = requests.post(LOGIN_COURIER_URL, data=json.dumps(payload))
    return response


@allure.step("Создание заказа")
def create_order(payload=None):
    if payload is None:
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": ["BLACK"]
        }
    response = requests.post(ORDER_URL, json=payload)
    return response


@allure.step("Получение списка заказов")
def get_order_list():
    order_list = requests.get(ORDER_URL)
    return order_list


@allure.step("Регистрация нового курьера")
def register_courier(payload=None):
    if payload is None:
        payload = {}

        # Генерируем новые значения для полей, если они не были переданы
    payload["login"] = payload.get("login", generate_random_string(10))
    payload["password"] = payload.get("password", generate_random_string(10))
    payload["firstName"] = payload.get("firstName", generate_random_string(10))

    response = requests.post(COURIER_URL, data=payload)
    return {"login": payload["login"], "password": payload["password"], "first_name": payload["firstName"],
            "response": response}
