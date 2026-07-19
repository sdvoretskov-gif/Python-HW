from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shape_completion():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 50)
    driver.maximize_window()

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')

    input_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#delay'))
    )
    input_field.clear()
    input_field.send_keys('45')

    buttons = ["7", "+", "8", "="]
    for button in buttons:
        xpath = f"//span[text()='{button}']"
        driver.find_element(By.XPATH, xpath).click()

    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    assert result

    driver.quit()
