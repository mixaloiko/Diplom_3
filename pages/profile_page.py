from locators.locators_profile_page import ORDER_HISTORY_BUTTON, LOGOUT_BUTTON
from pages.base_page import BasePage


class ProfilePage(BasePage):

    def click_order_history_button(self):
        self.click_on_element(ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_on_element(LOGOUT_BUTTON)
