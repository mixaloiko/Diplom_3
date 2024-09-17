from locators.locators_forgot_pasword_page import *
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    # находим и заполняем поле email, кликаем на кнопку восстановить
    def enter_email_and_click_reset(self):
        self.hide_overlay()
        self.set_text_to_element(EMAIL_INPUT, '123@123.ru')
        self.click_on_element(RECOVER_BUTTON)

    def click_recover_button(self):
        self.hide_overlay()
        self.click_on_element(RECOVER_BUTTON)

