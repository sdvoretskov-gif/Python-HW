from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    BUTTON_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BUTTON_SHIRT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    BUTTON_ONESIE = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    BUTTON_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "#checkout")
    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    BTN_CONT = (By.CSS_SELECTOR, "#continue")
    TOTAL_COST = (By.CSS_SELECTOR, ".summary_total_label")

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

    def add_to_cart(self):
        cart_backpack = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_BACKPACK))
        cart_backpack.click()

        cart_shirt = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_SHIRT))
        cart_shirt.click()

        cart_onesie = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_ONESIE))
        cart_onesie.click()

    def cart_link(self):
        cart = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CART))
        cart.click()

    def checkout(self):
        button_click = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        button_click.click()

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
        assert ShopPage.total_cost(self) == expected_total, \
            (f"Ошибка! Итоговая сумма не совпадает. "
             f"Ожидалось: {expected_total}, "
             f"Получено: {ShopPage.total_cost(self)}")
        print("Проверка пройдена: итоговая сумма = $58.29")
