import pytest
from selenium import webdriver
from lesson_10.calculator_page import CalculatorPage
import allure


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Калькулятор")
@allure.feature("Сложение")
@allure.story("Операция сложения целых чисел")
@allure.title("Сложение целых чисел")
@allure.description("Пример сложения целых чисел в калькуляторе"
                    "на страничке https://bonigarcia")
@allure.severity("Critical")
def test_calculator(driver):
    calc_page = CalculatorPage(driver)
    with allure.step(
            "открывает страницу калькулятора в браузере Google Chrome"):
        calc_page.open()
    with allure.step(
            "устанавливает задержку в вычислениях калькулятора"):
        calc_page.delay_input()
    with allure.step(
            "Нажимает кнопки калькулятора переданные в списке данного метода"):
        calc_page.buttons()
    with allure.step("возвращает результат вычислений"):
        calc_page.get_result()
    with allure.step("Сравнивает полученный результат с ожидаемым"):
        assert calc_page.get_result() == "15"
