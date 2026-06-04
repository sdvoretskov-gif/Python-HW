#Выведите на экран второй и второй с конца элементы через запятую.
# Продумайте такое решение, которое можно было бы применить к списку любой длины.
#employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Wat", "Moana", "Juilet"]
#print(employee_list[1], ',', employee_list[-2])

#def dev_by_three(number):
   # return "Да" if number % 3 == 0 else "Нет"

#num = int(input("Введите число: "))
#result = dev_by_three(num)
#print(f"Делится ли на три {num}? - {result}")

import math

def min_boxes(items):
    return math.ceil(items / 5)

num_items = int(input("Введите количество предметов: "))
print(f"Минимальное количество коробок: {min_boxes(num_items)}")