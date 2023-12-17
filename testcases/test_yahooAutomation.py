import time

import pytest
import softest
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.yahoo_change_pswd_page import ChangePasswd
from pages.yahoo_inbox_page import InboxPage
from pages.yahoo_login_page import LoginPage
from pages.yahoo_sent_mail_page import SendMail
from utilities.utils import Utils
from ddt import ddt, data, file_data, unpack


@pytest.mark.usefixtures("setup")
@ddt()
class TestEmailVerification(softest.TestCase):
    log = Utils.custom_logger()

    # @data(("caitan1wwww9@yahoo.com", "3Dsystems#1"), ("caitan19@yahoo.com", "3Dsysstems#1"), ("caitan19@yahoo.com", "3Dsystems#1"))
    # @unpack
    @file_data("../Testdata/testData.json")
    def test_write_and_send_email(self, username_input, password_input, recipient, subject, body):
        yahoo_asserts = Utils()
        lp = LoginPage(self.driver)
        un_check = lp.UsernameCheck(username_input)
        yahoo_asserts.assertUsername(un_check)
        pw_check = lp.PasswordCheck(password_input)
        yahoo_asserts.assertPassword(pw_check)
        inbox_page = InboxPage(self.driver)
        unique_email_subject = inbox_page.WriteAndSendEmail(recipient, subject, body)
        self.log.debug(unique_email_subject)
        sml = SendMail(self.driver)
        sent_emails_list = sml.checkSentMail()
        yahoo_asserts.assertSentMail(sent_emails_list, unique_email_subject)

    @file_data("../Testdata/testDataAdvSearch.json")
    def test_advanced_search_sent_mails(self, username_input, password_input, recipient):
        yahoo_asserts = Utils()
        lp = LoginPage(self.driver)
        un_check = lp.UsernameCheck(username_input)
        yahoo_asserts.assertUsername(un_check)
        pw_check = lp.PasswordCheck(password_input)
        yahoo_asserts.assertPassword(pw_check)
        sml = SendMail(self.driver)
        sent_emails_recp_list = sml.advanceSearchOfSentMails(recipient)
        # if_empty = sml.getSentBoxEmptyMsg().text
        yahoo_asserts.assertAdvanceSerachToList(recipient,sent_emails_recp_list)

    @pytest.mark.change_passwrd
    @file_data("../Testdata/testChangePasswd.json")
    def test_change_passwd(self, username_input, password_input, new_passwd):
        yahoo_asserts = Utils()
        lp = LoginPage(self.driver)
        un_check = lp.UsernameCheck(username_input)
        yahoo_asserts.assertUsername(un_check)
        pw_check = lp.PasswordCheck(password_input)
        yahoo_asserts.assertPassword(pw_check)
        inbox_page = InboxPage(self.driver)
        inbox_page.clickAccOpenerLink()
        inbox_page.clickAccInfoLink()
        chang_passwd = ChangePasswd(self.driver)
        chang_passwd.switch_browser_tabs(1, "descendant")  # switch to newly opened tab
        chang_passwd.setNewPassword(new_passwd)
        inbox_page.switch_browser_tabs(0, "ancestor")  # switch to parent tab
        inbox_page.clickAccOpenerLink()
        inbox_page.clickAccInfoLink()
        inbox_page.clickSignOut()

    @pytest.mark.change_passwrd
    @file_data("../Testdata/testChangePasswd.json")
    def test_verify_changed_psswd(self, username_input, password_input, new_passwd):
        yahoo_asserts = Utils()
        lp = LoginPage(self.driver)
        un_check = lp.UsernameCheck(username_input)
        yahoo_asserts.assertUsername(un_check)
        pw_check = lp.PasswordCheck(new_passwd)
        yahoo_asserts.assertPassword(pw_check)
