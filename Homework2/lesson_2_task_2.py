rate = input("Оцените работу оператора от 1 до 5 ")
rate = int(rate)
if rate < 1:
    rate = 1
if rate > 5:
    rate = 5

feedback = ""
if rate == 1:
    feedback = input("Все так плохо?")
elif rate == 2:
     feedback = input("Что именно Вам не понравилось")
elif rate == 3:
    feedback = input("Что по Вашему мнению нужно изменить")
elif rate == 4:
    feedback = input("Посоветуете ли наш сервис друзьям?")
else:
     feedback = input("Мы рады быть полезными Вам")
print(feedback)



