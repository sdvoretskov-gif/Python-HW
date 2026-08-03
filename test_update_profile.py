import faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_profile_page(driver):
   driver.get("https://gitflic.ru/user/airsworld")
   driver.save_screenshot("screenshots/full_page.png")


def update_profile(driver, wait, new_user_name, new_last_name):
   edit_button = wait.until(EC.presence_of_element_located(
       (By.CLASS_NAME, "user-profile__edit")
   ))
   edit_button.click()
   username_input = wait.until(EC.presence_of_element_located(
      (By.ID, "name")
   ))
   username_input.clear()
   username_input.send_keys(new_user_name)

   surname_input = driver.find_element(By.ID, "surname")
   surname_input.clear()
   surname_input.send_keys(new_last_name)

   save_button = wait.until(EC.presence_of_element_located(
       (By.CSS_SELECTOR, ".gf-button.--success")
   ))
   save_button.click()


def get_user_name(wait):
   user_name = wait.until(EC.presence_of_element_located(
      (By.CSS_SELECTOR, "h6.mb-0")
   ))
   user_name.screenshot("screenshots/user_name.png")
   return user_name.text
