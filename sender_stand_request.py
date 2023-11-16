import configuration
import requests

# здеь создается заказ
def create_order(order_body):
    return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH,
                         json=order_body)

#здесь можно получить наш заказ по его треку
def get_order_from_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH + str(track))