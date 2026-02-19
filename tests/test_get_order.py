import pytest
import allure
from api_methods.order_methods import OrderMethods

class TestGetOrder:

    @allure.title("Тест успешного получения заказа по номеру")
    def test_get_order_by_track_success(self):
        create_response = OrderMethods.create_order_with_colors(["BLACK"])
        assert create_response.status_code == 201

        track = create_response.json()["track"]    
        get_response = OrderMethods.get_order_by_track(track)
        assert get_response.status_code == 200, f"Expected 200, got {get_response.status_code}"
    
        response_data = get_response.json()    
        assert "order" in response_data
        
        order = response_data["order"]
        assert order["track"] == track, f"Expected track {track}, got {order.get('track')}"
        assert "id" in order
        assert "firstName" in order
        assert "lastName" in order
        
    @allure.title("Тест получения заказа без номера")
    def test_get_order_without_track(self):
        with pytest.raises(TypeError):
            OrderMethods.get_order_by_track()

    @allure.title("Тест получения несуществующего заказа")
    def test_get_nonexistent_order(self):
        nonexistent_track = 999999999
        response = OrderMethods.get_order_by_track(nonexistent_track)
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        
        response_data = response.json()
        assert "message" in response_data
     
        
       
    
    