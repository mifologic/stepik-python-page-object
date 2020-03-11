from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BOOK_NAME = (By.CSS_SELECTOR, "h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p:nth-child(1) > strong")
