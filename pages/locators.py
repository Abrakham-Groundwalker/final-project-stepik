from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR,".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR,"h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR,".product_main p.price_color")
    MESSAGE_ADDED_PRODUCT = (By.CSS_SELECTOR,".alert strong")
    MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR,".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR,".alertinner")

class BasketPageLocators():
    MESSAGE_ABOUT_BASKET_FULLNESS = (By.CSS_SELECTOR,".content p")
    BASKET_ITEMS = (By.CSS_SELECTOR,".basket-items")

