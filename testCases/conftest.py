from selenium import webdriver
import pytest

#Step 5
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser ****************")
    elif browser =='edge':
        driver = webdriver.Edge()
        print("Launching edge browser ****************")
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser): #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  #This will return browser value to setup method
    return request.config.getoption("--browser")


# PyTest HTML Report ##
#It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {
        "Project Name": "nopcommerceApp",
        "Module Name": "Customers",
        "Tester": "Pavan"
    }

#It is hook for delete/Modify Environment info to HTML Report i.e removing few default details
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA HOME", None)
    metadata.pop("Plugins", None)


"""
    These method will get browser name i.e chrome/edge from command prompt
    pytest -v -s testCases/test_login.py --browser chrome
    pytest -v -s testCases/test_login.py --browser edge

    What it means?    
        pytest_addoption is a special pytest hook function.
        Pytest will automatically look for this function inside your conftest.py file.
        It allows you to add your own custom command-line options when running pytest. 

        parser.addoption("--browser")
        This registers a new option called --browser that you can pass from the command line.
    for || execution
    COMMAND : pytest -v -s testCases/test_login.py --browser chrome -n 4
"""