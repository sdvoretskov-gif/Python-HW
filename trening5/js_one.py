
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://ru.wikipedia.org/wiki/')


driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(3)

button_link = driver.find_element(
    By.XPATH, '//a[contains(text(),"Свяжитесь с нами")]')

print(button_link.get_attribute('href'))
print(button_link.text)

button_link.click()
sleep(3)

driver.quit()