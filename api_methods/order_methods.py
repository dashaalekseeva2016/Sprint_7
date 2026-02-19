import requests
import allure
from url import URL
from data import OrderData
class OrderMethods:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(order_data: dict = None):
        if order_data is None:
            order_data = OrderData.ORDER_BODY.copy()
        return requests.post(URL.ORDERS, json=order_data)
    
    @staticmethod
    @allure.step("Создание заказа с цветами")
    def create_order_with_colors(colors: list = None):
        order_data = OrderData.ORDER_BODY.copy()
        if colors is not None:
            order_data["color"] = colors
        return OrderMethods.create_order(order_data)
    
    @staticmethod
    @allure.step("Получение заказа по номеру трека")
    def get_order_by_track(track: int):
        url = f"{URL.ORDERS_TRACK}?t={track}"
        return requests.get(url)
    
    @staticmethod
    @allure.step("Получение ID заказа по треку")
    def get_order_id_by_track(track: int):
        response = OrderMethods.get_order_by_track(track)
        if response.status_code == 200:
            response_data = response.json()
            if "order" in response_data:
                return response_data["order"].get("id")
            return response_data.get("id")
        return None
    
    @staticmethod
    @allure.step("Принятие заказа курьером")
    def accept_order(order_id: int, courier_id: int):
        url = f"{URL.ORDERS_ACCEPT}{order_id}"
        params = {"courierId": courier_id}
        return requests.put(url, params=params)
    
    @staticmethod
    @allure.step("Получение списка всех заказов")
    def get_orders_list():
        return requests.get(URL.ORDERS)