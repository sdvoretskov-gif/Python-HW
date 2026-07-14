from time import  sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://gitflic.ru/')

driver.add_cookie({
    'name': 'SESSION',
    'value': 'YTMzOTkxNjYtZTk3MS00MmZlLThjNTctZDAzZjI0MzVhMzRi',
    'domain': 'gitflic.ru'
})

driver.add_cookie({
    'name': 'cookiesAccepted',
    'value': 'true',
    'domain': 'gitflic.ru'
})

driver.refresh()
driver.get('https://gitflic.ru/user/sdvoretskov')

sleep(5)

driver.delete_all_cookies()
driver.refresh()
sleep(5)

driver.quit()
#cookies = driver.get_cookies()

#for cookie in cookies:
 #   print(f"{cookie['name']}: {cookie['value']}")

#driver.quit()