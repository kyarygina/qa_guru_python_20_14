import allure
from allure_commons.types import Severity
from pages.build_realty_page import BuildRealtyPage
from pages.buy_realty_page import BuyRealtyPage
from pages.daily_rent_realty_page import DailyRentRealtyPage
from pages.estimate_realty_page import EstimateRealtyPage
from pages.main_page import MainPage
from pages.mortgage_questions_page import MortgageQuestionsPage
from pages.owner_authentication_page import OwnerAuthenticationPage
from pages.rent_realty_page import RentRealtyPage

main_page = MainPage()

@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Купить'")
@allure.link("https://www.cian.ru", name="Testing")
def test_buy_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Купить'"):
        (
            main_page
            .click_buy_realty_type_dropdown()
            .click_house_checkbox()
            .click_buy_realty_price_dropdown()
            .fill_buy_realty_price_from_input('7000000')
            .fill_buy_realty_price_to_input('9000000')
            .fill_buy_realty_location_input('Сочи')
            .click_buy_realty_location()
            .click_filters_search_button()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'Купить дом в Сочи'"):
        buy_realty_page = BuyRealtyPage()
        buy_realty_page.should_header_have_text('Купить дом в Сочи')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Снять'")
@allure.link("https://www.cian.ru", name="Testing")
def test_rent_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Снять'"):
        (
            main_page
            .click_rent_realty_tab()
            .click_rent_realty_price_dropdown()
            .fill_rent_realty_price_from_input('20000')
            .fill_rent_realty_price_to_input('30000')
            .fill_rent_realty_location_input('Краснодар')
            .click_rent_realty_location()
            .click_filters_search_button()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'Снять 1, 2-комнатную квартиру в Краснодаре на длительный срок'"):
        rent_realty_page = RentRealtyPage()
        rent_realty_page.should_header_have_text('Снять 1, 2-комнатную квартиру в Краснодаре на длительный срок')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Посуточно'")
@allure.link("https://www.cian.ru", name="Testing")
def test_daily_rent_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Посуточно'"):
        (
            main_page
            .click_daily_rent_realty_tab()
            .fill_daily_rent_location_input('Калининград')
            .click_daily_rent_realty_location()
            .click_daily_rent_calendar_button()
            .click_daily_rent_body()
            .click_filters_search_button()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'Снять квартиру посуточно в Калининграде'"):
        daily_rent_realty_page = DailyRentRealtyPage()
        daily_rent_realty_page.should_header_have_text('Снять квартиру посуточно в Калининграде')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Построить'")
@allure.link("https://www.cian.ru", name="Testing")
def test_build_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Построить'"):
        (
            main_page
            .click_build_realty_tab()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'Проекты домов'"):
        build_realty_page = BuildRealtyPage()
        build_realty_page.should_header_have_text('Проекты домов')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Оценка'")
@allure.link("https://www.cian.ru", name="Testing")
def test_estimate_realty_tab_functionality():
    with allure.step("Заполнить фильтры на вкладке 'Оценка'"):
        (
            main_page
            .click_estimate_realty_tab()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'Мой дом — центр управления'"):
        estimate_realty_page = EstimateRealtyPage()
        estimate_realty_page.should_header_have_text('Мой дом — центр управления')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Ипотека'")
@allure.link("https://www.cian.ru", name="Testing")
def test_mortgage_realty_tab_functionality():
    with allure.step("Заполнить фильтры на вкладке 'Ипотека'"):
        (
            main_page
            .click_mortgage_realty_tab()
            .click_mortgage_realty_type_dropdown()
            .click_mortgage_realty_newbuilding_checkbox()
            .fill_mortgage_realty_price('9000000')
            .fill_mortgage_realty_down_payment('3000000')
            .click_mortgage_realty_term()
            .click_mortgage_realty_term_from_list()
            .fill_mortgage_realty_location_input('Саратов')
            .click_mortgage_realty_location()
            .click_mortgage_realty_right_button()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'Ответьте на несколько вопросов'"):
        mortgage_questions_page = MortgageQuestionsPage()
        mortgage_questions_page.should_header_have_text('Ответьте на несколько вопросов')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Подбор риелтора'")
@allure.link("https://www.cian.ru", name="Testing")
def test_realtor_realty_tab_filters():
    with allure.step("Заполнить фильтры на вкладке 'Подбор риелтора'"):
        (
            main_page
            .click_realtor_realty_tab()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'С чем нужна помощь риелтора?'"):
        main_page.should_header_have_text('С чем нужна помощь риелтора?')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "kyarygina")
@allure.feature("Фильтры поиска на главной странице")
@allure.story("Проверка фильтров на вкладке 'Подать за 0 ₽'")
@allure.link("https://www.cian.ru", name="Testing")
def test_zero_ruble_sell_realty_tab_display():
    with allure.step("Заполнить фильтры на вкладке 'Подать за 0 ₽'"):
        (
            main_page
            .click_zero_ruble_sell_realty_tab()
        )
    with allure.step("Проверить, что осуществлен переход на страницу с заголовком 'разместить объявление'"):
        owner_authentication_page = OwnerAuthenticationPage()
        owner_authentication_page.should_header_have_text('разместить объявление')