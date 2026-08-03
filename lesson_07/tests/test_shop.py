import pytest
from selenium import webdriver
from lesson_07.pages.shop_page import ShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.set_fields()
    shop_page.login()
    shop_page.add_to_cart()
    shop_page.cart_link()
    shop_page.checkout()
    shop_page.fill_fields()
    shop_page.btn_cont()
    shop_page.total_cost()
    shop_page.final_check()
