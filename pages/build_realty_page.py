from selene.support.conditions import have
from selene.support.shared import browser


class BuildRealtyPage:

    def __init__(self):
        self.build_realty_header = browser.element('h1')

    def should_header_have_text(self, value):
        self.build_realty_header.should(have.text(value))