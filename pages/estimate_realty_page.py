from selene.support.conditions import have
from selene.support.shared import browser


class EstimateRealtyPage:

    def __init__(self):
        self.estimate_realty_header = browser.element('h1')

    def should_header_have_text(self, value):
        self.estimate_realty_header.should(have.text(value))