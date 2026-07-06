from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/links/10")
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)
    links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
    assert len(links) == 9

    for i, link in enumerate(links):
        assert link.is_displayed()

    first_link_text = links[0].text
    assert "1" in first_link_text.lower()

    driver.quit()
