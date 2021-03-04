from .base_page import BasePage
from .locators import LoginPageLocators

link = 'http://selenium1py.pythonanywhere.com/accounts/login/'

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'Это не страница LoginPage'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Форма аутентификации не найдена'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации нового пользователя не найдена"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password1_field.send_keys(password)
        confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_CONFIRM)
        confirm_field.send_keys(password)
        submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit_button.click()