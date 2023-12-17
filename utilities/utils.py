import inspect
import logging

import softest
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class Utils(softest.TestCase):
    def assertListItemText(self, list, value):
        for item1 in list:
            print("The text is: ", item1.text)
            # self.soft_assert(self.assertEquals, item1.text, value)#assert item1.text == value
            self.soft_assert(self.assertEqual, item1.text, value)  # assert item1.text == value
            # self.soft_assert(self.assertTrue, item1.text == value)
            if item1.text == value:
                print("Test passed")
            else:
                print("Test failed")
        self.assert_all()

    def assertRatingsText(self, list, value):
        rate = value.find("+")
        rate_num = value[0:rate]
        for item1 in list:
            if item1.text != '':
                ind = item1.text.find("/")
                rating = item1.text[0:ind]
                print("The rating is: ", float(rating))
                self.soft_assert(self.assertGreaterEqual, rating, rate_num)
                if float(rating) >= int(rate_num) * 1.0:
                    print("Test passed")
                else:
                    print("Test failed")
        self.assert_all()

    def assertUsername(self, username_field_txt):
        print(username_field_txt)
        if username_field_txt == "Sign in to Yahoo Mail":
            self.assertNotEqual(username_field_txt, "Sign in to Yahoo Mail")
            print("Incorrect username entered. Still on the username input page")
        elif "Enter" in username_field_txt:
            self.assertIn("Enter", username_field_txt)
            print("Correct username entered. Moved to the password input page")

    def assertPassword(self, page_title):
        self.assertIn("caitan19@yahoo.com", page_title)
        if "caitan19@yahoo.com" in page_title:
            print("Correct password entered. Login successful")
        else:
            print("Incorrect password entered. Still on the password input page")

    def assertSentMail(self, sent_emails_list, email_subject):
        for sent_mail in sent_emails_list:
            self.soft_assert(self.assertEqual, sent_mail.text, email_subject)
            if sent_mail.text == email_subject:
                print("Email found in sent box: {0}".format(sent_mail.text))
                break
            else:
                print("Email not found in sent box: {0}".format(sent_mail.text))
        self.assert_all()

    def assertAdvanceSerachToList(self, recipient, sent_emails_recp_list):
        #print("RECPT",sent_emails_recp_list)
        if sent_emails_recp_list is not None:
            for recp in sent_emails_recp_list:
                # self.assertEqual(recp.get_attribute('innerHTML'), recipient)
                # print("TEXT IS {0}: ".format(recp.text))
                self.soft_assert(self.assertEqual, recp.text, recipient)
                if recp.text == recipient:
                    print("Search successful. All emails for {0} found.".format(recp.text))
                    break
                '''else:
                    print("Search unsuccessful. No emails for {0} found.".format(recp.get_attribute('innerHTML')))'''
            # self.assert_all()
        else:
            # self.assertRaises(NoSuchElementException)
            # self.assertNotEqual(if_empty, "Nothing to see here.")
            print("Search unsuccessful. No emails for {0} found.".format(recipient))
            self.assertTrue(False, "Search unsuccessful. No emails for {0} found.".format(recipient))

    def custom_logger(logLevel=logging.DEBUG):
        # Get the function name
        loggerName = inspect.stack()[1][3]
        # create the logger
        logger = logging.getLogger(loggerName)
        logger.setLevel(logLevel)
        # create console handler or file handler and set the log level
        consoleHandler = logging.StreamHandler()
        fileHandler = logging.FileHandler("testRun.log")
        # create formater
        formatter = logging.Formatter("%(asctime)s - %(levelname)s :- %(message)s")
        # add formater to console or file handler)
        consoleHandler.setFormatter(formatter)
        fileHandler.setFormatter(formatter)
        # add console handler or filehandler to the logger
        logger.addHandler(consoleHandler)
        logger.addHandler(fileHandler)
        return logger
