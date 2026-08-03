import pytest
from driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption(
        "--selenium_browser",
        action="store",
        default="chrome",
        help="выберите браузер для тестов: chrome, firefox, safari, edge"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск в headless режиме (без UI)"
    )

@pytest.fixture(scope="session")
def driver(request):
   browser_name = request.config.getoption("--selenium_browser")
   headless_mode = request.config.getoption("--headless")

   driver = create_driver(browser_name, headless_mode)

   if not headless_mode:
       driver.maximize_window()

   driver.get("https://gitflic.ru/")
   driver.add_cookie({
      "name": "SESSION",
      "value": "MzkwNjRhOGMtM2UxNi00OTU5LWFmMGYtMmM3N2NjMTlmMTlm",
      "domain": "gitflic.ru"
   })
   driver.add_cookie({
       "name": "cookiesAccepted",
       "value": "true",
       "domain": "gitflic.ru"
   })
   driver.refresh()
   yield driver
   driver.quit()

#def pytest_addoption(parser):
 #  parser.addoption(
  #     "--selenium-browser",
   #    action="store",
    #   default="chrome",
     #  help="Выберите браузер для тестов: chrome, firefox, safari, edge"
   #)