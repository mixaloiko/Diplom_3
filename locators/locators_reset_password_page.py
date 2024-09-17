from selenium.webdriver.common.by import By

SHOW_PASSWORD_BUTTON = By.CSS_SELECTOR, '.input__container:nth-child(1) .input__icon'
PASSWORD_INPUT_FIELD = By.CSS_SELECTOR, '.input__container:nth-child(1) > div'
PASSWORD_INPUT = By.NAME, 'Введите новый пароль'
