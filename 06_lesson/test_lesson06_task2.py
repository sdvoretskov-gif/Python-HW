from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    # Откройте страницу https: // gitflic.ru /.
    driver.get('https://gitflic.ru/')
    # Установите cookie пользователя 1.
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'MGU2NWU3OTMtODQ5Yi00YzkzLTliYmEtODFlNDgxOWUxOWJk',
        'domain': 'gitflic.ru'
    })
    # Обновите страницу.
    driver.refresh()
    # Сохраните текущий URL.
    current_url_user1 = driver.current_url
    # Перейдите на страницу пользователя 1.
    driver.get('https://gitflic.ru/user/sdvoretskov')
    wait.until(EC.title_is('sdvoretskov - Sergey Dvoretskov'))
    # Разлогиньтесь(очистите куки).
    driver.delete_all_cookies()
    # Установите cookie пользователя 2.
    driver.add_cookie({
        'name': 'SESSION',
        'value': 'MGU2NWU3OTMtODQ5Yi00YzkzLTliYmEtODFlNDgxOWUxOWJk',
        'domain': 'gitflic.ru'
    })
    # Обновите страницу.
    driver.refresh()
    # Перейдите на страницу пользователя 2.
    driver.get('https://gitflic.ru/user/sergeyd')
    wait.until(EC.title_is('sergeyd - Sergey D'))
    # Сохраните текущий URL.
    current_url_user2 = driver.current_url
    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert current_url_user1 != current_url_user2
    driver.quit()
