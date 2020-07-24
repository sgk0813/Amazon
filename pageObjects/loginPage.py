
class Login:

    def __init__(self, driver):
        self.driver = driver

        self.sign_in_button_xpath = "//*[@id='nav-flyout-ya-signin']/a/span"
        self.Continue_click_button_xpath = "//*[@id='continue']"
        self.submit_button_xpath = '//*[@id="signInSubmit"]'

    def get_url(self):
        self.driver.get("https://www.amazon.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def click_sign_in(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()

    def click_continue(self):
        self.driver.find_element_by_xpath(self.Continue_click_button_xpath).click()

    def click_submit(self):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()


