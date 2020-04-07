from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MainPage(Page):

    COUNTRY_LABEL = (By.CSS_SELECTOR, "div[lang='en'] .country-selection .us-link")
    POP_WINDOW_CLOSE = (By.CSS_SELECTOR, "button[type='button'].close:not(.modal-close)")
    SEARCH_INPUT = (By.ID, "gh-search-input")
    SUGGESTION_LIST = (By.CSS_SELECTOR, "#suggestViewClientComponent .suggestion-list a > span:not("
                                        ".suggestion-multicategory)")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit'].header-search-button")
    ACCOUNT_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".navigation-container .utility-navigation-list-item button["
                                               "data-lid='hdr_signin']")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "#account-menu-app .am-create-account__box a")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "#account-menu-app .lam-signIn__box a")
    PASSWORD = (By.ID, "fld-p1")
    EMAIL = (By.ID, "fld-e")
    SIGN_IN = (By.CSS_SELECTOR, ".cia-form button[type='submit']")
    NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, ".navigation-container .logged_user_name")
    CART_BUTTON_LOCATOR = (By.CSS_SELECTOR, ".shop-cart-icon .cart-link")

    def open(self):
        self.open_page('https://www.bestbuy.com/')

    def choose_country(self):
        self.wait_for_element_appear(*self.COUNTRY_LABEL)
        self.click(*self.COUNTRY_LABEL)

    def close_pop_up(self):
        self.wait_for_element_appear(*self.POP_WINDOW_CLOSE)
        self.click(*self.POP_WINDOW_CLOSE)

    def search_product(self, text: str):
        self.input_text(text, *self.SEARCH_INPUT)

    def search_product_click(self, text: str):
        self.input_text(text, *self.SEARCH_INPUT)
        # self.driver.wait.until(EC.text_to_be_present_in_element_value(self.SEARCH_INPUT, text_=text))
        sleep(2)
        # self.driver.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        self.click(*self.SEARCH_BUTTON)

    def wait_text(self, text: str):
        self.driver.wait.until(EC.text_to_be_present_in_element_value((By.ID, "gh-search-input"), text))
        # self.wait_for_text_element((By.ID, "gh-search-input"), "text")

    def wait_all_elements(self):
        self.wait_for_all_elements_appear(*self.SUGGESTION_LIST)

    def click_search_button(self):
        self.click(*self.SEARCH_BUTTON)

    def click_account_button(self):
        self.click(*self.ACCOUNT_BUTTON_LOCATOR)

    def click_create_account(self):
        self.click(*self.CREATE_ACCOUNT_BUTTON)

    def count_list(self, expected_value):
        self.count_elements(expected_value, *self.SUGGESTION_LIST)

    def click_sign_in_button(self):
        self.click(*self.SIGN_IN_BUTTON)

    def fill_data(self, email, password):
        self.input_text(email, *self.EMAIL)
        self.input_text(password, *self.PASSWORD)

    def click_submit_button(self):
        self.click(*self.SIGN_IN)

    def success_login(self, expected_name):
        self.verify_text(expected_name, *self.NAME_TITLE_LOCATOR)

    def click_cart_button(self):
        self.click(*self.CART_BUTTON_LOCATOR)