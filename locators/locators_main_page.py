from selenium.webdriver.common.by import By

PROFILE_BUTTON = By.XPATH, '//*[@id="root"]/div/header/nav/a/p'
INGREDIENT_BUN = By.PARTIAL_LINK_TEXT, 'Флюоресцентная булка R2-D3'
INGREDIENT_BUN_COUNTER = By.CSS_SELECTOR, 'p.counter_counter__num__3nue1'
INGREDIENT_POPUP_TITLE = By.CSS_SELECTOR, 'h2.Modal_modal__title_modified__3Hjkd'
INGREDIENT_POPUP_CLOSE = By.CSS_SELECTOR, 'button.Modal_modal__close_modified__3V5XS'
ORDER_BASKET = By.CLASS_NAME, 'BurgerConstructor_basket__29Cd7'
ORDER_BUTTON = By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7 button.button_button__33qZ0'

