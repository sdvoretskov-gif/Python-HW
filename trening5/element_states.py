from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://demoqa.com/radio-button')
driver.maximize_window()
sleep(5)

input_element = driver.find_element(By.ID, 'yesRadio')
sleep(3)

if input_element.is_enabled():
    print('input elements is enable')
else:
    print('input elements is blocked')

driver.quit()