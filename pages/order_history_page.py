from locators.locators_order_history import HISTORY_ORDER_ID, FEED_BUTTON
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):
    def get_order_id(self):
        element = self.find_element_with_wait(HISTORY_ORDER_ID)
        return element.text

    def find_and_click_feed_button(self):
        self.click_on_element(FEED_BUTTON)

