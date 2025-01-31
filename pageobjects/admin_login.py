from selenium.webdriver.common.by import By


class Login_adminPage:
    textbox_username_id = "//input[@id='loginFrm_loginname']"
    textbox_passwords_id = "//input[@id='loginFrm_password']"
    Login_btn = "//button[normalize-space()='Login']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_passwords_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_passwords_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.Login_btn).click()
