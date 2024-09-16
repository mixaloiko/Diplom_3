from locators.locators_feed_page import ORDER_ITEM, ORDER_DETAILS_POPUP, ORDER_ITEM_LIST, ORDER_COUNTER_ALL_TIME, \
    ORDER_COUNTER_TODAY, ORDER_IN_PROGRESS
from pages.base_page import BasePage


class FeedPage(BasePage):
    def open_order_item(self):
        self.click_on_element(ORDER_ITEM)

    def check_order_details_popup_opened(self):
        details_popup = self.find_element_with_wait(ORDER_DETAILS_POPUP)
        return details_popup.is_displayed()

    def check_order_id_is_present(self, order_id):
        elements_list = self.find_element_with_wait(ORDER_ITEM_LIST)
        return order_id in elements_list.text

    def get_all_time_count(self):
        self.scroll_to_element(ORDER_COUNTER_ALL_TIME)
        all_time_element = self.find_element_with_wait(ORDER_COUNTER_ALL_TIME)
        return all_time_element.text

    def get_today_count(self):
        self.scroll_to_element(ORDER_COUNTER_TODAY)
        today_element = self.find_element_with_wait(ORDER_COUNTER_TODAY)
        return today_element.text

    def get_in_progress_data(self):
        in_progress_element = self.find_element_with_wait(ORDER_IN_PROGRESS)
        return in_progress_element.text
