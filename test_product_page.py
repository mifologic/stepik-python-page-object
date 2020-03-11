import time

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    book_name = page.get_book_name()
    book_price = page.get_book_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_confirm_message(book_name)
    page.should_be_basket_price(book_price)

