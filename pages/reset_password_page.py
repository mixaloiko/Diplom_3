from locators.locators_reset_password_page import PASSWORD_INPUT_FIELD, SHOW_PASSWORD_BUTTON
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def click_show_password_button(self):
        self.hide_overlay()
        self.click_on_element(SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        element = self.find_element_with_wait(PASSWORD_INPUT_FIELD)

        # Получаем значение атрибута 'class'
        classes = element.get_attribute('class')

        # Проверяем, есть ли нужный класс
        return 'input_status_active' in classes.split()

