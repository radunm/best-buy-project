from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):

    WRITE_REVIEW_BUTTON = (By.CSS_SELECTOR, ".see-all-reviews-button-container a.write-a-review")
    REVIEW_BUTTON = (By.CSS_SELECTOR, ".user-generated-content-ratings-and-reviews .c-accordion-trigger")

    def review_click(self):
        self.click(*self.REVIEW_BUTTON)

    def verify_button(self, expected_text: str):
        self.verify_text(expected_text, *self.WRITE_REVIEW_BUTTON)