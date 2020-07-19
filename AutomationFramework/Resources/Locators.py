from selenium.webdriver.common.by import By


class Locators():

    # --- Login Page Locators ---
    USERNAME_TEXTBOX = (By.ID, "Username")
    PASSWORD_TEXTBOX = (By.ID, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='LOG IN']")

    # --- Product Page Locators ---
    SEARCH_TEXTBOX = (By.ID, 'ProductSearch')
    ADD_BUTTON = (By.XPATH, "//div[@class='sg-col-inner']//(add-button)[2]")
    CHECKOUT_BUTTON = (By.XPATH, "//input[@value='CHECK OUT']")

    # --- Cart Page Locators ---
    NAME_TEXTBOX = (By.ID, "Customer")
    MOBILE_TEXTBOX = (By.ID, "Mobile")
    ADDRESS_TEXTBOX = (By.ID, "Address")
    SUBMIT_BUTTON = (By.XPATH, "//input[@value='SUBMIT']")
    OTP_BUTTON = (By.XPATH, "//input[@value='OTP']")
    PAY_BUTTON = (By.XPATH, "//input[@value='PAY']")
