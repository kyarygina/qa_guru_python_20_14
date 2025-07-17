import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def open_browser():
    browser.config.base_url = 'https://www.cian.ru'
    browser.open('/')
    browser.driver.maximize_window()
    browser.driver.delete_all_cookies()

    yield

    browser.quit()
