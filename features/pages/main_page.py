from selenium.webdriver.common.by import By
from features.pages.base_page import Page

class MainPage(Page):
    USER_ICON_LIST = (By.ID, "com.instagram.android:id/username")
    TAB_BAR = (By.ID, "com.instagram.android:id/tab_bar")
    LINER_BAR = (By.CLASS_NAME, "android.widget.FrameLayout")

    def verify_main_page_is_open(self):
        assert False