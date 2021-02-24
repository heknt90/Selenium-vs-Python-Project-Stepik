from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):   

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.TITLE), "Не найдено название выбранного товара"
        title_header = self.browser.find_element(*ProductPageLocators.TITLE)
        return title_header.text
    
    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Не найдена стоимость выбранного товара"
        price_element = self.browser.find_element(*ProductPageLocators.PRICE)
        return price_element.text

    def check_alerts_after_added_product_to_basket(self):
        # check first alert
        self.should_be_first_alert()
        product_name = self.get_product_name()
        self.should_first_alert_contains_product_name(product_name)
        # check second alert
        self.should_be_second_alert()
        self.should_second_alert_contains_product_offer_check_confirm("Deferred benefit offer")
        # check third alert
        self.should_be_third_alert()
        product_price = self.get_product_price()
        self.should_third_alert_contains_total_price_equal_product_price(product_price)

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Не найдена кнопка добавления товара в корзину"

    def should_be_first_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_ALERT), "Не найдено первое уведомление"

    def should_first_alert_contains_product_name(self, product_name):
        print('Product Name', product_name)
        assert self.browser.find_element(*ProductPageLocators.SUCCESS_ADD_ALERT).text == product_name, f"В первом уведомлении нет подтверждения о добавлении товара с названием {product_name} в корзину"

    def should_be_second_alert(self):
        assert self.is_element_present(*ProductPageLocators.SUTISFIED_OFFER_ALERT), "Не найдено второе уведомление"

    def should_second_alert_contains_product_offer_check_confirm(self, offer_string):
        assert self.browser.find_element(*ProductPageLocators.SUTISFIED_OFFER_ALERT).text == offer_string, f"Во втором уведомлении нет подтверждения, что все товары в корзине соответствуют специальному предложению {offer_string}"

    def should_be_third_alert(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_COST_BASKET_ALERT), "Не найдено уведомление о стоимости товаров в корзине"

    def should_third_alert_contains_total_price_equal_product_price(self, product_price):
        assert self.browser.find_element(*ProductPageLocators.TOTAL_COST_BASKET_ALERT).text == product_price, "Стоимость товаров в корзине не совпадает со стоимостью выбранного товара"
    