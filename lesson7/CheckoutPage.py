from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    BTN_CONT = (By.CSS_SELECTOR, "#continue")
    TOTAL_COST = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        driver.maximize_window()

    def fill_fields(self):
        first_name = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME))
        first_name.send_keys('Сергей')

        last_name = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME))
        last_name.send_keys('Дворецков')

        postal_code = self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE))
        postal_code.send_keys('410010')

    def btn_cont(self):
        btn_cont = self.wait.until(
            EC.element_to_be_clickable(self.BTN_CONT)
        )
        btn_cont.click()

    def total_cost(self):
        total = self.wait.until(
            EC.presence_of_element_located(self.TOTAL_COST))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", total)
        return total.text.strip()

    def final_check(self):
        expected_total = "Total: $58.29"
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, '.summary_total_label'), expected_total))
