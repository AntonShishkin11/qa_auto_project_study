import faker

import pytest

from ..pages.login_page import LoginPage
from ..pages.basket_page import BasketPage
from ..pages.product_page import ProductPage

# link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        f = faker.Faker()
        email = f.email()
        password = f.password()

        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    # @pytest.mark.parametrize('promo_offer', [
    #     "0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
    def test_user_can_add_product_to_basket(self, browser, promo_offer=1):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_correct_add_to_basket_message()
        page.should_be_correct_price_in_basket_message()

    def test_user_cant_see_add_to_basket_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_added_to_basket_message()


def test_correct_product_url(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_new_year_url()


def test_should_see_add_basket_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_basket_button()


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

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_basket_is_empty()
    basket_page.should_be_basket_is_empty_text()
