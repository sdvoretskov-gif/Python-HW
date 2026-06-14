class address:
    index = '000000'
    city = 'unknow'
    street = 'unknow'
    house = 'unknow'
    apartment = 'unknow'

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
