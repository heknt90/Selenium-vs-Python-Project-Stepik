from time import sleep
import pytest

from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_alerts_after_added_product_to_basket()

same_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    # Открываем страницу товара 
    page = ProductPage(browser, same_link)
    page.open()
    # Добавляем товар в корзину 
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_ALERT), 'Незарегистрированный пользователь не должен видеть сообщение о добавлении товара в корзину'

def test_guest_cant_see_success_message(browser): 
    # Открываем страницу товара 
    page = ProductPage(browser, same_link)
    page.open()
    # Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_ALERT), 'Незарегистрированный пользователь не должен видеть сообщение о добавлении товара в корзину при открытии страницы'

def test_message_disappeared_after_adding_product_to_basket(browser): 
    # Открываем страницу товара
    page = ProductPage(browser, same_link)
    page.open()
    # Добавляем товар в корзину
    page.should_be_add_to_basket_button()
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе с помощью is_disappeared
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_ADD_ALERT), "Сообщение о добавлении товара в корзину должно было исчезнуть, но этого не произошло"


    