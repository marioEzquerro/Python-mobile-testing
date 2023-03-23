from features.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    _USERNAME_INPUT = (By.ID, 'tiet_sign_in_username')
    _PASSWORD_INPUT = (By.ID, 'tiet_sign_in_password')
    _SUBMIT_BUTTON = (By.ID, 'btn_sign_in_button')

    def user_in_login_page(self):
       return self.element_is_visible(self._USERNAME_INPUT)

    def enter_username(self, text):
        self.enter_text(self._USERNAME_INPUT, text)

    def enter_password(self, passw):
        self.enter_text(self._PASSWORD_INPUT, passw)

    def click_login(self):
        self.click_element(self._SUBMIT_BUTTON)
