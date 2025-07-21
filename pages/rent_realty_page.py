import allure
from selene.support.conditions import have
from selene.support.shared import browser


class RentRealtyPage:

    def __init__(self):
        self.rent_realty_header = browser.element('h1')

    @allure.step("Проверить наличие текста в заголовке")
    def should_header_have_text(self, value):
        self.rent_realty_header.should(have.text(value))