from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OnboardingPage(BasePage):

    _WELCOME_MESSAGE = (By.ID, "tv_onboarding_title")

    def user_in_onboarding_page(self):
        return self.element_is_visible(self._WELCOME_MESSAGE)
