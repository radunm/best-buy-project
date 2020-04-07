from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class Search(Page):
    SEARCH_TITLE = (By.CSS_SELECTOR, "#search-header-1 h1.search-title")
    PRODUCT_LIST_LINK_LOCATOR = (By.CSS_SELECTOR, "#sku-list-1 .sku-item-list li.sku-item a.image-link")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-lg.add-to-cart-button")
    GO_TO_CART_BUTTON = (By.CSS_SELECTOR, ".top-nav-container a.cart-nav")
    PRODUCT_TITLE_LOCATOR = (By.CSS_SELECTOR, "h1")
    ADDED_TO_CART_LABEL = (By.CSS_SELECTOR, ".top-nav-container span.success-text")

    def check_title(self, expected_text: str):
        self.verify_text(expected_text, *self.SEARCH_TITLE)

    def click_list_item(self, index: int):
        self.click_list_element(index, *self.PRODUCT_LIST_LINK_LOCATOR)
        sleep(2)

    def add_to_cart_click(self):
        model = self.driver.find_element(*self.PRODUCT_TITLE_LOCATOR).text
        f = open("products_name.txt", "a")
        f.write(model + "\n")
        f.close()
        self.click(*self.ADD_TO_CART_BUTTON)

    def click_go_to_cart(self):
        self.wait_for_element_appear(*self.ADDED_TO_CART_LABEL)
        self.click(*self.GO_TO_CART_BUTTON)