import allure

from conftest import *


@allure.title("Личный кабинет")
class TestProfile:
    @allure.step("Войти на страницу логина, заполнить обязательные поля, нажать Войти, нажать на кнопку Личный кабине, проверить, что произошел переход в личный кабинет")
    def test_open_profile(self, login_page, main_page, profile_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.login_new_user()
        main_page.click_profile_button()
        assert profile_page.is_page_opened()

    @allure.step("Войти на страницу логина, заполнить обязательные поля, нажать Войти, нажать на кнопку Личный кабинет, нажать на кнопку История заказов, проверить периход в историю заказов")
    def test_open_order_history(self, login_page, main_page, profile_page, order_history_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.login_new_user()
        main_page.click_profile_button()
        profile_page.click_order_history_button()
        assert order_history_page.is_page_opened()

    @allure.step("Войти на страницу логина, ввести email и password, нажать Войти, нажать кнопку перехода в личный кабинет, нажать кнопку Выйти")
    def test_logout(self, login_page, main_page, profile_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.login_new_user()
        main_page.click_profile_button()
        profile_page.click_logout_button()
        assert login_page.is_page_opened()

