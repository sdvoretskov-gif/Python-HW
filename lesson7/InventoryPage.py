from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    
    BUTTON_BACKPACK = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    BUTTON_SHIRT = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt")
    BUTTON_ONESIE = (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie")
    BUTTON_CART = (By.CSS_SELECTOR, ".shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        driver.maximize_window()

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
