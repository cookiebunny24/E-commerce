import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    logger = LogGen.loggen()
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    def test_homePageTitle(self, setup):
        self.logger.info("**********Test_001_Login****************")
        self.logger.info("**********Home Page test****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.set_page_load_timeout(80000)
        ac_title = self.driver.title
        print(ac_title)
        if ac_title == "Your store. Login":
            self.logger.info("**********Homepage title passed****************")
            assert True
            self.driver.close()
        else:
            self.logger.error("**********Homepage Title failed****************")
            self.driver.save_screenshot(".//Screenshots//"+"titlePage.png")
            assert False
            self.driver.close()

    def test_login(self, setup):
        self.logger.info("**********Test_002_Login****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.set_page_load_timeout(80000)
        self.lp = Login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        ac_title = self.driver.title
        if ac_title == "Dashboard / nopCommerce administration":
            self.logger.info("**********Login Passed****************")
            assert True
            self.driver.close()
        else:
            self.logger.error("**********Login Failed****************")
            self.driver.save_screenshot(".//Screenshots//"+"test_homepage.png")
            assert False
            self.driver.close()
