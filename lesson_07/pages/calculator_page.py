from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        driver.maximize_window()

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def delay_input(self):
        delay_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#delay')))
        delay_field.clear()
        delay_field.send_keys('45')

    def buttons(self):
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self):
        screen = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        return screen.text.strip()
