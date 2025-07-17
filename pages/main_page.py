from selene import browser
from selene.support.conditions import have


class MainPage:

    def __init__(self):
        # Кнопка "Найти"
        self.filters_search_button = browser.all('a').element_by(have.text('Найти'))

        # Вкладка "Купить"
        self.buy_realty_type_dropdown = browser.element('button[title="Квартиру в новостройке и вторичке"]')
        self.buy_realty_house_checkbox = browser.all('span').element_by(have.text('Дом, дача'))
        self.buy_realty_price_dropdown = browser.all('button').element_by(have.text('Цена'))
        self.buy_realty_price_from_input = browser.element('input[placeholder="от"]')
        self.buy_realty_price_to_input = browser.element('input[placeholder="до"]')
        self.buy_realty_location_input = browser.element('input[placeholder="Город, адрес, метро, район, ж/д или шоссе"]')
        self.buy_realty_location = browser.element('[title="Сочи, Краснодарский край"]')

        # Вкладка "Снять"
        self.rent_realty_tab = browser.all('a').element_by(have.text('Снять'))
        self.rent_realty_price_dropdown = browser.all('button').element_by(have.text('Цена'))
        self.rent_realty_price_from_input = browser.element('input[placeholder="от"]')
        self.rent_realty_price_to_input = browser.element('input[placeholder="до"]')
        self.rent_realty_location_input = browser.element('input[placeholder="Город, адрес, метро, район, ж/д, шоссе или ЖК"]')
        self.rent_realty_location = browser.element('span[title="Краснодар"]')

        # Вкладка "Посуточно"
        self.daily_rent_realty_tab = browser.all('a').element_by(have.text('Посуточно'))
        self.daily_rent_location_input = browser.element('input[placeholder="Куда вы хотите поехать?"]')
        self.daily_rent_realty_location = browser.element('span[title="Калининград"]')
        self.daily_rent_calendar_button = browser.all('button[data-name="FilterButton"]').element_by(have.text('Заезд — Отъезд'))
        self.daily_rent_body = browser.element('body')

        # Вкладка "Построить"
        self.build_realty_tab = browser.all('a').element_by(have.text('Построить'))

        # Вкладка "Оценить"
        self.estimate_realty_tab = browser.all('a').element_by(have.text('Оценить'))

        # Вкладка "Ипотека"
        self.mortgage_realty_tab = browser.all('ul[data-name="FiltersTabs"] a').element_by(have.text('Ипотека'))
        self.mortgage_realty_type_dropdown = browser.all('button').element_by(have.text('Квартира во вторичке'))
        self.mortgage_realty_newbuilding_checkbox = browser.all('button').element_by(have.text('Квартира в новостройке'))
        self.mortgage_realty_price = browser.element('input[placeholder="Стоимость недвижимости"]')
        self.mortgage_realty_down_payment = browser.element('input[placeholder="Первоначальный взнос"]')
        self.mortgage_realty_term = browser.all('button').element_by(have.text('Срок'))
        self.mortgage_realty_term_from_list = browser.all('button').element_by(have.text('20 лет'))
        self.mortgage_realty_location_input = browser.element('input[placeholder="Город"]')
        self.mortgage_realty_location = browser.all('span').element_by(have.text('Саратов'))
        self.mortgage_realty_right_button = browser.element('[data-mark="FiltersMortgageRightButton"]')

        # Вкладка "Подбор риелтора"
        self.realtor_realty_tab = browser.all('a').element_by(have.text('Подбор риелтора'))
        self.realtor_question_tab = browser.element('div[data-name="CPDModalContainer"] span')

        # Вкладка "Подать за 0 ₽"
        self.zero_ruble_sell_realty_tab = browser.all('a').element_by(have.text('Подать за 0 ₽'))

    # Методы для вкладки "Купить"
    def click_buy_realty_type_dropdown(self):
        self.buy_realty_type_dropdown.click()
        return self

    def click_house_checkbox(self):
        self.buy_realty_house_checkbox.click()
        return self

    def click_buy_realty_price_dropdown(self):
        self.buy_realty_price_dropdown.click()
        return self

    def fill_buy_realty_price_from_input(self, value):
        self.buy_realty_price_from_input.set_value(value)
        return self

    def fill_buy_realty_price_to_input(self, value):
        self.buy_realty_price_from_input.set_value(value)
        return self

    def fill_buy_realty_location_input(self, value):
        self.buy_realty_location_input.set_value(value)
        return self

    def click_buy_realty_location(self):
        self.buy_realty_location.click()
        return self

    def click_filters_search_button(self):
        self.filters_search_button.click()
        return self

    # Методы для вкладки "Снять"
    def click_rent_realty_tab(self):
        self.rent_realty_tab.click()
        return self

    def click_rent_realty_price_dropdown(self):
        self.rent_realty_price_dropdown.click()
        return self

    def fill_rent_realty_price_from_input(self, value):
        self.rent_realty_price_from_input.set_value(value)
        return self

    def fill_rent_realty_price_to_input(self, value):
        self.rent_realty_price_to_input.set_value(value)
        return self

    def fill_rent_realty_location_input(self, value):
        self.rent_realty_location_input.set_value(value)
        return self

    def click_rent_realty_location(self):
        self.rent_realty_location.click()
        return self

    # Методы для вкладки "Посуточно"
    def click_daily_rent_realty_tab(self):
        self.daily_rent_realty_tab.click()
        return self

    def fill_daily_rent_location_input(self, value):
        self.daily_rent_location_input.set_value(value)
        return self

    def click_daily_rent_realty_location(self):
        self.daily_rent_realty_location.click()
        return self

    def click_daily_rent_calendar_button(self):
        self.daily_rent_calendar_button.click()
        return self

    def click_daily_rent_body(self):
        self.daily_rent_body.click()
        return self

    # Методы для вкладки "Построить"
    def click_build_realty_tab(self):
        self.build_realty_tab.click()
        return self

    # Методы для вкладки "Оценить"
    def click_estimate_realty_tab(self):
        self.estimate_realty_tab.click()
        return self

    # Методы для вкладки "Ипотека"
    def click_mortgage_realty_tab(self):
        self.mortgage_realty_tab.click()
        return self

    def click_mortgage_realty_type_dropdown(self):
        self.mortgage_realty_type_dropdown.click()
        return self

    def click_mortgage_realty_newbuilding_checkbox(self):
        self.mortgage_realty_newbuilding_checkbox.click()
        return self

    def fill_mortgage_realty_price(self, value):
        self.mortgage_realty_price.set_value(value)
        return self

    def fill_mortgage_realty_down_payment(self, value):
        self.mortgage_realty_down_payment.set_value(value)
        return self

    def click_mortgage_realty_term(self):
        self.mortgage_realty_term.click()
        return self

    def click_mortgage_realty_term_from_list(self):
        self.mortgage_realty_term_from_list.click()
        return self

    def fill_mortgage_realty_location_input(self, value):
        self.mortgage_realty_location_input.set_value(value)
        return self

    def click_mortgage_realty_location(self):
        self.mortgage_realty_location.click()
        return self

    def click_mortgage_realty_right_button(self):
        self.mortgage_realty_right_button.click()
        return self

    # Методы для вкладки "Подбор риелтора"
    def click_realtor_realty_tab(self):
        self.realtor_realty_tab.click()
        return self

    def should_header_have_text(self,value):
        self.realtor_question_tab.should(have.text(value))
        return self

    # Методы для вкладки "Подать за 0 ₽"
    def click_zero_ruble_sell_realty_tab(self):
        self.zero_ruble_sell_realty_tab.click()
        return self