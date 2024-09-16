import allure

from conftest import *


@allure.title("Проверка основного функционала")
class TestMainFunctionality:
    @allure.step("Найти и нажать на кнопку Конструктор")
    def test_open_constructor(self, login_page, main_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.find_and_click_constructor_button()
        assert main_page.is_page_opened()

    @allure.step("Найти и нажать на кнопку Лента заказов")
    def test_feed_opened(self, login_page, feed_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.find_and_click_feed_button()
        assert feed_page.is_page_opened()

    @allure.step("Найти и нажать на ингредиент, проверить, что появился поп-ап с деталями ингредиента")
    def test_popup_with_details_ingredient_opened(self, main_page):
        main_page.load()
        main_page.hide_overlay()
        main_page.find_and_click_ingredient()
        assert main_page.is_pop_up_with_detail_ingredient_visible()

    @allure.step("Нажать на ингредиент, нажать на крестик на поп-апе ингредиента, проверить, что поп-ап закрылся")
    def test_popup_with_details_ingredient_closed(self, main_page):
        main_page.load()
        main_page.hide_overlay()
        main_page.open_ingredient_and_close()
        assert main_page.check_pop_up_with_detail_ingredient_closed()

    @allure.step("Найти и перетащить ингредиент, проверить, что каунтер ингредиента изменился")
    def test_ingredient_counter_increase(self, main_page):
        main_page.load()
        main_page.hide_overlay()
        counter_value_start = main_page.get_ingredient_counter_value()
        main_page.drag_and_drop_ingredient()
        counter_value_end = main_page.get_ingredient_counter_value()
        assert counter_value_start != counter_value_end

    @allure.step("Залогиниться и проверить, что есть кнопка оформить заказ")
    def test_user_can_create_order(self, login_page, main_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.login_new_user()
        assert main_page.check_order_button_available()
