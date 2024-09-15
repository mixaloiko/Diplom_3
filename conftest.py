import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from constants import *
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
from pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    driver = None
    if request.param == 'firefox':
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.shouldHideOverlay = True
    elif request.param == 'chrome':
        options = ChromeOption()
        driver = webdriver.Chrome()
        driver.shouldHideOverlay = False
    yield driver
    driver.quit()


@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver, LOGIN_URL)
    return page


@pytest.fixture()
def forgot_password_page(driver):
    page = ForgotPasswordPage(driver, FORGOT_PASSWORD_URL)
    return page


@pytest.fixture()
def reset_password_page(driver):
    page = ResetPasswordPage(driver, RESET_PASSWORD_URL)
    return page


@pytest.fixture()
def main_page(driver):
    page = MainPage(driver, MAIN_PAGE_URL)
    return page


@pytest.fixture()
def feed_page(driver):
    page = FeedPage(driver, FEED_PAGE_URL)
    return page


@pytest.fixture()
def profile_page(driver):
    page = ProfilePage(driver, PROFILE_PAGE_URL)
    return page


@pytest.fixture()
def order_history_page(driver):
    page = OrderHistoryPage(driver, ORDER_HISTORY_PAGE_URL)
    return page
