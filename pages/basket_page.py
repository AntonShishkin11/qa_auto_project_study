from .locators import BasketPageLocators, BasePageLocators
from ..pages.base_page import BasePage

languages = {
    "ar": "سلة التسوق فارغة",
    "ca": "La seva cistella està buida.",
    "cs": "Váš košík je prázdný.",
    "da": "Din indkøbskurv er tom.",
    "de": "Ihr Warenkorb ist leer.",
    "en": "Your basket is empty.",
    "en-gb": "Your basket is empty.",
    "el": "Το καλάθι σας είναι άδειο.",
    "es": "Tu carrito esta vacío.",
    "fi": "Korisi on tyhjä",
    "fr": "Votre panier est vide.",
    "it": "Il tuo carrello è vuoto.",
    "ko": "장바구니가 비었습니다.",
    "nl": "Je winkelmand is leeg",
    "pl": "Twój koszyk jest pusty.",
    "pt": "O carrinho está vazio.",
    "pt-br": "Sua cesta está vazia.",
    "ro": "Cosul tau este gol.",
    "ru": "Ваша корзина пуста",
    "sk": "Váš košík je prázdny",
    "uk": "Ваш кошик пустий.",
    "zh-cn": "Your basket is empty.",
}



class BasketPage(BasePage):

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "Url is incorrect"

    def should_be_basket_is_empty_text(self):
        basket_is_empty_message = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        page_lang = self.browser.find_element(*BasePageLocators.PAGE_LANGUAGE).get_attribute("value")
        assert languages[page_lang] in basket_is_empty_message, \
            "Basket isn't empty or message is incorrect"

    def should_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PURCHASE_LIST), \
        "Basket isn't empty"




