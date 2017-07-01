class hotel(object):
    'hotel room rate calculator'

    def __init__(self, rt, sales = 0.085, rm = 0.1):
        '''default argumets:
        sales tax = 8.5% and room tax = 10%'''

        self.RoomRate = rt
        self.SalesTax = sales
        self.RoomTax = rm

    def CalcTotal(self, days = 1):
        daily = round((self.RoomRate * (1 + self.SalesTax + self.RoomTax)),2)
        return days * daily

    if __name__ == '__main__':
        choi = hotel(299)
        choi.CalcTotal()
        choi.CalcTotal(2)
        gong = hotel(199 , 0.09, 0.2)
        gong.CalcTotal(3)
