# For run test type this
# pytest -v --tb=line --language=en test_main_page.py

from pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
    # page.go_to_login_page