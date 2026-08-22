import pytest
from selenium import webdriver
from lesson_07.pages.shop_page import (LoginPage,
                                       InventoryPage, CartPage, CheckoutPage)


@pytest.fixture(scope="function")
def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    yield d
    d.quit()


def test_full_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    login_page.open()
    login_page.set_fields()
    login_page.login()

    inventory_page.add_to_cart()
    inventory_page.cart_link()

    actual_items = CartPage.get_cart_items(self=cart_page)
    assert sorted(actual_items) == sorted(CartPage.EXPECTED_ITEMS), \
        (f"Товары в корзине не совпадают!"
         f"\nОжидалось:\n{CartPage.EXPECTED_ITEMS}"
         f"\nПолучено:\n{actual_items}")

    cart_page.checkout()
    checkout_page.fill_fields()
    checkout_page.btn_cont()

    expected_total = "Total: $58.29"
    actual_total = checkout_page.total_cost()
    assert actual_total == expected_total, \
           (f"Ошибка! Итоговая сумма не совпадает."
            f"\nОжидалось: {expected_total}, получено: '{actual_total}'")
    print("Проверка пройдена!")
