from user1 import user
from card import card


Roman = user('Roman', 'Ivanov', '24')
Igor = user('Igor', 'Egorov', '19')
Victor = user('Victor', 'Danilov', '47')
card = card('2346 6008 4443 3322', '02/25', 'AlexT')

Roman.sayName()
Roman.sayLastName()
Roman.setAge(25)
Roman.sayAge()
Roman.addCard(card)
Roman.getCard().pay(1000)