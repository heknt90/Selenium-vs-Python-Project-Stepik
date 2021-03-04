from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, "Это не страница с корзиной товаров"

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "В корзине не должно находиться товаров"

    def should_be_no_content_message(self):
        assert self.is_element_present(*BasketPageLocators.CONTENT_MESSAGE), "Сообщение о том, что корзина пуста - не найдено"

    