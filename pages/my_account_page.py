from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AccountPage(Page):

    NAME_TITLE_LOCATOR = (By.CSS_SELECTOR, ".shop-welcome-banner .welcome-banner__user-name")

    def verify_registration(self, *expected_text: str):
        self.verify_text(*expected_text, *self.NAME_TITLE_LOCATOR)