import pytest
import allure
from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods

@pytest.fixture
def created_courier():
    with allure.step("Создание тестового курьера"):
        courier_data, courier_id = CourierMethods.create_and_get_courier_id()
        yield {"data": courier_data, "id": courier_id}
        CourierMethods.delete_courier(courier_id)
          

@pytest.fixture
def created_order():
    with allure.step("Создание тестового заказа"):
        response = OrderMethods.create_order_with_colors(["BLACK"])
        assert response.status_code == 201
        
        track = response.json()["track"]
        yield track

@pytest.fixture(autouse=True)
def test_logger(request):
    allure.dynamic.title(f"Test: {request.node.name}")
    allure.dynamic.description(f"Running test: {request.node.name}")
    
    yield
    
    with allure.step("Test completed"):
        pass