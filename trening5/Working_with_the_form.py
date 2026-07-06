from time import sleep
from  selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_interaction():
    driver = webdriver.Chrome()
    driver.get('https://httpbin.org/forms/post')
    driver.maximize_window()
    sleep(10)

    cusName = driver.find_element(By.CSS_SELECTOR, "input[name='custname']")
    cusName.send_keys("Иван Иванов")
    sleep(5)

    submit_button = driver.find_element(
        By.XPATH, "//button[normalize-space()='Submit order']")
    submit_button.click()

    driver.quit()

    # //button[normalize-space()='Submit order']
    #[name="custname"]