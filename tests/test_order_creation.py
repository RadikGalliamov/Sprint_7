import pytest
import allure
from helpers.api_helpers import create_order
from data import TestOrderCreation


class TestPostCreatingOrder:
    @allure.title("Создание заказа")
    @pytest.mark.parametrize("data_colors", [
        TestOrderCreation.color_black,
        TestOrderCreation.color_black_and_gray,
        TestOrderCreation.no_color], ids=[
        "color - BLACK",
        "color - GREY",
        "color - NO COLOR"
    ])
    def test_color_selection(self, data_colors):
        response = create_order(data_colors)
        assert response.status_code == 201
        assert "track" in response.json()  # тело ответа содержит track
