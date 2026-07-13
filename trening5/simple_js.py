from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ru.wikipedia.org/wiki/")
wait = WebDriverWait(driver, 10)

driver.save_screenshot("screenshots/full_screen.png")

main_icon = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "mw-logo-icon"))
)
main_icon.screenshot('screenshots/icon_screen.png')

driver.quit()

#title = driver.execute_script('return document.title;')
#url = driver.execute_script('return window.location.href;')

#print(f"Заголовок: {title}")
#print(f"URL: {url}")