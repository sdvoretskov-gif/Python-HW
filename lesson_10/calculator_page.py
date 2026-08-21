from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Калькулятор")
class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)
        driver.maximize_window()

    def open(self):
        """
        Этот метод открывает страницу калькулятора
         в браузере Google Chrome
        :return:
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def delay_input(self):
        """
        Этот метод устанавливает задержку в вычислениях калькулятора
        :return:
        """
        delay_field = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#delay')))
        delay_field.clear()
        delay_field.send_keys('45')
        delay_field.send_keys(Keys.TAB)

    def buttons(self):
        """
        Нажимает  кнопки калькулятора переданные в списке данного метода
        :return:
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    def get_result(self):
        """
        Этот метод возвращает результат вычислений
        :return: int
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), '15')
        )
        result_element = self.driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text
