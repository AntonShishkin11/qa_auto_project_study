from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Добавить в корзину']")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong ")
