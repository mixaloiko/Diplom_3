import allure

from conftest import *


@allure.title("Восстановление пароля")
class TestForgotPassword:

    @allure.step("Найти и кликнуть по «Восстановить пароль» на странице логина, проверить переход на страницу восстановления пароля")
    def test_open_forgot_password_page(self, login_page, forgot_password_page):
        login_page.load()
        login_page.hide_overlay()
        login_page.find_and_click_forgot_password()
        assert forgot_password_page.is_page_opened()

    @allure.step("В поле для ввода email ввести email и нажать на кнопку восстановить")
    def test_set_email_and_click_reset(self, forgot_password_page, reset_password_page):
        forgot_password_page.load()
        forgot_password_page.hide_overlay()
        forgot_password_page.enter_email_and_click_reset()
        assert reset_password_page.is_page_opened()

    @allure.step("Кликнуть по кнопке скрыть/показать пароль")
    def test_input_password_active_after_click_on_show_button(self, forgot_password_page, reset_password_page):
        forgot_password_page.load()
        forgot_password_page.hide_overlay()
        forgot_password_page.click_recover_button()
        reset_password_page.click_show_password_button()
        assert reset_password_page.is_password_field_active()
