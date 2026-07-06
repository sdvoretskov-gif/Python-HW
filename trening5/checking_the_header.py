from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_page_title():
    driver = webdriver.Chrome()
    driver.get('https://httpbin.org/')
    driver.maximize_window()
    sleep(5)

    test_title = driver.find_element(By.CLASS_NAME, "title")
    print(test_title.text)

    driver.quit()

       # title = driver.find_element(By.TAG_NAME, "h1")
        #assert "httpbin" in title.text.lower()

        #driver.quit()



