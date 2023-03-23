from features.pages.login_page import LoginPage
from features.pages.onboarding_page import OnboardingPage


class Application:
    def __init__(self, driver):
        self.login_page = LoginPage(driver)
        self.onboarding_page = OnboardingPage(driver)
