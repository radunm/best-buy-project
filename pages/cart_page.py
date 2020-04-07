from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import os
from time import sleep


class CartPage(Page):

    EMPTY_CART_TITLE_LOCATOR = (By.CSS_SELECTOR, "#cartApp h2.empty-cart__info-title")
    PRODUCT_TITLE_LOCATOR = (By.CSS_SELECTOR, ".cart-item__details a.cart-item__title")
    CART_ITEMS_LIST = (By.CSS_SELECTOR, ".cart-listing__items .cart-item__details a.cart-item__title")
    SELECT_QUANTITY_LOCATOR = (By.CSS_SELECTOR, "select.c-dropdown")
    ITEMS_QUANTITY_LOCATOR = (By.ID, "items-tab")

    def verify_empty_cart(self, expected_text: str):
        self.verify_text(expected_text, *self.EMPTY_CART_TITLE_LOCATOR)

    def verify_item_in_cart(self):
        actual_name_list = self.driver.find_elements(*self.CART_ITEMS_LIST)
        with open("products_name.txt", "r") as reader:
            for expected_name, actual_name in zip(reader.readlines(), reversed(actual_name_list)):
                assert expected_name[:-1] == actual_name.text, f'Expected text {expected_name}, but got {actual_name}'
        os.remove("products_name.txt")

    def previous_page(self):
        self.driver.back()

    def select_quantity(self, option):
        select = Select(self.driver.wait.until(EC.presence_of_element_located(self.SELECT_QUANTITY_LOCATOR)))
        select.select_by_visible_text(option)
        sleep(2)

    def verify_quantity(self, expected_quantity: str):
        actual_quantity = self.driver.find_element(*self.ITEMS_QUANTITY_LOCATOR).text
        assert expected_quantity in actual_quantity, f'Expected text {expected_quantity}, but got {actual_quantity}'