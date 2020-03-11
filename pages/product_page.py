from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def get_book_name(self):
        book = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        return book.text

    def get_book_price(self):
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
        return price.text

    def should_be_confirm_message_with_book_name(self, book_name):
        message = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_MESSAGE)
        assert self.is_element_present(*ProductPageLocators.CONFIRM_MESSAGE)
        assert message.text == book_name, "Другое название книги " + message.text

    def should_be_message_with_basket_price(self, book_price):
        price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_IN_MESSAGE).text
        assert price == book_price, "Другая цена " + price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.CONFIRM_MESSAGE), \
           "Success message is presented, but should not be"

    def confirm_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.CONFIRM_MESSAGE)
