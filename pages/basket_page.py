from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET)

    def should_be_basket_is_empty_message(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        print(message.text)
        assert self.is_element_present(*BasketPageLocators.BASKET_MESSAGE)
