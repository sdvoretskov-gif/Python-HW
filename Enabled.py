from gc import enable
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/disabledinput')
driver.maximize_window()
sleep(5)

driver.find_element(By.ID, 'enableButton').click()
sleep(3)

input_element = driver.find_element(By.ID, 'inputField')

if input_element.is_enabled():
    print('input elements is enable')
else:
    print('input elements is blocked')

driver.quit()