#Step 7
import configparser

config = configparser.RawConfigParser()
"""
    RawConfigParser class has few method which can help us to read data from .ini file
    making it static so that we can use it via class name without creating object
"""
config.read(".\\Configurations\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get("common info","baseURL")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("common info","useremail")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info","password")
        return password
