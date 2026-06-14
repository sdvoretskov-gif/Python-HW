class user:

        def __init__(self, name, last_name, age):
            print("я создался")
            self.username = name
            self.last_name = last_name
            self.age = age

        def sayName(self):
            print("меня зовут ", self.username)

        def sayLastName(self):
            print("Моя фамилия ", self.last_name)

        def sayAge(self):
            print(self.age)

        def setAge(self, newAge):
            self.age = newAge

        def addCard(self, card):
            self.card = card

        def getCard(self):
            return self.card



