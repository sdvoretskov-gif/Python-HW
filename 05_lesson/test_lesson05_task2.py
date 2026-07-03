from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/forms/post")
    curent_url = driver.current_url
    driver.maximize_window()

    sleep(5)

    cust_name = driver.find_element(
        By.XPATH, '//input[@name="custname"]')
    cust_name.send_keys('Сергей')
    sleep(3)

    submit_order = driver.find_element(
        By.XPATH, '//button["submit order"]')
    submit_order.click()
    sleep(5)

    expected_url = "https://httpbin.org/post"
    assert curent_url != expected_url

    driver.quit()
