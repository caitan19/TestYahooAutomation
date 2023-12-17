import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from base.base_driver import BaseDriver

from utilities.utils import Utils


class LoginPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    USERNAME_TEXTBOX_FIELD = "//input[@id='login-username']"
    PASSWORD_TEXTBOX_FIELD = "//input[@id='login-passwd']"
    USERNAME_TXT_FIELD = "//*[contains(text(),'Sign in to Yahoo') or contains(text(),'Enter')]"
    PASSWORD_TXT_FIELD = "//*[contains(text(),'Enter')]"
    LOGIN_TITLE_FIELD = "//title"

    # Methods to get the fields
    def getUsernameField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.USERNAME_TEXTBOX_FIELD)

    def getPasswordField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PASSWORD_TEXTBOX_FIELD)

    def getLoginPageTitleField(self):
        return self.wait_for_presence_of_element(By.XPATH, self.LOGIN_TITLE_FIELD)

    def getUsernameTextField(self):
        return self.wait_for_presence_of_element(By.XPATH, self.USERNAME_TXT_FIELD)

    def getPasswordTextField(self):
        return self.wait_for_presence_of_element(By.XPATH, self.PASSWORD_TXT_FIELD)


    # Methods to perform the tests
    def inputUsername(self, username_input):
        username = self.getUsernameField()
        #self.driver.execute_script("arguments[0].click()", source)
        time.sleep(2)
        username.send_keys(username_input)
        username.send_keys(Keys.ENTER)

    def inputPassword(self, password_input):
        password = self.getPasswordField()
        #self.driver.execute_script("arguments[0].click()", source)
        time.sleep(2)
        password.send_keys(password_input)
        password.send_keys(Keys.ENTER)

    def extractTitle(self):
        page_title = self.driver.title #self.getLoginPageTitleField().text
        return page_title

    def extractUsernameText(self):
        username_error = self.getUsernameTextField().find_element(By.XPATH, self.USERNAME_TXT_FIELD).text
        return username_error

    def extractPasswordText(self):
        password_error = self.getPasswordTextField().find_element(By.XPATH, self.PASSWORD_TXT_FIELD).text
        return password_error


    def UsernameCheck(self, username_input):
        self.inputUsername(username_input)
        time.sleep(5)
        username_text = self.extractUsernameText()
        return username_text

    def PasswordCheck(self, password_input):
        self.inputPassword(password_input)
        page_title = self.extractTitle()
        return page_title
