import pytest
import allure
from api_methods.courier_methods import CourierMethods

class TestCourierDelete:
    @allure.title("Тест успешного удаления курьера")
    def test_delete_courier_success(self):
        courier_data = CourierMethods.create_courier_and_return_data()
        assert courier_data is not None
        
        login_response = CourierMethods.login_courier(
            courier_data["login"], 
            courier_data["password"]
        )
        assert login_response.status_code == 200
        courier_id = login_response.json()["id"]
        
        delete_response = CourierMethods.delete_courier(courier_id)
        
        assert delete_response.status_code == 200, f"Expected 200, got {delete_response.status_code}"
        assert delete_response.json() == {"ok": True}, f"Expected {{'ok': True}}, got {delete_response.json()}"
        
    @allure.title("Тест удаления курьера с несуществующим ID")
    def test_delete_courier_nonexistent_id(self):
        nonexistent_id = 999999999
        
        response = CourierMethods.delete_courier(nonexistent_id)
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        assert "message" in response.json()
        
    @allure.title("Тест удаления курьера без передачи ID")
    def test_delete_courier_without_id(self):
        with pytest.raises(TypeError):
            CourierMethods.delete_courier()    
