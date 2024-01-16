import random


class TestDataUrl:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
    COURIER_URL = f'{BASE_URL}courier/'
    LOGIN_COURIER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
    ORDER_URL = f'{BASE_URL}orders'


class TestDataLogin:
    valid_non_existent_login = {"login": "PetrovPetrov2024",
                                "password": "12345"}
    valid_login_and_invalid_login = {"login": "Petrov",
                                     "password": "[12345]"}
    valid_login_and_valid_password = {"login": "Petrov",
                                      "password": "12345"}
    valid_login_without_password = {"login": "Petrov",
                                    "password": ""}
    non_existent_user = {"login": "Petrov890890",
                         "password": "dfuebw7685"}
    without_login_valid_password = {"login": "",
                                    "password": "12345"}


class TestDataRegisterCourier:

    couriers_register_two_same_courier = {"login": "Ivanov1989",
                                          "password": "12345",
                                          "firstName": "hero1989"}
    couriers_register_with_empty_login = {"login": "",
                                          "password": "12345",
                                          "firstName": f"hero1989_{random.randint(1, 100)}"}
    couriers_register_with_empty_password = {"login": f"Ivanov1989_{random.randint(1, 100)}",
                                             "password": "",
                                             "firstName": f"hero1989_{random.randint(1, 100)}"}
    couriers_register_with_empty_firstName = {"login": f"Ivanov1989_{random.randint(1, 100)}",
                                              "password": "12345",
                                              "firstName": ""}


class TestOrderCreation:
    color_black = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK"
        ]
    }
    color_black_and_gray = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            "BLACK", "GRAY"
        ]
    }
    no_color = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": [
            ""
        ]
    }
