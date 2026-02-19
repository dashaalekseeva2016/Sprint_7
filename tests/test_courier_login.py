import requests
import allure
import pytest
from helpers import *
from url import URL
from api_methods.courier_methods import CourierMethods

class TestCourierLogin:

    @allure.title("Тест успешной авторизации курьера")
    def test_login_courier_success(self, created_courier):
        courier_info = created_courier
        
        response = CourierMethods.login_courier(
            courier_info["data"]["login"], 
            courier_info["data"]["password"]
        )
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert response.json()["id"] == courier_info["id"]

    @allure.title("Тест на ошибку при авторизации без заполнения обязательного поля")
    @pytest.mark.parametrize("payload", [
        {"password": "12345"},
        {"login": "test"},
        {}
    ])
    def test_login_missing_fields(self, payload):
        response = requests.post(URL.LOGIN_COURIER, data=payload)
        assert response.status_code == 400
        
    @allure.title("Тест авторизации с неверным логином")
    def test_login_wrong_login(self,created_courier):
        courier_info = created_courier
        response = CourierMethods.login_courier("nonexistent",courier_info["data"]["password"])
        
        assert response.status_code == 404
        assert "message" in response.json()

    @allure.title("Тест авторизации с неверным паролем")
    def test_login_wrong_password(self, created_courier):
        courier_info = created_courier
        
        response = CourierMethods.login_courier(courier_info["data"]["login"], "wrong_password")
        
        assert response.status_code == 404
        assert "message" in response.json()
    