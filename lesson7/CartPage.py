from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    BUTTON_INVENTORY = (By.CSS_SELECTOR, '#inventory_item_name')
    ITEM_IN_CART = (
        By.CSS_SELECTOR,"#add-to-cart-sauce-labs-backpack",
        "#add-to-cart-sauce-labs-bolt-t-shirt",
        "#add-to-cart-sauce-labs-onesie")
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, "#checkout")
    EXPECTED_CART_ITEMS = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        driver.maximize_window()

    def get_cart_items(self) -> list[str]:
        self.wait.until(EC.visibility_of_element_located(self.BUTTON_INVENTORY))
        cart_items_containers = self.driver.find_elements(*self.BUTTON_INVENTORY)

        result = []
        for item_container in cart_items_containers:
            name_element = item_container.find_element(*self.ITEM_IN_CART)
            result.append(name_element.text.strip())

        return result

    def test_cart_contents(self):
        actual_cart_items = self.get_cart_items()

    def checkout(self):
        button_click = self.wait.until(
            EC.element_to_be_clickable(self.BUTTON_CHECKOUT))
        button_click.click()
