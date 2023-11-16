import sender_stand_request
import data
#здесь можно получить данные о заказе по его треку
def test_create_order():
    track_number = sender_stand_request.get_order_from_track(sender_stand_request.create_order(data.order_body).json()["track"])
    assert track_number.status_code == 200
#Устинова Виктория Михайловна 10