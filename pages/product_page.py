import time

from .locators import ProductPageLocators
from ..pages.base_page import BasePage


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_new_year_url()
        self.should_be_add_basket_button()

    def should_be_product_new_year_url(self):
        assert '?promo=newYear' in self.browser.current_url, "Url is incorrect"

    def should_be_add_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON), "Add basket button is not presented"

    def add_product_to_basket(self):
        add_basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_add_to_basket_message(self):
        message = self.browser.find_element(*ProductPageLocators.ADD_BASKET_MESSAGE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert message == f"{product_name} has been added to your basket." or \
            message == f"{product_name} был добавлен в вашу корзину.", 'Add to basket message is incorrect'

    def should_not_be_added_to_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADD_BASKET_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_added_to_basket_message(self):
        assert self.is_disappeared(*ProductPageLocators.ADD_BASKET_MESSAGE), \
            "Success message didn't disappear, but should not be"

    def should_be_correct_price_in_basket_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_message = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == price_in_message, "Price in message and price of product don't match"
