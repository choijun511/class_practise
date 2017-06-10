'''
对路的抽象
'''

class Road(object):

    whoami = 'road'

    def __init__(self, name, length, width, has_starbucks):
        self.name = name
        self.length = length
        self.width = width
        self.has_starbucks = has_starbucks

    def drink_coffee(self):
        if self.has_starbucks:
            print('yes, you can')
            return True
        else:
            print('no, there no starbucks, go another road')
            return False

    @property
    def can_two_way_travle(self):
        return True

    def __doc__(self):
        return '''这是一个路的抽象，init时传入名称，长度，宽度
        '''


def test_road():
    bagualing = Road('八卦岭', 100, 10, False)
    print('Can I drink coffee? %s' % bagualing.drink_coffee())
    print('Can I turn around? %s' % bagualing.can_two_way_travle)

    yuanling = Road('园岭八街', 100, 10, True)
    print('Can I drink coffee? %s' % yuanling.drink_coffee())

if __name__ == '__main__':
    test_road()
