from ..pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"

def test_correct_product_url(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_new_year_url()

def test_should_see_add_basket_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_basket_button()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

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