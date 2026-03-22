from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, f"В юрл {self.url} нет подстроки login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        emailInput = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        emailInput.send_keys(email)

        password1Input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1)
        password1Input.send_keys(password)

        password2Input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2)
        password2Input.send_keys(password)

        registerBtn = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        registerBtn.click()