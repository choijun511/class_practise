'''
有停车位的路
'''
import re
from road import Road
from car import Car


class RoadWithParkingLot(Road):

    '''这是一个路的抽象，init时传入名称，长度，宽度，停车位的数量
    Road.parking -> 停车
    Road.leave   -> 开走
    Road.left_parking_lot_number -> 剩余停车位
    '''

    whoami = 'road_with_parking_log'

    def __init__(self, name, length, width, has_starbucks, parking_lot_number):
        super(RoadWithParkingLot, self).__init__(name, length, width, has_starbucks)
        self.parking_lot_number = parking_lot_number
        self.parking_lot = []

    def parking(self, car):
        if len(self.parking_lot) >= self.parking_lot_number:
            raise ValueError('不好意思，%s车位已满' % self.name)
        self.parking_lot.append(car)

    def leave(self, car):
        if car not in self.parking_lot:
            raise ValueError('%s的车不在%s车位内' % (car.owner, self.name))
        self.parking_lot.remove(car)

    @property
    def left_parking_lot_number(self):
        return self.parking_lot_number - len(self.parking_lot)

    @property
    def can_two_way_travle(self):
        return False

    def set_name(self, name):
        if not re.search('一|二|三|四|五|六|七|八|九', name):
            raise ValueError('有停车位的路请用数字命名')
        super(RoadWithParkingLot, self).set_name(name)

    def __repr__(self):
        description = super(RoadWithParkingLot, self).__repr__()
        return description.replace(self.__class__.__name__, self.__class__.__name__ + ':' + self.name)


def test_yuanling():
    yuanling = RoadWithParkingLot('园岭八街', 100, 2, True, 20)
    yuanling.parking(cai_car)
    yuanling.parking(cat_car)
    print(yuanling.left_parking_lot_number)
    print('test yuanling ok')
    yuanling.drink_coffee()


def test_bagualing():
    bagualing = RoadWithParkingLot('八卦岭', 10, 2, False, 0)
    bagualing.drink_coffee()
    print('Can I turn around? %s' % bagualing.can_two_way_travle)
    # bagualing.parking(cai_car)
    print(bagualing.left_parking_lot_number)
    print('test bagualing ok')


def test_repr():
    yuanling = RoadWithParkingLot('园岭八街', 100, 2, True, 20)
    print(yuanling)
    print(cai_car)


def test_set_name():
    yuanling = RoadWithParkingLot('园岭八街', 100, 2, True, 20)
    # yuanling.set_name('园岭哈哈哈哈')
    print(yuanling)
    super(RoadWithParkingLot, yuanling).set_name('园岭哈哈哈哈')
    print('after set name')
    print(yuanling)


if __name__ == '__main__':
    cai_car = Car('cai')
    gong_car = Car('gong')
    cat_car = Car('baobao')
    # test_yuanling()
    # test_repr()
    # test_bagualing()
    test_set_name()
