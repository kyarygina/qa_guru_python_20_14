import allure
from selene.support.conditions import have
from selene.support.shared import browser


class OwnerAuthenticationPage:

    def __init__(self):
        self.owner_authentication_header = browser.element('h3')

    @allure.step("Проверить наличие текста в заголовке")
    def should_header_have_text(self, value):
        self.owner_authentication_header.should(have.text(value))