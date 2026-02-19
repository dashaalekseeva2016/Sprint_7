import requests
import allure
import pytest
from helpers import *
from url import URL
from api_methods.courier_methods import CourierMethods



class TestCourierCreate:

    @allure.title("Тест на успешное создание курьера")
    def test_create_courier_success(self):
        courier_data = CourierMethods.generate_courier_data()
        response = CourierMethods.create_courier(courier_data)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
          

    @allure.title("Тест на ошибку при создании двух одинаковых курьеров")
    def test_create_duplicate_courier(self, created_courier):
        courier = created_courier
        existing_data = courier["data"]
        response = requests.post(URL.CREATE_COURIER, data=existing_data)
        assert response.status_code == 409
        assert "message" in response.json()

    @allure.title("Тест на создание курьера без обязательных полей")
    @pytest.mark.parametrize("payload", [
        {"password": "123", "firstName": "name"},
        {"login": "test", "firstName": "name"},
        {"login": "test", "password": "123"}
    ])
    def test_create_courier_missing_fields(self, payload):
        response = CourierMethods.create_courier(payload)
        
        assert response.status_code == 400
        assert "message" in response.json()

    @allure.title("Тест на ошибку при создании курьера с существующим логином")
    def test_create_courier_existing_login(self, created_courier):
        existing_data = created_courier["data"]
        new_courier = {
            "login": existing_data["login"],
            "password": CourierMethods.generate_random_string(10),
            "firstName": CourierMethods.generate_random_string(10)
        }
        
        response = requests.post(URL.CREATE_COURIER, data=new_courier)
        
        assert response.status_code == 409
        response_data = response.json()
        assert "message" in response_data