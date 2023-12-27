import allure
import requests
import random
import string

BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1'


@allure.title("Генерация случайной строки заданной длины")
def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@allure.title("Регистрация нового курьера")
def register_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(f'{BASE_URL}/courier', data=payload)
    return {"login": login, "password": password, "first_name": first_name, "response": response}


@allure.title("Проверка попытки зарегистрировать курьера с уже существующими данными")
def check_duplicate_courier_registration(courier):
    payload = {
        "login": courier["login"],
        "password": courier["password"],
        "firstName": courier["first_name"]
    }

    response = requests.post(f'{BASE_URL}/courier', data=payload)
    return response


@allure.title("Вход курьера в систему")
def login_courier(credentials):
    payload = {
        "login": credentials["login"],
        "password": credentials["password"]
    }

    response = requests.post(f'{BASE_URL}/courier/login', data=payload)
    return response


@allure.title("Создание заказа (логику необходимо реализовать согласно документации API)")
def create_order():
    pass


@allure.title("Получение списка заказов (логику необходимо реализовать согласно документации API)")
def get_order_list():
    pass
