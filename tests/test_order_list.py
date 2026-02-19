import requests
import allure
from url import URL

class TestOrdersList:
    @allure.title("Тест получения списка заказов")
    def test_get_orders_list(self):
        response = requests.get(URL.ORDERS)
        
        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)