class CourierData:
    DEFAULT_LOGIN = "test_courier"
    DEFAULT_PASSWORD = "password123"
    DEFAULT_FIRSTNAME = "John"
    
    ERROR_MESSAGES = {
        'not_enough_data': "Недостаточно данных для создания учетной записи",
        'login_already_used': "Этот логин уже используется",
        'account_not_found': "Учетная запись не найдена"
    }
class OrderData:
    ORDER_BODY = {
        "firstName": "Eren",
        "lastName": "Yeager",
        "address": "Shiganshina, 2 apt.",
         "metroStation": 4,
        "phone": "+7 909 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2026-03-06",
        "comment": "For attack on titan",
        "color": []
    }

    DEFAULT_ORDER = {
        "firstName": "Eren",
        "lastName": "Yeager",
        "address": "Shiganshina, 2 apt.",
        "metroStation": 4,
        "phone": "+7 909 999 99 99",
        "rentTime": 5,
        "deliveryDate": "2026-03-06",
        "comment": "For attack on titan",
        "color": []
    }
