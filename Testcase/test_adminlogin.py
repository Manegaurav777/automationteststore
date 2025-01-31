import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.Logger import Logging_Class
from pageobjects.admin_login import Login_adminPage
import os
from dotenv import load_dotenv
load_dotenv()


class Testlogin:
    admin_page_url =os.getenv('admin_page_url')
    username1 =os.getenv('username1')
    password1 = os.getenv('password1')
    invalid_username = os.getenv('invalid_username')
    log = Logging_Class.log_genarator()

    def test_verifytitle(self,setup):
        self.driver = setup
        self.log.info("opening Automation store url")
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        act_title = self.driver.title
        exp_title = "Account Login"
        if exp_title == act_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_verifytitle.png")
            self.driver.close()
            assert False

    def test_validadminlogin(self,setup):
        self.driver =setup
        self.log.info("opening Automation store url")
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.lap = Login_adminPage(self.driver)
        self.log.info("Entering Username")
        self.lap.enter_username(self.username1)
        self.log.info("Entering Password")
        self.lap.enter_password(self.password1)
        self.lap.click_login()
        act_title = self.driver.title
        exp_title = "My Account"
        #act_dashboard_text = self.driver.find_element(By.XPATH, "//a[normalize-space()='Apparel & accessories']").text
        if exp_title == act_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_validadminlogin.png")
            self.driver.close()
            assert False

    def test_invalidCred(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.maximize_window()
        self.lap = Login_adminPage(self.driver)
        self.lap.enter_username(self.invalid_username)
        self.lap.enter_password(self.password1)
        self.lap.click_login()
        act_title = self.driver.title
        exp_title = "Account Login"
        if exp_title == act_title:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshot\\test_invalidCred.png")
            self.driver.close()
            assert False

