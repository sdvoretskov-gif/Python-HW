import math


request = float(input('Введете длинну стороны квадрата: '))


def square(sm):
    sum = math.ceil(sm ** 2)
    return sum


result = square(request)
print('Площадь квадрата равна  ', result)
