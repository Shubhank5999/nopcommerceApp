from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(normalize-space(), 'Customers')]"
    lnkCustomers_menuitem_xpath = "//*[@href='/Admin/Customer/List']//p[contains(normalize-space(), 'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//*[@class='select2-selection__choice'][contains(text(),'Registered')]"
    LstitemAdministrators_xpath = "//li[contains (text(), 'Administrators'))"
    LstitemRegistered_xpath = "//li[@class='select2-results__option'][contains (text(), 'Registered')]"
    LstitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    LstitemVendors_xpath = "//li[contains (text(), 'Vendors')]"
    drpmgr0fVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_id = "Gender_Male"
    rdFeMaleGender_id = "Gender_Female"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    """
        customer role is not a drop down it is a text box and when we click on it it will display some list items
        How we know this as when we add element Select tag is not there in html instead we have li tag
    """

    def __init__(self,driver):  #This driver will come from actual test
        self.driver = driver  #initiating local driver and now this driver belongs to class so we need to access using self

    def clickOnCustomerMenue(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenueItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):#Email will be passed through actual test case
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,passw):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(passw)

    def setCustomerRoles(self, role):
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role =='Registered':
            self.Listitem = self.driver.find_element(By.XPATH,self.LstitemRegistered_xpath)
        elif role=='Administrators':
            self.listitem = self.driver.find_element(By.XPATH,self.LstitemAdministrators_xpath)
        elif role == 'Guests':
            # Here user can be Registered(or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@class='select2-selection__rendered']/li[1]/span[1]")
            self.listitem = self.driver.find_element(By.XPATH,self.LstitemGuests_xpath)
        elif role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH,self.LstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH,self.LstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH,self.LstitemGuests_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.listitem)
            #clicking via JS
    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgr0fVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element(By.ID,self.rdFeMaleGender_id).click()
        else:
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
            self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
            self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)
    def clickOnSave(self):
            self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
    def setAdminContent(self, comname):
            self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(comname)