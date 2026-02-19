import pytest
import allure
from api_methods.order_methods import OrderMethods
from api_methods.courier_methods import CourierMethods


class TestAcceptOrder:
    
    @allure.title("Тест успешного принятия заказа")
    def test_accept_order_success(self, created_courier, created_order):
        courier_id = created_courier["id"]
        track = created_order
        
        order_id = OrderMethods.get_order_id_by_track(track)
        assert order_id is not None
        
        response = OrderMethods.accept_order(order_id, courier_id)
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Тест принятия заказа без ID курьера")
    def test_accept_order_without_courier_id(self):
        create_order_response = OrderMethods.create_order_with_colors(["BLACK"])
        assert create_order_response.status_code == 201
        
        track = create_order_response.json()["track"]
        order_id = OrderMethods.get_order_id_by_track(track)
        assert order_id is not None
        
        with pytest.raises(TypeError):
            OrderMethods.accept_order(order_id) 

    @allure.title("Тест принятия заказа с неверным ID курьера")
    def test_accept_order_invalid_courier_id(self):
        create_order_response = OrderMethods.create_order_with_colors(["BLACK"])
        assert create_order_response.status_code == 201
        
        track = create_order_response.json()["track"]
        order_id = OrderMethods.get_order_id_by_track(track)
        assert order_id is not None

        invalid_courier_id = 999999999
        response = OrderMethods.accept_order(order_id, invalid_courier_id)
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        assert "message" in response.json()
        
    @allure.title("Тест принятия заказа без ID заказа")
    def test_accept_order_without_order_id(self):
        courier_id = CourierMethods.create_and_get_courier_id()
        assert courier_id is not None
        with pytest.raises(TypeError):
            OrderMethods.accept_order(courier_id=courier_id)  

    @allure.title("Тест принятия заказа с неверным ID заказа")
    def test_accept_order_invalid_order_id(self):
        courier_id = CourierMethods.create_and_get_courier_id()
        assert courier_id is not None
        
        invalid_order_id = 999999999
        response = OrderMethods.accept_order(invalid_order_id, courier_id)
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        assert "message" in response.json()
        
     
     