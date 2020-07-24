from selenium import webdriver
import time


class Configg:
    def __init__(self, driver):
        self.driver = driver

    def driver_setup(self):
        self.driver = webdriver.Chrome("C://Users//user//Amazon//drivers//chromedriver.exe")
