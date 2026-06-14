from address import address
from Mailing import mailing

to_address = address('119007', 'Moscow', 'Lavrushinsky Lane', '10', '1')
from_address = address('410042', 'Saratov', 'Moskovskaya Street', '72', '2')
mailing_1 = mailing('119007, Moscow, Lavrushinsky Lane, 10 - 1', '410042, Saratov, Moskovskaya Street, 72 - 2', '130', '11977654890004')

print(mailing_1)
#Отправление <track> из <индекс>, <город>, <улица>, <дом> - <квартира> в <индекс>, <город>, <улица>, <дом> -<квартира>. Стоимость <стоимость> рублей.
