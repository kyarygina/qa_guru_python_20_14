import allure
from selene.support.conditions import have
from selene.support.shared import browser


class MortgageQuestionsPage:

    def __init__(self):
        self.mortgage_questions_header = browser.element('.PageFork_text__ItTq5')

    @allure.step("Проверить наличие текста в заголовке")
    def should_header_have_text(self, value):
        self.mortgage_questions_header.should(have.text(value))