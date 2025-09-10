from selenium import webdriver
from selenium.webdriver.common.by import By
class LoginPage:

    #STEP 1     Identifying locators for all the element for login and logout
    """
    these are class level variable so we need to access them using self or class name when accessing them inside method like setUserName
    self. is preferred in Page Object Model
    """
    textbox_username_id ="Email"
    textbox_password_id ="Password"
    button_login_xpath = "//*[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    # STEP2 creating action method
    """   
    Now we need to implement action items for all the locators before that we need to initialize the driver
    What this constructor is doing
    it will capture driver from test case and that driver we will initiate to class level so self.driver will have the value of driver
    passed through our TC
    and thats why we will use self.driver every where and here to implement action methods """
    def __init__(self,driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
        """
        We don’t use self for username because it’s just a method parameter passed from the test case.
        username is a local variable
        """
    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def clicklogout(self):
        self.driver.find_element(By.LINK_TEXT,self.link_logout_linktext).click()