def month_to_season(mn):
    if 1 <= mn <= 2:
        return 'Это Зима'
    if 3 <= mn <= 5:
        return 'Это Весна'
    if 6 <= mn <= 8:
        return 'Это Лето'
    if 9 <= mn <= 11:
        return 'Это Осень'
    if mn == 12:
        return 'Это Зима'
    return 'Нет такого месяца в году'


request = int(input('Веведите номер месяца в году(1-12): '))
print(month_to_season(request))
