import allure

from conftest import *
from helpers import register_new_user_and_return_data, create_random_order


@allure.title("Лента заказов")
class TestOrderFeed:
    @allure.step("Нажать на заказ, проверить, что появилось всплывающее окно с деталями заказа")
    def test_order_details_popup_opened(self, feed_page):
        feed_page.load()
        feed_page.hide_overlay()
        feed_page.open_order_item()
        assert feed_page.is_order_details_popup_opened()

    @allure.step("Создать заказ, войти в личный кабинет, нажать на историю заказов, проверить, что созданный заказ есть в ленте заказов")
    def test_order_from_history_displayed_on_feed_page(self, login_page, main_page, profile_page, feed_page, order_history_page):
        user_data = register_new_user_and_return_data()
        create_random_order(user_data['accessToken'])
        login_page.load()
        login_page.hide_overlay()
        login_page.login_existing_user(user_data['email'], user_data['password'])
        main_page.click_profile_button()
        profile_page.click_order_history_button()
        history_order_id = order_history_page.get_order_id()
        order_history_page.find_and_click_feed_button()
        assert feed_page.is_order_id_present(history_order_id)

    @allure.step("Создать заказ, сравнить, что счетчик заказов за все время изменился")
    def test_order_counter_all_time_change(self, feed_page):
        feed_page.load()
        all_time_count_before = feed_page.get_all_time_count()
        user_data = register_new_user_and_return_data()
        create_random_order(user_data['accessToken'])
        feed_page.refresh()
        all_time_count_after = feed_page.get_all_time_count()
        assert all_time_count_after > all_time_count_before

    @allure.step("Создать заказ, сравнить, что счетчик заказов за сегодня изменился")
    def test_order_counter_today_change(self, feed_page):
        feed_page.load()
        today_count_before = feed_page.get_today_count()
        user_data = register_new_user_and_return_data()
        create_random_order(user_data['accessToken'])
        feed_page.refresh()
        today_count_after = feed_page.get_today_count()
        assert today_count_after > today_count_before

    @allure.step("Создать заказ, проверить, что номер заказа отображается в разделе В работе")
    def test_order_in_progress(self, feed_page):
        user_data = register_new_user_and_return_data()
        order = create_random_order(user_data['accessToken'])
        order_id = str(order['order']['number'])
        feed_page.load()
        feed_page.wait(5)
        in_progress_data = feed_page.get_in_progress_data()
        assert order_id in in_progress_data
