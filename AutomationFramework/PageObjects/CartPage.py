from AutomationFramework.PageObjects.BasePage import BasePage
from AutomationFramework.Resources.Locators import Locators


class CartPage(BasePage):
    """Cart checkout page of xyz.com"""
    def __init__(self, driver):
        super.__init__(driver)

    def set_customer_name(self, name):
        self.clear(Locators.NAME_TEXTBOX)
        self.enter_text(Locators.NAME_TEXTBOX, name)

    def set_customer_mobile(self, mobile):
        self.clear(Locators.MOBILE_TEXTBOX)
        self.enter_text(Locators.MOBILE_TEXTBOX, mobile)

    def set_customer_address(self, address):
        self.clear(Locators.ADDRESS_TEXTBOX)
        self.enter_text(Locators.ADDRESS_TEXTBOX, address)

    def click_submit(self):
        self.click(Locators.SUBMIT_BUTTON)

    def click_otp(self):
        self.click(Locators.OTP_BUTTON)

    def click_pay(self):
        self.click(Locators.PAY_BUTTON)
