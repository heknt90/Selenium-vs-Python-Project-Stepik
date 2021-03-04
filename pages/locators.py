from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a.btn')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    CONTENT_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    TITLE = (By.CSS_SELECTOR, "#content_inner h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner .price_color")
    SUCCESS_ADD_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-success:nth-child(1) .alertinner strong")
    SUTISFIED_OFFER_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-success:nth-child(2) .alertinner strong")
    TOTAL_COST_BASKET_ALERT = (By.CSS_SELECTOR, "#messages .alert.alert-info .alertinner p:nth-child(1) strong")