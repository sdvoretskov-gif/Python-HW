import pytest
from selenium import webdriver
from lesson_07.pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calc_page = CalculatorPage(driver)
    calc_page.open()
    calc_page.delay_input()
    calc_page.buttons()
    calc_page.get_result()
    assert calc_page.get_result() == "15"
