from AutomationFramework.PageObjects.BasePage import BasePage
from AutomationFramework.Resources.Locators import Locators


class ProductPage(BasePage):
    """Product Page of xyz.com"""
    def __init__(self, driver):
        super.__init__(driver)

    def search_product(self, product):
        self.clear(Locators.SEARCH_TEXTBOX)
        self.enter_text(Locators.SEARCH_TEXTBOX, product)

    def add_product(self):
        self.click(Locators.ADD_BUTTON)

    def click_checkout(self):
        self.click(Locators.CHECKOUT_BUTTON)