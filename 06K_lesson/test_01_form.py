from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shape_completion():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    driver.get(
        'https://bonigarcia.dev/selenium-webdriver-java/data-types.html')
    wait.until(EC.title_is('Hands-On Selenium WebDriver with Java'))

    first_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='first-name']"))
    )
    first_name.send_keys('Иван')

    last_name = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='last-name']"))
    )
    last_name.send_keys('Петров')

    address = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='address']"))
    )
    address.send_keys('Ленина, 55-3')

    email = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='e-mail']"))
    )
    email.send_keys('test@skypro.com')

    phone_number = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='phone']"))
    )
    phone_number.send_keys('+7985899998787')

    zip_code = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='zip-code']"))
    )
    zip_code.send_keys()
    zip_code.clear()

    city = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='city']"))
    )
    city.send_keys('Москва')

    country = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='country']"))
    )
    country.send_keys('Россия')

    job_position = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='job-position']"))
    )
    job_position.send_keys('QA')

    company = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "input[name='company']"))
    )
    company.send_keys('SkyPro')

    submit = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit.click()

    red_field = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )
    assert red_field.is_displayed(), "Поле должно иметь класс .alert-danger"

    success_elements = driver.find_elements(By.CSS_SELECTOR, ".alert-success")

    elements_to_check = [first_name, last_name, address, email, phone_number,
                         zip_code, city, country, job_position, company]

    elements_to_check = success_elements

    for element in elements_to_check:
        class_string = element.get_attribute("class")

        assert "alert-success" in class_string, \
            (f"Элемент {element} не содержит 'alert-success'."
             f" Текущие классы: '{class_string}'")

    driver.quit()
