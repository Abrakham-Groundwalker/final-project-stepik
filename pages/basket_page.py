from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_ITEMS), "basket items is presented"

    def should_be_message_about_basket_empties(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_ABOUT_BASKET_FULLNESS), "Message about basket empties is not presented"
    