from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    # 2. Найдите и нажмите на кнопку "Start"
    click_start = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[id="start"] button')
        )
    )
    click_start.click()
    # 3. Дождитесь появления текста "Hello World!"
    new_text = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div[id="finish"] h4')
        )
    )
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/full_page_after.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    assert new_text.text == 'Hello World!'
    driver.quit()
