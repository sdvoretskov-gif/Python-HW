from smartphone import smartphone

catalog = [
    smartphone('Nokia', '3310', '+79271800019'),
    smartphone('Sony Ericsson', 'w700i', '+79054005062'),
    smartphone('Honor', '90 lite', '+79874457845'),
    smartphone('Iphone', '14', '+79012564555'),
    smartphone('Samsung', 'Galaxy A05', '+79805000106')
]

for smartphone in catalog:
    print(f'Устройство абонента: {smartphone.stamp} {smartphone.model} контакт: {smartphone.subscriberNumber}')