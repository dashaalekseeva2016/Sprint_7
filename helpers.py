from api_methods.courier_methods import CourierMethods
from api_methods.order_methods import OrderMethods

def create_test_courier():
    return CourierMethods.create_and_get_courier_id()

def create_test_order(colors=None):
    return OrderMethods.create_order_with_colors(colors)