from time import  sleep
from playwright.sync_api import Page, expect


def test_yougile_login(page: Page):
    # Открыть страницу авторизации: https://ru.yougile.com/team/
    page.goto('https://ru.yougile.com/team/')

    #Ввести в поле «Email» логин: sdvoretskov@inbox.ru [autocomplete="email"]
    page.locator('[autocomplete="email"]').fill('sdvoretskov@inbox.ru')

    # Ввести в поле «Пароль» пароль: ASD_asd333 [autocomplete="current-password"]
    page.locator("[autocomplete='current-password']").fill('ASD_asd333')

    # Нажать кнопку «Войти» .bg-action-default[role="button"]
    page.locator(".bg-action-default[role='button']").click()
    sleep(10)
    page.goto('https://ru.yougile.com/team/settings-account')
    # Пользователь перенаправлен на главную страницу YouGile
    sleep(10)
    user_name = page.locator('[placeholder="Отображаемое имя…"]')

    expect(user_name).to_be_visible()
    expect(user_name).to_have_value("Сергей Д")










#Название: успешная авторизация пользователя.

#Предусловия: пользователь зарегистрирован в системе.

#Шаги





#Ожидаемый результат


#Отображается интерфейс рабочего пространства
# имя пользователя [placeholder="Отображаемое имя…"] Сергей Д