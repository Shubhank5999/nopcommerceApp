import time

import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import ExcelUtils
"""
Why we are importing Login class as we want to use action methods define in Login and 
both classes are in different package
"""
#Step3
class Test_002_login:
    #STEP 8, step 9 adding logs
    baseURL = ReadConfig.getApplicationURL()
    path = ".//testData/LoginData.xlsx"
    sheet = 'Sheet1'
    logger = LogGen.loggen()


#step 4

    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("*************** Test_002_login *****************")
        self.logger.info("*************** verifying login test *****************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = ExcelUtils.getRowCount(self.path,self.sheet)
        print(f"No of rows in excel are : {self.rows}")
        lst_status = []
        for r in range(2,self.rows+1):
            self.user = ExcelUtils.readData(self.path,self.sheet,r,1)
            self.password = ExcelUtils.readData(self.path,self.sheet,r,2)
            self.exp = ExcelUtils.readData(self.path,self.sheet,r,3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            actTitle=self.driver.title
            expTitle = "Dashboard / nopCommerce administration"
            if expTitle==actTitle:
                if self.exp== "Pass":
                    self.logger.info('**********************Login test case passed************************')
                    self.lp.clicklogout()
                    lst_status.append('Pass')
                elif self.exp=='Fail':
                    self.logger.info('**********************Login test case passed************************')
                    self.lp.clicklogout()
                    lst_status.append('Fail')
            elif actTitle != expTitle:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
        if 'Fail' not in lst_status:
            self.logger.info("************DDT got passed ********************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************DDT got failed ********************")
            self.driver.close()
            assert False
        self.logger.info("**************End of login DDT test ********************")
        self.logger.info("************** Completed Test_002_login ********************")



