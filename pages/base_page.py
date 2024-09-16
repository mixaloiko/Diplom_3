from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def load(self):
        self.driver.get(self.url)

    def refresh(self):
        self.driver.refresh()

    def wait(self, seconds):
        action_chains = ActionChains(self.driver)
        action_chains.pause(seconds).perform()

    def is_page_opened(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 5).until(expected_conditions.url_contains(self.url))
        # проверить, что произошел переход на страницу сброса пароля
        current_url = self.driver.current_url
        return self.url in current_url

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def hide_overlay(self):
        if self.driver.shouldHideOverlay is True:
            self.driver.execute_script("document.getElementsByClassName('Modal_modal__loading__3534A')[0].parentElement.style.display = 'none';")

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        return element.send_keys(text)
