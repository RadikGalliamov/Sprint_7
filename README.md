Sprint_7
tests/test_courier_registration.py - Задание 1.Создание курьера
tests/test_courier_login.py - Задание 2.Логин курьера
tests/test_order_creation.py - Задание 3.Создание заказа
tests/test_order_list.py - Задание 4.Список заказов

pytest -v - запуск всех тестов
pytest -v tests/test_courier_registration.py - запуск тестов test_courier_registration.py


pytest tests --alluredir=allure_results - генерировать Allure-отчёт 
allure serve allure_results - сформировать отчёт в формате веб-страницы
requirements.txt - список установленных библиотек
allure_results - файлы для отчетов Allure 
allure-report - отчет Allure