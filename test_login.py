import pytest
import time
from selenium import webdriver
from PageObjects.LoginPage import Login

class Test_001_Login:
    baseURL = "https://www.cansrdev.com/clinical/dashboard/"
    username = 'joercampell1@yopmail.com'
    password = "Joe123!"

    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="Cansr | Login":
            assert True
        else:
            assert False

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        time.sleep(6)
        act_title = self.driver.title

        if act_title=="Cansr.com":
            assert True
        else:
            assert  False


