from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        driver.maximize_window()


    def open(self):
        self.driver.get(
            "https://www.saucedemo.com/"
        )
        self.driver.add_cookie({
            "name": "session-username",
            "value": "standard_user",
            "domain": "www.saucedemo.com"
        })


    def set_fields(self):
        btn_user_name = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
        btn_user_name.send_keys('standard_user')

        btn_password = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
        btn_password.send_keys('secret_sauce')


    def login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
