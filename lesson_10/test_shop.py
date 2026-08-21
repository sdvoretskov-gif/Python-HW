import pytest
from selenium import webdriver
from lesson_10.shop_page import (LoginPage,
                                 InventoryPage, CartPage, CheckoutPage)
import allure


@pytest.fixture(scope="function")
def driver():
    d = webdriver.Firefox()
    d.maximize_window()
    yield d
    d.quit()


@allure.epic("Магазин")
@allure.feature("Полный цикл от логирования до покупки товара")
@allure.story("Логирование, выбор товара, просмотр корзины, покупка")
@allure.title("Покупка товаров")
@allure.description("Тест описывает полный цикл от логирования "
                    "до покупки товаров "
                    "на сайте интернет-магазина https://www.saucedemo.com/")
@allure.severity("Critical")
def test_full_checkout_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    with allure.step(
            "открывает страницу ввода логина и пароля в браузере Firefoxe"):
        login_page.open()
    with allure.step(
            "вводит в поля user_name и password, данные пользователя"):
        login_page.set_fields()
    with allure.step("нажимает кнопку логирования"):
        login_page.login()

    with allure.step("добавляет в корзину товары"):
        inventory_page.add_to_cart()
    with allure.step("нажимает на значок корзины"):
        inventory_page.cart_link()

    with allure.step(
            "проверяет товары в корзине сравнивая имеющиеся с ожидаемыми"):
        actual_items = CartPage.get_cart_items(self=cart_page)
        assert sorted(actual_items) == sorted(CartPage.EXPECTED_ITEMS), \
            (f"Товары в корзине не совпадают!"
             f"\nОжидалось:\n{CartPage.EXPECTED_ITEMS}"
             f"\nПолучено:\n{actual_items}")

    with allure.step("нажимает на кнопку Checkout"):
        cart_page.checkout()
    with allure.step("заполняет поля данными покупателя"):
        checkout_page.fill_fields()
    with allure.step("нажимает кнопку продолжить оформление покупки"):
        checkout_page.btn_cont()

    expected_total = "Total: $58.29"
    actual_total = checkout_page.total_cost()

    with allure.step("сравнивает итоговую сумму покупки  с ожидаемой"):
        assert actual_total == expected_total, \
            (f"Ошибка! Итоговая сумма не совпадает."
             f"\nОжидалось: {expected_total}, получено: '{actual_total}'")
    print("Проверка пройдена!")
