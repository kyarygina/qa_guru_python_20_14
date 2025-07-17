from selene.support.conditions import have
from selene.support.shared import browser


class BuyRealtyPage:

    def __init__(self):
        self.buy_realty_header = browser.element('h1')

    def should_header_have_text(self, value):
        self.buy_realty_header.should(have.text(value))