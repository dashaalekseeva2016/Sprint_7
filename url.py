class URL:
    BAS_URL = "http://qa-scooter.praktikum-services.ru"
    CREATED_COURIER = f"{BAS_URL}/api/v1/courier"
    LOGIN_COURIER = f"{BAS_URL}/api/v1/courier/login"
    ORDERS = f"{BAS_URL}/api/v1/oreders"
    DELETE_COURIER = f"{BAS_URL}/api/v1/courier/:id"
    ORDERS_ACCEPT = f"{BAS_URL}/api/v1/orders/accept/:id"
    ORDERS_TRACK = f"{BAS_URL}/api/v1/orders/track"