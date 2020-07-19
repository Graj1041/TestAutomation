class CommonUtility():

    def __init__(self, driver):
        self.driver = driver

    def capture_screenshot(self, path):
        self.driver.get_screenshot_as_file(path)