from selenium import webdriver
from AutomationFramework.PageObjects import LoginPage, ProductPage, CartPage
from AutomationFramework.Resources.TestData import TestData
import pytest
import HtmlTestRunner


class OrderProductTest():

    @pytest.fixture(scope="module")
    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=chrome_options,
                                       executable_path=TestData.CHROME_EXECUTABLE_PATH)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        yield
        self.driver.close()

    def test_login(self, setup):
        lp = LoginPage(self.driver)
        lp.set_user_name(TestData.USER_NAME)
        lp.set_password(TestData.USER_PASSWORD)
        '''
        As we know CAPTCHA images are not meant to be automated,it is implemented to prevent automation.
        We can use any third party APIs(like deathByCaptcha,antiCaptcha) to automate it or 
        we can give a wait time to take user input and proceed.
        But in Testing Environment, we can ask developer to either disable it or generate an API of CAPTCHA generation.    
        '''
        lp.click_login()
        self.assertEqual("Product Board", self.driver.title, "web page title is not matching")

    def test_add_product(self, setup):
        pp = ProductPage(self.driver)
        pp.search_product(self.product)
        pp.add_product()
        pp.click_checkout()
        self.assertEqual("Cart", self.driver.title, "Item is not displayed in cart")

    def test_order_product(self, setup):
        cp = CartPage(self.driver)
        cp.set_customer_name(self.name)
        cp.set_customer_address(self.address)
        cp.set_customer_mobile(self.mobile)
        cp.click_submit()
        cp.click_otp()
        cp.click_pay()
        self.assertEqual("Order Success", self.driver.title, "Your order is not placed successfully")


if __name__ == '__main__':
    pytest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='..\\Reports'))