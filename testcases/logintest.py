import unittest
import time
from selenium.webdriver import ActionChains
from pageObjects.homePage import Home
from pageObjects.config import Configg
from pageObjects.loginPage import Login
from testcases import XLUtils


class LoginTest(unittest.TestCase):

    def test_sign_in(self):
        path = "D://Test Data//Credentials.xlsx"
        row = XLUtils.get_row_count(path, "Sheet1")

        for r in range(2, row + 1):
            conf = Configg(self)
            conf.driver_setup()
            login = Login(conf.driver)
            login.get_url()
            actions = ActionChains(conf.driver)
            hover = conf.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
            conf.driver.implicitly_wait(5)
            actions.move_to_element(hover).perform()
            # sign_in = self.driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span').click()
            sign_in = login.click_sign_in()
            username = XLUtils.read_data(path, "Sheet1", r, 1)
            password = XLUtils.read_data(path, "Sheet1", r, 2)
            conf.driver.find_element_by_id('ap_email').send_keys(username)
            # self.driver.find_element_by_xpath('//*[@id="continue"]').click()
            login.click_continue()
            username_error = conf.driver.find_element_by_xpath("//h4[@class='a-alert-heading']")
            time.sleep(2)
            if username_error.is_displayed():
                username_screenshot = conf.driver.save_screenshot(
                    'C://Users//user//PycharmProjects//Tests//Reports//Screenshots//Username_error.png')
                print("Test Failed")
                XLUtils.write_data(path, "Sheet1", r, 3, "Test Failed")
                conf.driver.quit()
            else:
                conf.driver.find_element_by_id('ap_password').send_keys(password)
                time.sleep(1)
                # self.driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
                login.click_submit()
                time.sleep(2)

                if conf.driver.title == "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more":
                    print("Test passed.")
                    XLUtils.write_data(path, "Sheet1", r, 3, "Test Passed")
                    homepage = Home(conf.driver)
                    action1 = ActionChains(conf.driver)
                    hover2 = conf.driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
                    action1.move_to_element(hover2).perform()
                    # sign_out = self.driver.find_element_by_xpath('//*[@id="nav-item-signout"]').click()
                    sign_out = homepage.click_sign_out()
                    conf.driver.quit()
                else:
                    print("Test Failed")
                    password_screenshot = conf.driver.save_screenshot(
                        'C://Users//user//PycharmProjects//Tests//Reports//Screenshots//Password_error.png')
                    XLUtils.write_data(path, "Sheet1", r, 3, "Test Failed")
                    conf.driver.quit()


if __name__ == "__main__":
    unittest.main()
