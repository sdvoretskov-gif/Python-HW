class card:
    number = '0000 0000 0000 0000'
    validDate = '03/27'
    holder = 'unknow'

    def __init__(self, number, date, holder):
        self.number = number
        self.validDate = date
        self.holder = holder

    def pay(self, amount):
        print('с карты', self.number, 'списали', amount)