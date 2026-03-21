from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.get(self.url)
        btn = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        btn.click()
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should dissapear"

    def accuracy_of_message_about_adding_product(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_PRODUCT)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text == message.text

    def accuracy_of_message_about_basket_sum(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_PRICE)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert price.text in message.text
    