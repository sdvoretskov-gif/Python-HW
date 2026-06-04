def is_year_leap(year):
    return 'True' if year % 4 == 0 else 'False'


request = int(input('Введите год в формате - ГГГГ: '))
result = is_year_leap(request)
print(f'Год {request} - {result}')
