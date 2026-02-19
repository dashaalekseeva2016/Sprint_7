import requests
import random
import string
import allure
from url import URL

class CourierMethods:
    @staticmethod
    @allure.step("Генерация случайной строки")
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    @staticmethod
    @allure.step("Генерация данных для нового курьера")
    def generate_courier_data():
        return {
            "login": CourierMethods.generate_random_string(10),
            "password": CourierMethods.generate_random_string(10),
            "firstName": CourierMethods.generate_random_string(10)
        }
    
    @staticmethod
    @allure.step("Создание курьера")
    def create_courier(courier_data: dict):
        return requests.post(URL.CREATE_COURIER, data=courier_data)
    
    @staticmethod
    @allure.step("Авторизация курьера")
    def login_courier(login: str, password: str):
        payload = {"login": login, "password": password}
        return requests.post(URL.LOGIN_COURIER, data=payload)
    
    @staticmethod
    @allure.step("Создание курьера и получение его данных")
    def create_courier_and_return_data():
        courier_data = CourierMethods.generate_courier_data()
        response = CourierMethods.create_courier(courier_data)
        if response.status_code == 201:
            return courier_data
        return None
    
    @staticmethod
    @allure.step("Получение ID курьера")
    def get_courier_id(login: str, password: str):
        response = CourierMethods.login_courier(login, password)
        if response.status_code == 200:
            return response.json()["id"]
        return None
    
    @staticmethod
    @allure.step("Создание курьера и получение его ID")
    def create_and_get_courier_id():
        courier_data = CourierMethods.create_courier_and_return_data()
        if courier_data is None:
            return None, None
        courier_id = CourierMethods.get_courier_id(
            courier_data["login"], 
            courier_data["password"]
        )
        return courier_data, courier_id
    
    @staticmethod
    @allure.step("Удаление курьера с ID")
    def delete_courier(courier_id: int):
        url = f"{URL.DELETE_COURIER}{courier_id}"
        return requests.delete(url)