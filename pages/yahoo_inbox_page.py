import time

import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.yahoo_sent_mail_page import SendMail

from base.base_driver import BaseDriver
from utilities.utils import Utils


class InboxPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    COMPOSE_BTN_FIELD = "//a[normalize-space()='Compose']"
    SET_AS_DEFAULT_BTN_FIELD = "//button[normalize-space()='Set as default']"
    MSG_TO_FIELD = "//input[@id='message-to-field']"
    SUBJECT_FIELD = "//input[@placeholder='Subject']"
    MSG_BODY_FIELD = "//div[@aria-label='Message body']"
    SEND_BTN_FIELD = "//span[normalize-space()='Send']"
    ACC_MENU_OPENER_FIELD = "//label[@id='ybarAccountMenuOpener']"
    ACC_INFO_FIELD = "//a[normalize-space()='Account info']"
    SIGN_OUT_FIELD = "//span[contains(text(), 'Sign out')]"

    # Methods to get the fields
    def getComposeBtnField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.COMPOSE_BTN_FIELD)

    def getDefaultBtnField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SET_AS_DEFAULT_BTN_FIELD)

    def getMsgToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MSG_TO_FIELD)

    def getSubjectField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SUBJECT_FIELD)

    def getMsgBody(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.MSG_BODY_FIELD)

    def getSendBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEND_BTN_FIELD)

    def getAccOpenerLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACC_MENU_OPENER_FIELD)

    def getAccInfoLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ACC_INFO_FIELD)

    def getSignOutBtn(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SIGN_OUT_FIELD)

    # Methods to perform the tests
    def clickComposeBtn(self):
        self.getComposeBtnField().click()
        # self.driver.execute_script("arguments[0].click()", source)
        time.sleep(2)

    def selectDefaultMailingType(self):
        self.getDefaultBtnField().click()
        # self.driver.execute_script("arguments[0].click()", destination)

    def inputRecipient(self, recipient_email):
        self.getMsgToField().click()
        self.getMsgToField().send_keys(recipient_email)

    def inputSubject(self, email_subject):
        self.getSubjectField().click()
        current_time = round(time.time() * 1000)
        subject = email_subject + '_' + str(current_time)
        self.getSubjectField().send_keys(subject)
        return subject

    def inputMsgBody(self, email_body):
        self.getMsgBody().click()
        self.getMsgBody().send_keys(email_body)

    def clickSendBtn(self):
        send_btn = self.getSendBtn()
        send_btn.click()

    def clickAccOpenerLink(self):
        acc_opener_link = self.getAccOpenerLink()
        self.driver.execute_script("arguments[0].click()", acc_opener_link)

    def clickAccInfoLink(self):
        acc_info_link = self.getAccInfoLink()
        self.driver.execute_script("arguments[0].click()", acc_info_link)

    def clickSignOut(self):
        self.getSignOutBtn().click()

    # Search flights method
    def WriteAndSendEmail(self, recipient_email, email_subject, email_body):
        yahoo_asserts = Utils()
        self.clickComposeBtn()
        # self.selectDefaultMailingType()
        self.inputRecipient(recipient_email)
        unique_subject = self.inputSubject(email_subject)
        self.inputMsgBody(email_body)
        self.clickSendBtn()
        time.sleep(5)
        return unique_subject
