# import time

# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from utilities.Logger import Logging_Class
# from pageobjects.admin_login import Login_adminPage
# import os
# from dotenv import load_dotenv
# load_dotenv()


# class Testlogin:
#     admin_page_url =os.getenv('admin_page_url')
#     log = Logging_Class.log_genarator()
#     path=".//Testdata//TestData_AutomationStore.xlsx"
#     def test_validadminlogin_DataDriven(self,setup):
#         self.driver =setup
#         self.driver.implicitly_wait(10)
#         self.log.info("opening Automation store url")
#         self.driver.get(self.admin_page_url)
#         self.driver.maximize_window()
#         self.lap = Login_adminPage(self.driver)
#         self.log.info("Entering Username")
#         self.lap.enter_username(self.username1)
#         self.log.info("Entering Password")
#         self.lap.enter_password(self.password1)
#         self.lap.click_login()
#         act_title = self.driver.title
#         exp_title = "My Account"
#         if exp_title == act_title:
#             assert True
#             self.driver.close()
#         else:
#             self.driver.save_screenshot(".\\Screenshot\\test_validadminlogin.png")
#             self.driver.close()
#             assert False
