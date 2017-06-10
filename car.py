'''
车
'''

class Car(object):

    def __init__(self, owner):
        self.owner = owner

    def __repr__(self):
        description = super(Car, self).__repr__()
        return description.replace(self.__class__.__name__, self.__class__.__name__ + ' driven by ' + self.owner)


def public(a, b):
    print(a, b)

def _half_private(a, b):
    '''
    import * can't import
    '''
    print(a, b)


def __private(a, b):
    '''
    目前没看出差别来
    '''
    print(a, b)
