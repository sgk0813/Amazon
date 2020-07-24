class Home:

    def __init__(self, driver):
        self.driver = driver

        self.sign_out_button_xpath = '//*[@id="nav-item-signout"]'

    def click_sign_out(self):
        self.driver.find_element_by_xpath(self.sign_out_button_xpath)