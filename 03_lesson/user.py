class user:

    def __init__(self, first_name, last_name):
        self.firstName = first_name
        self.lastName = last_name

    def sayName(self):
        print('Моё имя ', self.firstName)

    def saylastName(self):
        print('Моя фамилия ', self.lastName)

    def sayNameAndLastName(self):
        print('Мои имя и фамилия ', self.firstName, self.lastName)
