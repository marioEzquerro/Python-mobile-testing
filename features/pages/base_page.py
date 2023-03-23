from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            return self.driver.find_element(by=locator[0], value=locator[1])
        except NoSuchElementException as ex:
            print(ex)

    def enter_text(self, locator, text):
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(text)

    def click_element(self, locator):
        self.find_element(locator).click()

    def element_is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            element.is_displayed()
            return True
        except NoSuchElementException:
            return False
            
