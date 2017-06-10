'''
园岭八街
'''
from car import Car

class YuanlingEightRoad(object):

    def __init__(self):
        self.name = '园岭八街'
        self.length = 10
        self.width = 2
        self.parking_lot_number = 20
        self.parking_lot = []

    def parking(self, car):
        if len(self.parking_lot) >= self.parking_lot_number:
            raise ValueError('不好意思，车位已满')
        self.parking_lot.append(car)

    def leave(self, car):
        if car not in self.parking_lot:
            raise ValueError('车不在车位内')
        self.parking_lot.remove(car)

    @property
    def left_parking_lot_number(self):
        return self.parking_lot_number - len(self.parking_lot)


def test_parking():
    yuanling = YuanlingEightRoad()
    yuanling.parking(cai_car)
    yuanling.parking(gong_car)
    yuanling.parking(cat_car)

def test_left_parking_log_number():
    yuanling = YuanlingEightRoad()
    yuanling.parking(cai_car)
    yuanling.parking(gong_car)
    print(yuanling.left_parking_lot_number)

if __name__ == '__main__':
    cai_car = Car('cai')
    gong_car = Car('gong')
    cat_car = Car('baobao')
    test_left_parking_log_number()
