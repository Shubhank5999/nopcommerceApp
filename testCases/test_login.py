import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
"""
Why we are importing Login class as we want to use action methods define in Login and 
both classes are in different package
"""
#Step3
class Test_001_login:
    # baseURL = "https://admin-demo.nopcommerce.com/"
    # username = "admin@yourstore.com"
    # password = "admin"
    #STEP 8, step 9 adding logs
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    #calling loggen method using class name as it is a static method making it a class level here so we need to use self

#Login test is a main test so it will come under sanity and normal data driven test come under regression.
#these are user defined so we need make pytest.ini to put all markers there

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("*******************Test_001_login**********************")
        self.logger.info("*********************** Verifying home page title *****************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="nopCommerce demo store. Login":
            self.driver.close()
            self.logger.info('****************Home page title got passed ********************')
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.logger.error('****************Home page title got failed ********************')
            self.driver.close()
            assert False

#step 4

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*************** verifying login test *****************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        act_title = self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            self.logger.info("*************** login test is passed *****************")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(r"C:\Users\hp\PycharmProjects\nopcommerceApp\Screenshots\\"+"test_login.png")
            self.logger.error("*************** login test is failed *****************")
            self.driver.close()
            assert False
        """
            By attaching lp to self, you make it an instance variable of the test class.
            Now, other methods inside the same class can access it:
        """
