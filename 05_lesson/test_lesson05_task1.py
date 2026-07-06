from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_to_be


def test_navigation():
    driver = webdriver.Chrome()
    initial_url = driver.current_url
    print(f"Начальный URL: {initial_url}")
    driver.get('https://httpbin.org/')
    driver.maximize_window()
    sleep(5)

    driver.find_element(
        By.CSS_SELECTOR, 'a[href = "/forms/post"]').click()
    assert url_to_be('https://httpbin.org/forms/post')
    sleep(5)

    driver.get('https://httpbin.org/')
    assert initial_url
    sleep(5)

    driver.quit()
