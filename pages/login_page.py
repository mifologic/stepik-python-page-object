import re
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        login = self.browser.find_element(*LoginPageLocators.NEW_USER_LOGIN)
        login.send_keys(email)
        user_password = self.browser.find_element(*LoginPageLocators.NEW_USER_PASSWORD)
        user_password.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password.send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert re.search(r'login', url), "Substring 'login' is not present in link"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
