from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://gitflic.ru')
driver.maximize_window()
driver.find_element(By.CLASS_NAME, "cookiesBtn").click()
sleep(2)

click_button = driver.find_element(By.CLASS_NAME, 'button-start')
click_button.click()

sleep(2)

input_login = driver.find_element(By.ID, 'email')
input_login.send_keys('sdvoretskov@inbox.ru')

input_password = driver.find_element(By.ID, 'passwordBasic')
input_password.send_keys('uW5..Zd9w6MnPBR')

sleep(2)

submit_button = driver.find_element(By.CLASS_NAME, 'btn-success')
submit_button.click()

sleep(5)

user_name = driver.find_element(By.CLASS_NAME, 'profile-page__profile-name')
print(user_name.text)

search_input = driver.find_element(By.CSS_SELECTOR, 'input.gf-custom-search__input')

print(search_input.get_attribute('placeholder'))

driver.quit()
#id="username" placeholder="Логин"
#id="password" placeholder="Пароль"
#логин sdvoretskov
#пароль uW5..Zd9w6MnPBR