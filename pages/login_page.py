from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import register_new_user_and_return_data
from locators.locators_login_page import RECOVER_PASSWORD, CONSTRUCTOR_BUTTON, FEED_BUTTON, INPUT_EMAIL, INPUT_PASSWORD, \
    LOGIN_BUTTON
from pages.base_page import BasePage


class LoginPage(BasePage):

    def login_new_user(self):
        self.hide_overlay()

        user_data = register_new_user_and_return_data()

        self.set_text_to_element(INPUT_EMAIL, user_data['email'])
        self.set_text_to_element(INPUT_PASSWORD, user_data['password'])
        self.click_on_element(LOGIN_BUTTON)

    def login_existing_user(self, email, password):
        self.hide_overlay()

        self.set_text_to_element(INPUT_EMAIL, email)
        self.set_text_to_element(INPUT_PASSWORD, password)
        self.click_on_element(LOGIN_BUTTON)

    def find_and_click_forgot_password(self):
        self.scroll_to_element(RECOVER_PASSWORD)
        self.click_on_element(RECOVER_PASSWORD)

    def find_and_click_constructor_button(self):
        self.click_on_element(CONSTRUCTOR_BUTTON)

    def find_and_click_feed_button(self):
        self.click_on_element(FEED_BUTTON)

    def check_feed_page_opened(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains('feed'))
        # проверить, что произошел переход на страницу с заказами
        current_url = self.driver.current_url
        return 'feed' in current_url
