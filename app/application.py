from pages.main_page import MainPage
from pages.search_results_page import Search
from pages.registration_page import RegistrationPage
from pages.my_account_page import AccountPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = Search(self.driver)
        self.registration_page = RegistrationPage(self.driver)
        self.my_account_page = AccountPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)