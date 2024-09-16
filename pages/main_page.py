from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_main_page import *
from pages.base_page import BasePage


class MainPage(BasePage):
    def find_and_click_ingredient(self):
        self.click_on_element(INGREDIENT_BUN)

    def is_pop_up_with_detail_ingredient_visible(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(INGREDIENT_POPUP_TITLE))
        title_element_text = self.get_text_from_element(INGREDIENT_POPUP_TITLE)
        return title_element_text == 'Детали ингредиента'

    def open_ingredient_and_close(self):
        self.click_on_element(INGREDIENT_BUN)
        self.click_on_element(INGREDIENT_POPUP_CLOSE)

    def check_pop_up_with_detail_ingredient_closed(self):
        # ожидание загрузки страницы
        WebDriverWait(self.driver, 3).until(expected_conditions.invisibility_of_element_located(INGREDIENT_POPUP_TITLE))
        title_element = self.driver.find_element(*INGREDIENT_POPUP_TITLE)
        return not title_element.is_displayed()

    def drag_and_drop_ingredient(self):
        # Находим элементы: что перетаскивать и куда
        source_element = self.find_element_with_wait(INGREDIENT_BUN)  # Элемент для перетаскивания
        target_element = self.find_element_with_wait(ORDER_BASKET)  # Целевая область

        # Выполняем drag-and-drop с помощью JavaScript
        drag_and_drop_script = """
            function simulateDragDrop(sourceNode, destinationNode) {
                var EVENT_TYPES = {
                    DRAG_END: 'dragend',
                    DRAG_START: 'dragstart',
                    DROP: 'drop'
                }

                function createCustomEvent(type) {
                    var event = new CustomEvent("CustomEvent")
                    event.initCustomEvent(type, true, true, null)
                    event.dataTransfer = {
                        data: {},
                        setData: function(type, val) {
                            this.data[type] = val
                        },
                        getData: function(type) {
                            return this.data[type]
                        }
                    }
                    return event
                }

                function dispatchEvent(node, type, event) {
                    if (node.dispatchEvent) {
                        return node.dispatchEvent(event)
                    }
                    if (node.fireEvent) {
                        return node.fireEvent("on" + type, event)
                    }
                }

                var dragStartEvent = createCustomEvent(EVENT_TYPES.DRAG_START)
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, dragStartEvent)

                var dropEvent = createCustomEvent(EVENT_TYPES.DROP)
                dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent)

                var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END)
                dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent)
            }

            simulateDragDrop(arguments[0], arguments[1])
        """

        self.driver.execute_script(drag_and_drop_script, source_element, target_element)

    def get_ingredient_counter_value(self):
        source_element = self.find_element_with_wait(INGREDIENT_BUN)
        counter_element = source_element.find_element(*INGREDIENT_BUN_COUNTER)
        return counter_element.text

    def check_order_button_available(self):
        order_button = self.find_element_with_wait(ORDER_BUTTON)
        return order_button.is_displayed()

    def click_profile_button(self):
        self.click_on_element(PROFILE_BUTTON)
