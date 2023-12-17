import time

from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver
from utilities.utils import Utils


class SendMail(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    SENT_MAIL_LINK_FIELD = "//span[contains(text(),'Sent')]"
    SENT_EMAILS_LIST = "//div[@data-test-id='virtual-list-container']//div//div[@data-test-id='virtual-list']/ul/li//span[@data-test-id='message-subject']" #"//div[@data-test-id='virtual-list-container']//div//div[@data-test-id='virtual-list']/ul/li//span[contains(text(),'Test subject_')]"
    SENT_EMAILS_TO_RECP_LIST = "//div[@data-test-id='virtual-list-container']//div//div[@data-test-id='virtual-list']/ul/li//span/span"
    ADV_SEARCH_TOGGLE_FIELD = "//button[@title='Toggle advanced search pane']"
    ADV_SEARCH_TO_FIELD = "//input[@aria-owns='react-typehead-list-adv-search-to']"
    #ADV_SEARCH_BTN = "//button[@data-test-id='search-basic-btn']"
    SENT_BOX_EMPTY_FILED = "//span[normalize-space()='Nothing to see here.']"

    # Methods to get the fields
    def getSentMailLink(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SENT_MAIL_LINK_FIELD)

    def getSentMailsList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SENT_EMAILS_LIST)

    def getSentMailsRecpList(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.SENT_EMAILS_TO_RECP_LIST)

    def getAdvanceSearchToggle(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADV_SEARCH_TOGGLE_FIELD)

    def getAdvanceSearchToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ADV_SEARCH_TO_FIELD)

    def getSentBoxEmptyMsg(self):
        return self.wait_for_presence_of_element(By.XPATH, self.SENT_BOX_EMPTY_FILED)

    # Methods to perform the tests
    def clickSentMailsLink(self):
        sent_link = self.getSentMailLink()
        self.driver.execute_script("arguments[0].click()", sent_link)

    def clickAdvSearchToggle(self):
        adv_search = self.getAdvanceSearchToggle()
        self.driver.execute_script("arguments[0].click()", adv_search)

    def inputAdvSearchTo(self, recipient_email):
        self.getAdvanceSearchToField().click()
        self.getAdvanceSearchToField().send_keys(recipient_email)
        self.getAdvanceSearchToField().send_keys(Keys.ENTER)

    '''def clickAdvSearchBtn(self):
        self.getAdvanceSearchBtn().click()
        self.getAdvanceSearchBtn().click()'''

    # Check sent mail method
    def checkSentMail(self):
        self.clickSentMailsLink()
        sent_emails_list = self.getSentMailsList()
        return sent_emails_list

    def advanceSearchOfSentMails(self, recipient_email):
        self.clickSentMailsLink()
        time.sleep(2)
        self.clickAdvSearchToggle()
        self.inputAdvSearchTo(recipient_email)
        time.sleep(5)
        sent_mail_recp_list = self.getSentMailsRecpList()
        # self.clickAdvSearchBtn()
        return sent_mail_recp_list

