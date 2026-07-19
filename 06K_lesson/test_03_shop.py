from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')

    driver.add_cookie({
        "name": "session-username",
        "value": "standard_user",
        "domain": "www.saucedemo.com"
    })
    driver.refresh()

    driver.get('https://www.saucedemo.com/inventory.html')

    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', \
        "Не удалось перейти на страницу"

    cart_backpack = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack"))
    )
    cart_backpack.click()

    cart_shirt = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"))
    )
    cart_shirt.click()

    cart_onesie = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie"))
    )
    cart_onesie.click()

    cart = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '.shopping_cart_link'))
    )
    cart.click()

    checkout = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#checkout'))
    )
    checkout.click()

    first_name = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#first-name'))
    )
    first_name.send_keys('Сергей')

    last_name = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#last-name'))
    )
    last_name.send_keys('Дворецков')

    postal_code = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#postal-code'))
    )
    postal_code.send_keys('410010')

    btn_cont = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '#continue'))
    )
    btn_cont.click()

    total_cost = driver.find_element(
        By.CSS_SELECTOR, '.summary_total_label').text

    expected_total = "Total: $58.29"
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.summary_total_label'), expected_total))
    assert total_cost == expected_total, \
        (f"Ошибка! Итоговая сумма не совпадает. "
         f"Ожидалось: {expected_total}, Получено: {total_cost}")
    print("Проверка пройдена: итоговая сумма = $58.29")

    driver.quit()
