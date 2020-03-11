from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > a")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class BasketPageLocators:
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    CONFIRM_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    BOOK_NAME = (By.CSS_SELECTOR, "h1")
    BOOK_PRICE = (By.CSS_SELECTOR, ".price_color")
    BOOK_NAME_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BASKET_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p:nth-child(1) > strong")
