from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_selection_state_to_be


def test_yougile_login():
    driver = webdriver.Chrome()
# Открыть страницу авторизации: https://ru.yougile.com/team/
    driver.get('https://ru.yougile.com/team/')
    driver.maximize_window()
    sleep(7)
#Ввести в поле «Email» логин: sdvoretskov@inbox.ru [autocomplete="email"]
    driver.find_element(
        By.CSS_SELECTOR, '[autocomplete="email"]').send_keys(
        'sdvoretskov@inbox.ru')
    sleep(9)
# Ввести в поле «Пароль» пароль: ASD_asd333 [autocomplete="current-password"]
    driver.find_element(
        By.CSS_SELECTOR, "[autocomplete='current-password']").send_keys(
        'ASD_asd333')
    sleep(9)
# Нажать кнопку «Войти» .bg-action-default[role="button"]
    driver.find_element(
        By.CSS_SELECTOR, ".bg-action-default[role='button']").click()
    sleep(9)
    driver.get('https://ru.yougile.com/team/settings-account')
    sleep(9)
# Пользователь перенаправлен на главную страницу YouGile
    user_name = driver.find_element(
        By.CSS_SELECTOR, '[placeholder="Отображаемое имя…"]')
    assert user_name.is_displayed()
    assert user_name.get_attribute("value") == "Сергей Д"

    driver.quit()









#Название: успешная авторизация пользователя.

#Предусловия: пользователь зарегистрирован в системе.

#Шаги





#Ожидаемый результат


#Отображается интерфейс рабочего пространства
# имя пользователя [placeholder="Отображаемое имя…"] Сергей Д