import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from utils import attach


@pytest.fixture(scope="function", autouse=True)
##def setup_browser():
    ##browser.config.base_url = 'https://www.cian.ru'
   ## browser.config.timeout = 10
    ##with allure.step("Открыть главную страницу ЦИАН"):
     ##   browser.open('/')
     ##   browser.driver.delete_all_cookies()
      ##  browser.driver.maximize_window()

  ##  yield

  ##  browser.quit()
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = "https://www.cian.ru"

    with allure.step("Открыть главную страницу ЦИАН"):
        browser.open('/')

    browser.driver.delete_all_cookies()
    browser.driver.maximize_window()
    browser.config.timeout = 20

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
