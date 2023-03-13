from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Clase conteniendo todos los metodos comunes


class Page:
    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, filename):
        filename = filename.replace('<', '').replace('>', '').replace('"', '').replace(' ', '_')
        self.driver.save_screenshot('./features/screenshot/' + filename + '.png')

    def find_elements(self, locator):
        try:
            return self.driver.find_elements(by=locator[0],
                                         value=locator[1])
        except NoSuchElementException as ex:
            print(ex)

    def find_element(self, locator):
        return self.driver.find_element(by=locator[0],
                                        value=locator[1])

    def click_on_element(self, locator):
       self.find_element(locator).click()
       
    def input(self, text, locator):
        password_input = self.find_element(locator)
        password_input.send_keys(text)

    def clear_text(self, locator):
       self.find_element(locator).clear()

    def enter_text(self, locator, text):
       self.clear_text(locator)    
       self.find_element(locator).send_keys(text)
