from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.driver.wait = WebDriverWait(self.driver, 15)

    def open_page(self, url):
        self.driver.get(url)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def click_list_element(self, list_index: int, *locator):
        e = self.driver.find_elements(*locator)[list_index]
        e.click()

    def input_text(self, text: str, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def wait_for_element_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_element_to_be_clickable(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_all_elements_appear(self, *locator):
        self.driver.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_text_element(self, *locator, text: str):
        self.driver.wait.until(EC.text_to_be_present_in_element_value(locator, text))

    def verify_text(self, expected_text: str, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def count_elements(self, expected_value: int, *locator):
        actual_value = int(len(self.driver.find_elements(*locator)))
        assert actual_value == int(expected_value), f'Expected {expected_value} elements, but got {actual_value} elements'