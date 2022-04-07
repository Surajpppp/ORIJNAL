import pytest
from selenium import webdriver
from pageobjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen


class TestCase001:
    urls = ReadConfig.getapplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_title(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("*******opening url**********")
        self.driver.maximize_window()
        self.driver.get(self.urls)
        self.logger.info("*******getting title of title page**********")
        title = self.driver.title
        if title == "Your store. Login":
            self.logger.info("*******verifying title page pass**********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshorts\\" + "test_title.png", )
            self.logger.info("*******verifying title page fail**********")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.logger.info('*******test_login**********')
        self.logger.info('*******starting_url**********')
        self.driver.get(self.urls)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.logger.info('*******inserting username**********')
        self.lp.setUserName(self.username)
        self.logger.info('*******inserting password**********')
        self.lp.setPassword(self.password)
        self.logger.info('*******clicking on login button**********')
        self.lp.Login()
        self.logger.info('*******getting title of title page**********')
        title1 = self.driver.title

        if title1 == "Dashboard / nopCommerce administration":
            self.logger.info('*******test_login pass**********')
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\screenshorts\\" + "test_login.png", )
            self.logger.info('*******test_login fail**********')
            self.driver.close()
            assert False
