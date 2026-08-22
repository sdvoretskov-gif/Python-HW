from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def set_fields(self):
        user_name = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#user-name")))
        user_name.send_keys('standard_user')

        password = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#password")))
        password.send_keys('secret_sauce')

    def login(self):
        button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        button.click()


class InventoryPage:

    BUTTON_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BUTTON_SHIRT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    BUTTON_ONESIE = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    BUTTON_CART = (By.CSS_SELECTOR, ".shopping_cart_link")
    BUTTON_REMOVE_BACKPACK = (
        By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    BUTTON_REMOVE_SHIRT = (
        By.CSS_SELECTOR, "#remove-sauce-labs-bolt-t-shirt")
    BUTTON_REMOVE_ONESIE = (
        By.CSS_SELECTOR, "#remove-sauce-labs-onesie")
    CART_BADGE = (
        By.CSS_SELECTOR,
        ".shopping_cart_badge"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def add_to_cart(self):
        cart_backpack = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_BACKPACK))
        cart_backpack.click()
        self.wait.until(EC.visibility_of_element_located
                        (self.BUTTON_REMOVE_BACKPACK))

        cart_shirt = self.driver.find_element(*self.BUTTON_SHIRT)
        cart_shirt.click()
        self.wait.until(EC.visibility_of_element_located
                        (self.BUTTON_REMOVE_SHIRT))

        cart_onesie = self.driver.find_element(*self.BUTTON_ONESIE)
        cart_onesie.click()
        self.wait.until(EC.visibility_of_element_located
                        (self.BUTTON_REMOVE_ONESIE))

    def cart_link(self):
        self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE),
            message="Не дождался появления значка корзины с товарами."
        )

        cart_button = self.driver.find_element(*self.BUTTON_CART)
        cart_button.click()


class CartPage:

    CART_ITEM_LABEL = (By.CSS_SELECTOR, ".cart_item .cart_item_label")
    ITEM_NAME_LINK = (
        By.CSS_SELECTOR, ".cart_item .cart_item_label .inventory_item_name")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "#checkout")
    EXPECTED_ITEMS = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self) -> list[str]:
        self.wait.until(EC.visibility_of_element_located(
            self.ITEM_NAME_LINK))

        cart_items_containers = self.driver.find_elements(
            *self.ITEM_NAME_LINK)

        result = []
        for item in cart_items_containers:
            result.append(item.text.strip())
        return result

    def checkout(self):
        button_click = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        button_click.click()


class CheckoutPage:

    FIRST_NAME = (By.CSS_SELECTOR, "#first-name")
    LAST_NAME = (By.CSS_SELECTOR, "#last-name")
    POSTAL_CODE = (By.CSS_SELECTOR, "#postal-code")
    BTN_CONT = (By.CSS_SELECTOR, "#continue")
    TOTAL_COST = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

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
