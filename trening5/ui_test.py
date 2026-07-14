
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_update_user_name():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get('https://gitflic.ru/')

    driver.add_cookie({
        'name': 'SESSION',
        'value': 'YTMzOTkxNjYtZTk3MS00MmZlLThjNTctZDAzZjI0MzVhMzRi',
        'domain': 'gitflic.ru'
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    # Перейти на страницу профиля.
    driver.get('https://gitflic.ru/user/sdvoretskov')
    # Нажать кнопку редактирования профиля.
    edit_button = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'user-profile__edit'))
    )
    edit_button.click()
    # Изменить имя и фамилию в форме.
    username_input = wait.until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    username_input.clear()
    username_input.send_keys('Sergey')

    surname_input = driver.find_element(By.NAME, 'surname')
    surname_input.clear()
    surname_input.send_keys('Dvoretskov')
    # Сохранить изменения.
    save_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".gf-button.--success"))
    )
    save_button.click()
    # Вернуться на страницу профиля.
    driver.get('https://gitflic.ru/user/sdvoretskov')

    user_name = driver.find_element(By.CSS_SELECTOR, "h6.mb-0")
    assert user_name.text == 'Sergey Dvoretskov'
