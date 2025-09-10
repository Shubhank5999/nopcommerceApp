import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen ()
    # Logger
    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("******** SearchCustomerByEmail_004 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp =LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("** ** * Loginsuccesful ** ** ** ** ** ")
        self.logger.info("******* Starting Search Customer By Email **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenue()
        self.addcust.clickOnCustomerMenueItem()

        self.logger.info("** ******* searching customer by emailID **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("steve")
        searchcust.setLastName("Gates")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("Steve Gates")
        assert True == status
        self.driver.close()
        self.logger.info("*************** TC_SearchCustomerByEmail_005 closed ***********")
        self.logger.info("*************** TC_SearchCustomerByEmail_005 Finished ***********")
