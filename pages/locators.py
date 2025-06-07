from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > \
    div.basket-mini.pull-right.hidden-xs > span > a")
    PAGE_LANGUAGE = (By.CSS_SELECTOR, "#language_selector > div > select > option[selected]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# class MainPageLocators():
#     LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONF_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ADD_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong ")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    CONTINUE_SHOPPING_LINK = (By.CSS_SELECTOR, "#content_inner > p > a")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#content_inner > div.form-group.clearfix > div > div > a")
    PURCHASE_LIST = (By.CSS_SELECTOR, "#content_inner > div.basket-title.hidden-xs")
