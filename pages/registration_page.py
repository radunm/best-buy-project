from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class RegistrationPage(Page):

    CREATE_ACCOUNT_TITLE = (By.CSS_SELECTOR, ".cia-main-content h1")
    FIRST_NAME = (By.CSS_SELECTOR, ".cia-main-content h1")
    LAST_NAME = (By.CSS_SELECTOR, ".cia-main-content h1")
    EMAIL = (By.CSS_SELECTOR, ".cia-main-content h1")
    PASSWORD = (By.CSS_SELECTOR, ".cia-main-content h1")
    CONF_PASSWORD = (By.CSS_SELECTOR, ".cia-main-content h1")
    PHONE = (By.CSS_SELECTOR, ".cia-main-content h1")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, ".cia-create-account-form > button")
    INPUT_LIST = (By.CSS_SELECTOR, ".cia-create-account-form input.cia-form__field:not([placeholder='Optional'])")
    input_list_locator = [".cia-main-content h1"]
    data_list = ["David", "Ross", "ross@gmail.com", "rTY5d,+)(*vbgf1", "rTY5d,+)(*vbgf1", "415", "608", "2459"]

    def verify_page(self):
        title = self.driver.find_element(*self.CREATE_ACCOUNT_TITLE).text
        assert 'Create an Account' in title, f'Expected text "Create an Account", but got {title}'

    def fill_data(self):
        field_list = self.driver.find_elements(*self.INPUT_LIST)

        data_to_fill = 0
        for field in field_list:
            if field.get_attribute('name') == 'phone':
                field.clear()
                field.click()
                for phone_digit in range(5, 8):
                    field.send_keys(self.data_list[phone_digit])
                break
            field.clear()
            field.send_keys(self.data_list[data_to_fill])
            data_to_fill += 1

    def click_create_account(self):
        field_list = self.driver.find_elements(*self.INPUT_LIST)
        for field in field_list:
            d = field.get_attribute('value')
            print(field.get_attribute('value'))
        sleep(4)
        self.click(*self.CREATE_ACCOUNT_BUTTON)