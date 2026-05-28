#Выведите на экран второй и второй с конца элементы через запятую.
# Продумайте такое решение, которое можно было бы применить к списку любой длины.
#employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Wat", "Moana", "Juilet"]
#for l in range (0, len(employee_list)):
 #   print(employee_list[1],',', employee_list[-2])

#employee_list = ["John Snow", "Piter Pen",
 #                "Drakula", "IvanIV", "Moana", "Juilet"]

#print(employee_list[1] + ", " + employee_list[-2])

dev_by_three = input('Введите число: ')
if (int(dev_by_three) % 3 == 0):
    print('Делется ли на три ', dev_by_three, '?', '-', 'Да')
else:
    print('Делется ли на три ', dev_by_three, '?', '-', 'Нет')



def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"

num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")
