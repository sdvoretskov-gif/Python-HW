from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProjectsPage:
    # Локаторы элементов
    NEW_PROJECT_BUTTON = (By.CSS_SELECTOR, ".projects-layout__action-text.mr-1")
    PROJECT_TITLE_INPUT = (By.CSS_SELECTOR, "#projectTitle")
    CREATE_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-sm btn-success float-right']")
    PROJECT_CARDS = (By.CSS_SELECTOR, ".nav-link.d-flex.align-items-center.flex-nowrap.f4.active")
    PROJECT_TITLE_IN_CARD = (By.CSS_SELECTOR, "a[href='/project/sergeyd/asd']")

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://gitflic.ru/project/"
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.url)

    def click_new_project(self):
        self.driver.find_element(*self.NEW_PROJECT_BUTTON).click()

    def create_project(self, project_name):
        # Заполняем название
        title_field = self.wait.until(
            EC.presence_of_element_located(self.PROJECT_TITLE_INPUT)
            )
        title_field.clear()
        title_field.send_keys(project_name)

        # Скроллим и нажимаем создать
        create_btn = self.driver.find_element(*self.CREATE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", create_btn)
        create_btn.click()

    def get_project_names(self):
        # Получаем все карточки проектов
        cards = self.driver.find_elements(*self.PROJECT_CARDS)
        names = []

        for card in cards:
            try:
                # Ищем название внутри карточки
                title_element = card.find_element(*self.PROJECT_TITLE_IN_CARD)
                names.append(title_element.text)
            except:
                continue

        return names
