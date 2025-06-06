import time

import pytest

from ..pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"


def test_correct_product_url(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_new_year_url()


def test_should_see_add_basket_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_basket_button()


# @pytest.mark.parametrize('promo_offer', [
#     "0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_can_add_product_to_basket(browser, promo_offer=1):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_add_to_basket_message()
    page.should_be_correct_price_in_basket_message()


def test_add_to_basket_message_is_correct(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_add_to_basket_message()


def test_price_in_basket_message_is_correct(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_correct_price_in_basket_message()


@pytest.mark.xfail
def test_cant_see_added_to_basket_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_added_to_basket_message()


def test_guest_cant_see_add_to_basket_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_added_to_basket_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_added_to_basket_message()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
