import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from mimesis import Person


@pytest.mark.parametrize('promo_number', ["offer0",
                                          "offer1",
                                          "offer2",
                                          "offer3",
                                          "offer4",
                                          "offer5",
                                          "offer6",
                                          pytest.param("offer7", marks=pytest.mark.xfail),
                                          "offer8",
                                          "offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, promo_number):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={}".format(promo_number)
    page = ProductPage(browser, link)
    page.open()
    book_name = page.get_book_name()
    book_price = page.get_book_price()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_confirm_message_with_book_name(book_name)
    page.should_be_message_with_basket_price(book_price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.confirm_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()
    basket_page.should_be_basket_is_empty_message()


@pytest.mark.user_tests
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = Person().email(domains=None)
        password = Person().password(length=10, hashed=False)
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        yield

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        book_name = page.get_book_name()
        book_price = page.get_book_price()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_be_confirm_message_with_book_name(book_name)
        page.should_be_message_with_basket_price(book_price)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
