from AutomationFramework.PageObjects.BasePage import BasePage
from AutomationFramework.Resources.Locators import Locators


class LoginPage(BasePage):
    """Login page of xyz.com"""
    def __init__(self, driver):
        super.__init__(driver)

    def set_user_name(self, username):
        self.clear(Locators.USERNAME_TEXTBOX)
        self.enter_text(Locators.USERNAME_TEXTBOX, username)

    def set_password(self, password):
        self.clear(Locators.PASSWORD_TEXTBOX)
        self.enter_text(Locators.PASSWORD_TEXTBOX, password)

    def click_login(self):
        self.click(Locators.LOGIN_BUTTON)
