from features.pages.base_page import Page
from selenium.webdriver.common.by import By


class LoginPage(Page):

    # Locator values in Login page
    _USER_NAME_INPUT = (By.ID, 'tiet_sign_in_username')
    _PASSWORD_INPUT = (By.ID, 'tiet_sign_in_password')
    _LOGIN_BUTTON = (By.ID, 'btn_sign_in_button')

    def enter_username(context, text):
        context.enter_text(context._USER_NAME_INPUT, text)

    def enter_password(context, text):
        context.enter_text(context._PASSWORD_INPUT, text)

    def click_login_button(context):
        context.click_on_element(context._LOGIN_BUTTON)

    def navigateBack(context):
        print(' entered navigate back')
        context.driver.implicitly_wait(20)
        context.driver.back()
