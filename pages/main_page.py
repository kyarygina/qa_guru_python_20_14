import allure
from selene import browser
from selene.support.conditions import have


class MainPage:

    def __init__(self):
        # Кнопка "Найти"
        self.filters_search_button = browser.all('a').element_by(have.text('Найти'))

        # Элементы на вкладке "Купить"
        self.buy_realty_type_dropdown = browser.element('button[title="Квартиру в новостройке и вторичке"]')
        self.buy_realty_house_checkbox = browser.all('span').element_by(have.text('Дом, дача'))
        self.buy_realty_price_dropdown = browser.all('button').element_by(have.text('Цена'))
        self.buy_realty_price_from_input = browser.element('input[placeholder="от"]')
        self.buy_realty_price_to_input = browser.element('input[placeholder="до"]')
        self.buy_realty_location_input = browser.element('input[placeholder="Город, адрес, метро, район, ж/д или шоссе"]')
        self.buy_realty_location = browser.element('[title="Сочи, Краснодарский край"]')

        # Элементы на вкладке "Снять"
        self.rent_realty_tab = browser.all('a').element_by(have.text('Снять'))
        self.rent_realty_price_dropdown = browser.all('button').element_by(have.text('Цена'))
        self.rent_realty_price_from_input = browser.element('input[placeholder="от"]')
        self.rent_realty_price_to_input = browser.element('input[placeholder="до"]')
        self.rent_realty_location_input = browser.element('input[placeholder="Город, адрес, метро, район, ж/д, шоссе или ЖК"]')
        self.rent_realty_location = browser.element('span[title="Краснодар"]')

        # Элементы на вкладке "Посуточно"
        self.daily_rent_realty_tab = browser.all('a').element_by(have.text('Посуточно'))
        self.daily_rent_location_input = browser.element('input[placeholder="Куда вы хотите поехать?"]')
        self.daily_rent_realty_location = browser.element('span[title="Калининград"]')
        self.daily_rent_calendar_button = browser.all('button[data-name="FilterButton"]').element_by(have.text('Заезд — Отъезд'))
        self.daily_rent_body = browser.element('body')

        # Элементы на вкладке "Построить"
        self.build_realty_tab = browser.all('a').element_by(have.text('Построить'))

        # Элементы на вкладке "Оценить"
        self.estimate_realty_tab = browser.all('a').element_by(have.text('Оценить'))

        # Элементы на вкладке "Ипотека"
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

        # Элементы на вкладке "Подбор риелтора"
        self.realtor_realty_tab = browser.all('a').element_by(have.text('Подбор риелтора'))
        self.realtor_question_tab = browser.element('div[data-name="CPDModalContainer"] span')

        # Элементы на вкладке "Подать за 0 ₽"
        self.zero_ruble_sell_realty_tab = browser.all('a').element_by(have.text('Подать за 0 ₽'))

    # Методы для вкладки "Купить"

    @allure.step("Нажать на дропдаун с выбором типа недвижимости")
    def click_buy_realty_type_dropdown(self):
        self.buy_realty_type_dropdown.click()
        return self

    @allure.step("Выбрать чек-бокс 'Дом,дача'")
    def click_house_checkbox(self):
        self.buy_realty_house_checkbox.click()
        return self

    @allure.step("Нажать на дропдаун с выбором цены")
    def click_buy_realty_price_dropdown(self):
        self.buy_realty_price_dropdown.click()
        return self

    @allure.step("Заполнить поле с ценой 'от'")
    def fill_buy_realty_price_from_input(self, value):
        self.buy_realty_price_from_input.set_value(value)
        return self

    @allure.step("Заполнить поле с ценой 'до'")
    def fill_buy_realty_price_to_input(self, value):
        self.buy_realty_price_from_input.set_value(value)
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_buy_realty_location_input(self, value):
        self.buy_realty_location_input.set_value(value)
        return self

    @allure.step("Нажать на локацию из выпадающего списка")
    def click_buy_realty_location(self):
        self.buy_realty_location.click()
        return self

    @allure.step("Нажать на кнопку 'Найти'")
    def click_filters_search_button(self):
        self.filters_search_button.click()
        return self

    # Методы для вкладки "Снять"

    @allure.step("Нажать на вкладку 'Снять'")
    def click_rent_realty_tab(self):
        self.rent_realty_tab.click()
        return self

    @allure.step("Нажать на дропдаун с выбором цены")
    def click_rent_realty_price_dropdown(self):
        self.rent_realty_price_dropdown.click()
        return self

    @allure.step("Заполнить поле с ценой 'от'")
    def fill_rent_realty_price_from_input(self, value):
        self.rent_realty_price_from_input.set_value(value)
        return self

    @allure.step("Заполнить поле с ценой 'до'")
    def fill_rent_realty_price_to_input(self, value):
        self.rent_realty_price_to_input.set_value(value)
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_rent_realty_location_input(self, value):
        self.rent_realty_location_input.set_value(value)
        return self

    @allure.step("Нажать на локацию из выпадающего списка")
    def click_rent_realty_location(self):
        self.rent_realty_location.click()
        return self

    # Методы для вкладки "Посуточно"

    @allure.step("Нажать на вкладку 'Посуточно'")
    def click_daily_rent_realty_tab(self):
        self.daily_rent_realty_tab.click()
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_daily_rent_location_input(self, value):
        self.daily_rent_location_input.set_value(value)
        return self

    @allure.step("Нажать на локацию из выпадающего списка")
    def click_daily_rent_realty_location(self):
        self.daily_rent_realty_location.click()
        return self

    @allure.step("Нажать на дропдаун с календарем")
    def click_daily_rent_calendar_button(self):
        self.daily_rent_calendar_button.click()
        return self

    @allure.step("Закрыть календарь")
    def click_daily_rent_body(self):
        self.daily_rent_body.click()
        return self

    # Методы для вкладки "Построить"

    @allure.step("Нажать на вкладку 'Построить'")
    def click_build_realty_tab(self):
        self.build_realty_tab.click()
        return self

    # Методы для вкладки "Оценить"

    @allure.step("Нажать на вкладку 'Оценить'")
    def click_estimate_realty_tab(self):
        self.estimate_realty_tab.click()
        return self

    # Методы для вкладки "Ипотека"

    @allure.step("Нажать на вкладку 'Ипотека'")
    def click_mortgage_realty_tab(self):
        self.mortgage_realty_tab.click()
        return self

    @allure.step("Нажать на дропдаун с выбором типа недвижимости")
    def click_mortgage_realty_type_dropdown(self):
        self.mortgage_realty_type_dropdown.click()
        return self

    @allure.step("Выбрать чек-бокс 'Квартира в новостройке'")
    def click_mortgage_realty_newbuilding_checkbox(self):
        self.mortgage_realty_newbuilding_checkbox.click()
        return self

    @allure.step("Указать стоимость недвижимости")
    def fill_mortgage_realty_price(self, value):
        self.mortgage_realty_price.set_value(value)
        return self

    @allure.step("Указать сумму первоначального взноса")
    def fill_mortgage_realty_down_payment(self, value):
        self.mortgage_realty_down_payment.set_value(value)
        return self

    @allure.step("Нажать на дропдаун с выбором срока ипотеки")
    def click_mortgage_realty_term(self):
        self.mortgage_realty_term.click()
        return self

    @allure.step("Выбрать срок ипотеки")
    def click_mortgage_realty_term_from_list(self):
        self.mortgage_realty_term_from_list.click()
        return self

    @allure.step("Заполнить поле с локацией")
    def fill_mortgage_realty_location_input(self, value):
        self.mortgage_realty_location_input.set_value(value)
        return self

    @allure.step("Выбрать локацию из выпадающего списка")
    def click_mortgage_realty_location(self):
        self.mortgage_realty_location.click()
        return self

    @allure.step("Нажать на кнопку 'Получить предложения банков'")
    def click_mortgage_realty_right_button(self):
        self.mortgage_realty_right_button.click()
        return self

    # Методы для вкладки "Подбор риелтора"

    @allure.step("Нажать на вкладку 'Подбор риелтора'")
    def click_realtor_realty_tab(self):
        self.realtor_realty_tab.click()
        return self

    @allure.step("Проверить наличие текста в заголовке")
    def should_header_have_text(self,value):
        self.realtor_question_tab.should(have.text(value))
        return self

    # Методы для вкладки "Подать за 0 ₽"

    @allure.step("Нажать на вкладку 'Подать за 0 ₽'")
    def click_zero_ruble_sell_realty_tab(self):
        self.zero_ruble_sell_realty_tab.click()
        return self