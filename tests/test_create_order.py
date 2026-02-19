import pytest
import allure
from api_methods.order_methods import OrderMethods


class TestCreateOrder:

    @allure.title("Тест создания заказа с разными цветами")
    @pytest.mark.parametrize("colors", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_colors(self, colors):
        response = OrderMethods.create_order_with_colors(colors)
        
        assert response.status_code == 201
        assert "track" in response.json()