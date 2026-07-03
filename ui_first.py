import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(10)
driver.get("https://www.google.com")
#driver.get("https://yozhka.lukit.ru")

print(driver.title)
print(driver.current_url)

driver.refresh()

time.sleep(10)
driver.quit()

#driver.get(url) Открыть страницу
#driver.refresh() Обновить страницу
#driver.back() Вернуться назад
#driver.forward() Перейти вперед***

#driver.maximize_window() Развернуть окно на весь экран
#driver.minimize_window() Свернуть окно
#driver.set_window_size(width, height) Установить размер окна

#driver.title Получить заголовок страницы
#driver.current_url Получить текущий URL
#driver.page_source Получить HTML-код страницы

#driver.save_screenshot(path) Сохранить скриншот страницы

#driver.quit() Закрыть браузер и завершить сессию
#driver.close() Закрыть текущую вкладку