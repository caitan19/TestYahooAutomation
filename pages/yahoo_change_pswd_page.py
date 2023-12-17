import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class ChangePasswd(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    '''ACC_MENU_OPENER_FIELD = "//label[@id='ybarAccountMenuOpener']"
    ACC_INFO_FIELD = "//a[normalize-space()='Account info']"'''
    ACC_SEC_FIELD = "//a[contains(text(),'Security')]"
    CHANGE_PASSWD_FIELD = "//a[normalize-space()='Change password']"
    NEW_PASSWD_FIELD = "//input[@id='createNPwdTxtField']"
    SET_NEW_PASSWD_BTN = "//button[@id='btnCnpContinue']"
    #SIGN_OUT_FIELD = "//span[contains(text(), 'Sign out')]"

    # Methods to get the fields
    '''def getAccOpenerLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACC_MENU_OPENER_FIELD)

    def getAccInfoLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACC_INFO_FIELD)'''

    def getAccSecLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACC_SEC_FIELD)

    def getChangePasswdLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHANGE_PASSWD_FIELD)

    def getNewPasswdLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.NEW_PASSWD_FIELD)

    def getContinueBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SET_NEW_PASSWD_BTN)

    '''def getSignOutBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SIGN_OUT_FIELD)'''

    # Methods to perform the tests
    '''def clickAccOpenerLink(self):
        acc_opener_link = self.getAccOpenerLink()
        self.driver.execute_script("arguments[0].click()", acc_opener_link)

    def clickAccInfoLink(self):
        acc_info_link = self.getAccInfoLink()
        self.driver.execute_script("arguments[0].click()", acc_info_link)'''

    def clickAccSecLink(self):
        self.getAccSecLink().click()

    def clickChangePsswdLink(self):
        self.getChangePasswdLink().click()

    def setNewPsswd(self, new_passwd):
        self.getNewPasswdLink().click()
        self.getNewPasswdLink().send_keys(new_passwd)

    def clickContinue(self):
        self.getContinueBtn().click()

    '''def clickSignOut(self):
        self.getSignOutBtn().click()'''

    # Change password method
    def setNewPassword(self, new_passwd):
        self.clickAccSecLink()
        time.sleep(5)
        self.clickChangePsswdLink()
        self.setNewPsswd(new_passwd)
        self.clickContinue()
        time.sleep(3)
        #self.driver.close()
